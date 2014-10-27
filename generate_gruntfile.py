p = app.Plone
from zope.site.hooks import setSite
setSite(p)

from zope.site.hooks import getSite


portal = getSite()

import json

from Products.CMFPlone.interfaces import (
    IBundleRegistry,
    IResourceRegistry)
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

registry = getUtility(IRegistry)
bundles = registry.collectionOfInterface(IBundleRegistry, prefix="plone.bundles")
resources = registry.collectionOfInterface(IResourceRegistry, prefix="plone.resources")
lessvariables = registry.records['plone.lessvariables'].value

gruntfile_template = """
module.exports = function(grunt) {{
    'use strict';
    grunt.initConfig({{
        pkg: grunt.file.readJSON('package.json'),
        less: {{
            {less}
        }},
        requirejs: {{
            {requirejs}
        }},
        watch: {{
            scripts: {{
                files: {files},
                tasks: ['requirejs', 'less']
            }}
        }}
    }});

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-requirejs');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-concat');

    grunt.registerTask('default', ['watch']);
    grunt.registerTask('compile', ['requirejs', 'less', 'concat']);
}}
"""

concat_config = """
            "{name}": {{
              src: {sources},
              dest: {destination},
            }},
"""

requirejs_config = """
            {bkey}: {{
                options: {{
                    baseUrl: '/',
                    generateSourceMaps: false,
                    preserveLicenseComments: false,
                    paths: {paths},
                    shim: {shims},
                    wrapShim: true,
                    name: '{name}',
                    out: '{out}',
                    optimize: "uglify"
                }}
            }},
"""

less_config = """
            {name}: {{
                options: {{
                    strictMath: false,
                    sourceMap: true,
                    outputSourceFiles: true,
                    relativeUrls: true,
                    modifyVars: {{
                      {globalVars}
                    }}
                }},
                files: {{
                    {files}                  
                }}
            }}
"""

less_trick = ".."
for i in range(20):
    less_trick += "/.."


from plone.resource.file import FilesystemFile
from Products.Five.browser.resource import FileResource
from Products.Five.browser.resource import DirectoryResource
from plone.resource.directory import FilesystemResourceDirectory


def resource_to_dir(resource):
    if resource.__module__ == 'Products.Five.metaclass':
        try:
            return resource.chooseContext().path
        except:
            try:
                return resource.context.path
            except:
                return None
    elif isinstance(resource, FilesystemFile):
        return resource.path
    elif isinstance(resource, FileResource):
        return resource.chooseContext().path
    elif isinstance(resource, DirectoryResource):
        return resource.context.path
    elif isinstance(resource, FilesystemResourceDirectory):
        return resource.directory
    else:
        print "Missing resource type"
        return None

# REQUIRE JS CONFIGURATION

paths = {}
shims = {}
for requirejs, script in resources.items():
    if script.js:
        # Main resource js file
        resource_file = portal.unrestrictedTraverse(script.js, None)
        if resource_file:
            src = resource_to_dir(resource_file)
            if src:
                # Extract .js
                paths[requirejs] = src[:-3]
                exports = script.export
                deps = script.deps
                inits = script.init
                if exports != '' or deps != '' or inits != '':
                    shims[requirejs] = {}
                    if exports != '' and exports is not None:
                        shims[requirejs]['exports'] = exports
                    if deps != '' and deps is not None:
                        shims[requirejs]['deps'] = deps.split(',')
                    if inits != '' and inits is not None:
                        shims[requirejs]['init'] = inits
        else:
            print "No file found: " + script.js
    if script.url:
        # Resources available under name-url name
        paths[requirejs + '-url'] = resource_to_dir(portal.unrestrictedTraverse(script.url))


# LESS CONFIGURATION

globalVars = {}
globalVars["sitePath"] = "'/'"
globalVars["isPlone"] = "false"
globalVars["isMockup"] = "false"

less_vars_params = {
    'site_url': 'LOCAL',
}

# Storing variables to use them on further vars
for name, value in lessvariables.items():
    less_vars_params[name] = value

for name, value in lessvariables.items():
    t = value.format(**less_vars_params)
    if 'LOCAL' in t:
        t_object = portal.unrestrictedTraverse(str(t.replace('LOCAL/', '').replace('\\"', '')), None)
        if t_object:
            t_file = resource_to_dir(t_object)
            globalVars[name] = "'%s%s/'" % (less_trick, t_file)
        else:
            print "No file found: " + str(t.replace('LOCAL/', '').replace('\\"', ''))
    else:
        globalVars[name] = t

for name, value in resources.items():
    for css in value.css:
        # less vars can't have dots on it
        local_src = portal.unrestrictedTraverse(css, None)
        if local_src:
            local_file = resource_to_dir(local_src)
            globalVars[name.replace('.', '_')] = "'%s%s'" % (less_trick, local_file)
        else:
            print "No file found: " + css

globalVars_string = ""
for g, src in globalVars.items():
    globalVars_string += "\"%s\": \"%s\",\n" % (g, src)

# BUNDLE LOOP

require_configs = ""
less_files = ""
less_final_config = ""
watch_files = []

for bkey, bundle in bundles.items():
    if bundle.compile:
        for resource in bundle.resources:
            res_obj = resources[resource]
            if res_obj.js:
                js_object = portal.unrestrictedTraverse(res_obj.js, None)
                if js_object:
                    main_js_path = resource_to_dir(js_object)
                    target_dir = '/'.join(bundle.jscompilation.split('/')[:-1])
                    target_name = bundle.jscompilation.split('/')[-1]
                    target_path = resource_to_dir(portal.unrestrictedTraverse(target_dir))
                    watch_files.append(main_js_path)
                    rc = requirejs_config.format(
                        bkey=resource,
                        paths=json.dumps(paths),
                        shims=json.dumps(shims),
                        name=main_js_path,
                        out=target_path + '/' + target_name
                    )
                    require_configs += rc

            if res_obj.css:
                for css_file in res_obj.css:
                    css = portal.unrestrictedTraverse(css_file, None)
                    if css:
                        main_css_path = resource_to_dir(css)
                        target_dir = '/'.join(bundle.csscompilation.split('/')[:-1])
                        target_name = bundle.csscompilation.split('/')[-1]
                        target_path = resource_to_dir(portal.unrestrictedTraverse(target_dir))
                        less_file = "\"%s/%s\": \"%s\"," % (target_path, target_name, main_css_path)
                        less_files += less_file
                        watch_files.append(main_css_path)
                    else:
                        print "No file found: " + script.js
                less_files += '\n'
        less_final_config = less_config.format(
            name=bkey,
            globalVars=globalVars_string,
            files=less_files)


gruntfile = open('Gruntfile.js', 'w')
gruntfile.write(gruntfile_template.format(
    less=less_final_config,
    requirejs=require_configs,
    files=json.dumps(watch_files))
)
gruntfile.close()
