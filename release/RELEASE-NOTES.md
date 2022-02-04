# Release notes for Plone 6.0-dev

Last updated: Friday February 4, 2022.

## Highlights

Changes since 6.0.0a3:

- collective.recipe.template = 2.2
- plone.app.querystring = 1.5.0
- plone.app.versioningbehavior = 1.4.6
- plone.app.tiles = 3.3.0

## Expected

There are some items that we want to include during the alpha phase, but which are not ready yet:

- Updated JavaScript for Plone Classic, using ES6 modules.  No more through-the-web compiling of JavaScript. See [PLIP 3211](https://github.com/plone/Products.CMFPlone/issues/3211).
- Add `plone.volto` as dependency of the `Plone` package.  See [issue 1](https://github.com/plone/plone.volto/issues/1).
- Add `plone.base` as basic package with shared code.  See [issue 3395](https://github.com/plone/Products.CMFPlone/issues/3395).


## Installation

Some documentation about installation:

- Installation instructions from the Mastering Plone 6 training:
  https://training.plone.org/5/mastering-plone/installation.html
- Volto frontend installation:
  https://docs.voltocms.com/getting-started/install/
- [Community post](https://community.plone.org/t/our-pip-based-development-workflow-for-plone/14562) on work in progress with [`plone-kickstarter`](https://github.com/bluedynamics/plone-kickstarter) and [`mxdev`](https://github.com/bluedynamics/mxdev).

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
extends = https://dist.plone.org/release/6.0.0a3/versions.cfg
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
bin/pip install -r https://dist.plone.org/release/6.0.0a3/requirements.txt
bin/buildout
bin/instance fg
```


## Install backend with pip

If you don't want to use buildout, you can install the Plone Python packages with `pip`.
Change to a new directory and then:

```
python3.9 -m venv .
bin/pip install -U pip setuptools wheel
bin/pip install Plone plone.volto -c https://dist.plone.org/release/6.0.0a3v/constraints.txt --use-deprecated legacy-resolver
bin/mkwsgiinstance -u admin:admin -d .
bin/runwsgi -v etc/zope.ini
```


## Create Plone backend

After you have installed the backend with buildout or pip, open a browser and go to http://localhost:8080/.
Click 'Create a new Plone site' to prepare for the new Volto frontend.
If you want Plone Classic instead, click 'Create Classic Plone site'.
(If this button is not available, then you did not install `plone.volto` with buildout or pip. 'Create a new Plone site' will create a Classic site then.)

Note: For Volto, make sure the Path identifier is Plone.  You can change this, but then you need to change some Volto frontend configuration as well.

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
