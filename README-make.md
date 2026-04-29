# Using the Makefile in buildout.coredev

Traditionally, the way to run `buildout.coredev`, was to use Buildout, and you can still do that.
Basically:

```
python -mvenv .
bin/pip install -r requirements.txt
bin/buildout
```

Buildout is not well known outside of the Plone world, and it can have problems when a new `pip` or `setuptools` version is released.
So we are busy putting pip on the same level as Buildout for doing core development.
See [CMFPlone issue 3670](https://github.com/plone/Products.CMFPlone/issues/3670).

This document describes the current status, and mostly how you use the included `Makefile`.
This is work in progress.  Once things have settled over the coming months, we can put this in the main documentation.

Remember: for now you can still choose to ignore this and continue to use Buildout for core Plone development.


## Goal

The goal of the `Makefile` is to offer a pip-based alternative for what Buildout has offered so far.
Those are:

* Define which versions of Python packages to use.
* Define for which packages we should ignore the version pin and use a checkout instead, using the `mr.developer` Buildout extension.
* Create a Plone instance based on some configuration.
* Create a script for starting Plone: `bin/instance fg`
* Create a script for running tests of core Plone packages: `bin/test` or `bin/test -s package.name`


## Tools

First, there are some tools you should know about.


### `plone.releaser`

[`plone.releaser`](https://github.com/plone/plone.releaser) is our wrapper around [`zest.releaser`](https://github.com/zestsoftware/zest.releaser), used for releasing Pythong packages.
But it also introduces a `manage` script that has recently gotten some extra commands.
These are needed to translate between our current Buildout files and what we need for `pip`.

* `manage versions2constraints` takes the `versions*.cfg` files and translates them to `constraints*.txt` files for use by `pip`.
* `manage buildout2pip` does the same, but also translates `sources.cfg` and `checkouts.cfg` (used by `mr.developer`) to `mxsources.ini` and `mxcheckouts.ini` (for use by `mxdev`).

In the future there should be commands that do the opposite, so we can start treating the `pip/mxdev` files as canonical, and generate their Buildout counterparts for those still using Buildout.


### mxdev

`mxdev` is used instead of the `mr.developer` Buildout extension.
Its goal is to take requirements and constraints, and ignore some of the constraints to replace them with source checkouts.
The end result are some files that `pip` (or `uv`) then uses to install Python packages.

See https://github.com/mxstack/mxdev/tree/main


### mxmake

`mxmake` was used to generate the `Makefile`.
This means you should not edit the `Makefile` by hand.
Please only touch `include.mk` if anything needs to be changed or extra targets are needed.

Every now and then we can regenerate the `Makefile`.
TODO: how do we do that?

See https://mxstack.github.io/mxmake


## How to use the `Makefile`

At the top of the `Makefile` you see several domains or topics that are included.
These [topics are documented](https://mxstack.github.io/mxmake/topics.html).
So if you want details about `make` targets, you can look there.
Here, let me introduce the main ones.


### Install

`make install` calls several other `make` targets, listed in `INSTALL_TARGETS`.
If you `grep INSTALL_TARGETS Makefile include.mk` you can see which they are.
Currently:

* mxenv
* sources
* mxfiles
* packages
* zope-instance
* PLONERELEASER_TARGET, which installs `plone.releaser`

You can call those targets individually as well, if you know you want to run a specific one.

Main results:

* In the `src` directory there are checkouts of packages, just like `mr.developer` would do.
  You can still use Buildout and `mr.developer` next to this: the two approaches can work side by side.
* In `.venv` there is a virtual environment with Plone and all test requirements installed.
* In `instance` a Zope instance is created.

Important: you may need to run `make install` twice, especially after you change something.
These large Makefiles are tricky.

### Start

Run `make zope-start` to start the Zope instance.

### The `manage` command

The `manage` command from `plone.releaser` can be used in various ways.
It knows how to query or update files from both buildout and pip:

See the help text:

```shell
make manage ARGS="--help"
```

### Manage checkouts

Add a package to the checkouts:

```shell
make manage ARGS="add-checkout plone.restapi"
```

This does not yet checkout the package: it only updates the `checkouts.cfg` and `mxcheckouts.ini` files.
To *use* the new checkout, you still need to run `make install`.
If the new checkout is still not used, you can more agressively get a new environment:
`make mxenv-clean` and `make install`.

Remove a package from the checkouts:

```shell
make manage ARGS="remove-checkout plone.restapi"
```

Similarly, you still need to call `make install` after this.

### Manage versions

Update a package version:

```shell
make manage ARGS="set-package-version plone.restapi 10.0.0"
```

Again, you still need to call `make install` to actually install the new version.


### Run tests

Use the `make test` target to run tests for one or more packages.
Without extra arguments, this runs all tests (except robot tests) for all packages that we want to test in core.

```shell
make test
```

To influence what tests are run, you can use `TEST_ARGS` and/or `TEST_PACKAGE`.
You can pass these on the command line or set them as an environment variable.

Run all unit and functional tests for a given package:

```shell
make test TEST_PACKAGE=plone.namedfile
```

Alternatively:

```shell
export TEST_PACKAGE=plone.namedfile
make test
```

Note that this tests the *installed* version of the package.
This can be a final version in `site-packages` or a source checkout.
See the section "Manage checkouts and versions" on how to influence what is installed.

Note: Simply having a package directory under `src/` is not enough for `make test` to pick it up.
This may be an old checkout that is not currently active.
You need to explicitly add it as a checkout and reinstall:

```
make manage ARGS="add-checkout plone.restapi"
make mxenv-clean
make install
```

Only after this will `make test TEST_PACKAGE=plone.restapi` use the source from src/.

Under the hood, the `test` target calls `zope-testrunner`.
To find out which arguments this supports, ask for help:

```shell
make test TEST_ARGS=--help
```

Run all pure unit tests (so no test layers) for all packages:

```shell
make test TEST_ARGS=-u
```

Enter an interactive prompt after the first test failure:

```shell
make test TEST_ARGS=-D
```

List all tests for a given package

```shell
make test TEST_ARGS=--list-tests TEST_PACKAGE=plone.namedfile
```

Run tests for multiple packages:

```shell
make test TEST_ARGS='-m plone.namedfile -m plone.scale'
```

Note: using `-s` instead of `-m` in the previous example won't work.
`make test` calls a command that already passes about 100 packages with `-s`, unless you override it with `TEST_PACKAGE`.


#### Robot tests

To run robot tests, you must do two things.
First you must install or sync the robotframework browser packages, which is done with NodeJS:

```shell
make rfbrowser
```

You need to do this only once per testing session:
you can make multiple `make test` calls with robot tests after this.

Second: pass the `--all` argument.
Otherwise robot tests are skipped.

Run all pure unit, functional, and robot tests for a package:

```shell
make test TEST_ARGS=--all TEST_PACKAGE=Products.CMFPlone
```

Run only the robot tests for a package:

```shell
make test TEST_ARGS='-t ONLYROBOT --all' TEST_PACKAGE=Products.CMFPlone
```

To watch the browser run Robot Framework tests, set the `ROBOT_BROWSER` environment variable.

The following example runs a specific Robot test with the Chrome browser visible:

```shell
ROBOT_BROWSER=chrome make test TEST_PACKAGE=plone.schemaeditor TEST_ARGS='--all -t "Add a fieldSet and move a field into this fieldset"'
```


### Dirty and clean

Most targets have two related targets, for "dirty" and "clean".
What do these do?
Let's give an example.

* `make mxfiles` creates `constraints-mxdev.txt requirements-mxdev.txt`
* Run `make mxfiles` again, and nothing happens, because everything is up to date.
* `make mxfiles-dirty` signals to make that the `mxfiles` target is "dirty".
* This means that the next run of `make mxfiles` will create the files again.
* You can also call `make mxfiles-clean`.
  This has the same effect as `make mxfiles-dirty`, but it also cleans:
  it removes the files that were created by the previous `make mxfiles` call.
