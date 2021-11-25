# Release notes for Plone 6.0.0 alpha 1

Released: Friday October 22, 2021.

The first real alpha release of Plone 6 is here!


## Highlights

Some highlights of this release are:

- The big one: Volto as new front-end, using React, built with modern JavaScript tools.
- The backend is now called Plone Classic. It generally works the same as Plone 5.2, so if you are not ready for Volto yet, you can just use this.
- Removed Python 2 and Archetypes compatibility.
- Support only for Python 3.7, 3.8 and 3.9.
- Zope 5.3
- Removed `CMFQuickInstallerTool` dependency.
- Removed `CMFFormController` dependency and removed all remaining form controller scripts (`cpy`/`vpy`).
- Removed dependency on `Products.TemporaryFolder`.
  Note: in your `plone.recipe.zope2instance` buildout part, you must set `zodb-temporary-storage = off`,
  otherwise you get errors when starting Plone.
- Extensive overhaul of Plone UI elements based on Bootstrap 5 components.
- Introduction of icon resolver with use of `icon_expr` definitions.
- Barceloneta LTS theme
- Add control panel for relations
- Add plone.api.relation module to ease using relations.
- Use Dexterity for the Plone Site root object.
- Add a traverser `++api++` as an alternative to mark a request as REST request.


## Expected

There are some items that we want to include during the alpha phase, but which are not ready yet:

- Updated JavaScript for Plone Classic, using ES6 modules.  No more through-the-web compiling of JavaScript.
- Replace `z3c.autoinclude` with `plone.autoinclude`.  No more `includeDependencies`.
- An updated installation method to more easily combine the node frontend and Python backend.


## Installation

Some documentation about installation:

- Installation instructions from the Mastering Plone 6 training:
  https://training.plone.org/5/mastering-plone/installation.html
- Volto frontend installation:
  https://docs.voltocms.com/getting-started/install/

There is no Docker image for Plone 6 yet, so we will have to do the backend by hand.
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
extends = https://dist.plone.org/release/6.0.0a1/versions.cfg
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
bin/pip install -r https://dist.plone.org/release/6.0.0a1/requirements.txt
bin/buildout
bin/instance fg
```


## Install backend with pip

If you don't want to use buildout, you can install the Plone Python packages with `pip`.
Change to a new directory and then:

```
python3.9 -m venv .
bin/pip install -U pip setuptools wheel
bin/pip install Plone plone.volto -c https://dist.plone.org/release/6.0.0a1/constraints.txt --use-deprecated legacy-resolver
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
