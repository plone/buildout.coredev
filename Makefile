SHELL := /bin/bash
CURRENT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

# We like colors
# From: https://coderwall.com/p/izxssa/colored-makefile-for-golang-projects
RED=`tput setaf 1`
GREEN=`tput setaf 2`
RESET=`tput sgr0`
YELLOW=`tput setaf 3`

all: build

# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
.PHONY: help
help: ## This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: all
all: build

.PHONY: build
build:
	python3 -m venv .
	bin/pip install --upgrade pip
	bin/pip install -r requirements.txt
	bin/buildout

.PHONY: clean
clean: ## Remove old virtualenv and creates a new one
	@echo "Clean"
	rm -rf develop-eggs eggs bin lib include share .Python .installed.cfg .mr.developer.cfg

.PHONY: test
test: ## Run tests
	@echo "$(GREEN)==> Run Tests$(RESET)"
	bin/test --xml

.PHONY: test-acceptance
test-acceptance: ## Run acceptance tests
	@echo "$(GREEN)==> Run Acceptance Tests$(RESET)"
	export ROBOTSUITE_PREFIX=ONLYROBOT && bin/alltests -t ONLYROBOT --all --xml

.PHONY: pip-bootstrap
pip-bootstrap:  ## Pip: Bootstrap a venv for tests (future: several venvs with less installed)
	mkdir -p venvs
	python3 -m venv venvs/test
	./venvs/test/bin/pip install --upgrade -r requirements-bootstrap.txt

.PHONY: mxdev-generate
mxdev-generate:  ## mxdev: generate requirements and constraints files without pulling sources
	./venvs/test/bin/mxdev -c mxdev.ini -n

.PHONY: mxdev-update
mxdev-update:  ## mxdev: update requirements and constraints files and pull the sources
	./venvs/test/bin/mxdev -c mxdev.ini

.PHONY: pip-update
pip-update:  ## Pip: Update a venv for tests (future: several venvs with less installed)
    # uv seems to act on the current directory.
	cd venvs/test && bin/uv pip install -r ../../requirements-test.txt

.PHONY: pip-test
pip-test:  ## Pip: Run only a few unit tests, as proof of concept.
	./venvs/test/bin/zope-testrunner --path venvs/test/lib/*/site-packages/ -u -s Products.CMFPlone
