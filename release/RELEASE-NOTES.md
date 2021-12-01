# Release notes for Plone 6.0.0 dev

Last updated: Wednesday December 1, 2021.

## Highlights

Changes since 6.0.0a1:

- plone.app.contenttypes: Remove atcontenttypes dependencies and most migration code, and removed backwards compatibility ATContentTypes view name registrations.
- plone.app.layout: Moved most portlet related code to `plone.app.portlets`.  Removed long deprecated `getIcon` from layout-policy.
- plone.app.textfield and plone.app.z3cform: Restored ability to enable multiple wysiwyg editors. This change will end up in Plone 5.2 as well.
- plone.app.z3cform: Enable formautofocus for Plone forms. Allow disabling it for specific forms with `enable_autofocus = False`.
- plone.dexterity: Removed dependency on `plone.synchronize`, and copy its one and only simple `synchronized` function.
- plone.restapi: Enable table blocks indexing. Return non-batched vocabularies given a query param `b_size=-1`.  Add root (INavigationRoot) for the current object information in @translations endpoint. Implement `IJSONSummarySerializerMetadata` allowing addons to extend the metadata returned by Summary serializer. Enable usage of metadata_fields also for POST calls.
- plonetheme.barceloneta: Make loading of webfont optional. Move Barceloneta specific styles out of `base.scss`. Update to Bootstrap 5.1.3.


## Expected

There are some items that we want to include during the alpha phase, but which are not ready yet:

- Updated JavaScript for Plone Classic, using ES6 modules.  No more through-the-web compiling of JavaScript. See [PLIP 3211](https://github.com/plone/Products.CMFPlone/issues/3211).
- Replace `z3c.autoinclude` with `plone.autoinclude`.  No more `includeDependencies`.  See [Plip 3339](https://github.com/plone/Products.CMFPlone/issues/3339).
- An updated installation method to more easily combine the node frontend and Python backend. See [community post](https://community.plone.org/t/our-pip-based-development-workflow-for-plone/14562).


## Installation

Some documentation about installation:

- Installation instructions from the Mastering Plone 6 training:
  https://training.plone.org/5/mastering-plone/installation.html
- Volto frontend installation:
  https://docs.voltocms.com/getting-started/install/
- [Community post](https://community.plone.org/t/our-pip-based-development-workflow-for-plone/14562) on work in progress.

If you use Docker, we have some images:

- `plone/plone-backend` (5.2 and 6.0)
- `plone/plone-frontend` (Volto)
- `plone/plone-haproxy`

If you don't do Docker, you will have to do the backend by hand.
The links above should give you information on how to install the prerequisites, like Python, also on Windows.
Here, we will focus on Unix-like systems (Linux, Mac OSX), but Windows should work as well.
The steps are:

* Install the Plone (Classic) backend with buildout or pip.
* Create the Plone Site in the browser.
* Install the Plone frontend (Volto) with node.


## Install backend with buildout

Change to a new directory and put a file `buildout.cfg` in it:

```
[buildout]
extends = https://dist.plone.org/release/6.0-dev/versions.cfg
parts = instance

[instance]
recipe = plone.recipe.zope2instance
eggs =
    Plone
    plone.volto
user = admin:admin
zodb-temporary-storage = off
```

Install it with:

```
python3.9 -m venv .
bin/pip install -r https://dist.plone.org/release/6.0-dev/requirements.txt
bin/buildout
bin/instance fg
```


## Install backend with pip

If you don't want to use buildout, you can install the Plone Python packages with `pip`.
Change to a new directory and then:

```
python3.9 -m venv .
bin/pip install -U pip setuptools wheel
bin/pip install Plone plone.volto -c https://dist.plone.org/release/6.0-dev/constraints.txt --use-deprecated legacy-resolver
bin/mkwsgiinstance -u admin:admin -d .
bin/runwsgi -v etc/zope.ini
```


## Create Plone backend

After you have installed the backend with buildout or pip, open a browser and go to http://localhost:8080/.
If you want Plone Classic, click 'Create a new Plone site'.
If instead you want to prepare for the new Volto frontend, click the Advanced button.
In the Advanced form:

* Make sure the Path identifier is Plone.  (You can change this, but then you need to change some Volto configuration as well.)
* uncheck 'Example content'
* check 'Plone 6 Frontend (Default content on homepage)'
* check 'Plone 6 Frontend (plone.volto)'

Submit the form and your backend is ready.
If you want Classic Plone, you are done.
If you want the full Plone 6 with Volto, read on.


## Frontend with node

You should probably read one of documentation pages linked above.
But the following gives you the general idea.

First install nvm, the Node Version Manager

* On Linux: `apt-get install nvm`
* On Mac: `brew install nvm`
* Or use the installation procedure detailed in the [nvm documentation](https://github.com/nvm-sh/nvm)

Create a Volto project:

```
nvm install --lts
npm install --global yarn
npm init yo @plone/volto
```

This will take long, and then ask for a project name.
It will create a directory with this name.
Go to that directory and start the frontend:

```
yarn start
```

In your browser go to http://localhost:3000.

You are done.  Welcome to Plone 6!
