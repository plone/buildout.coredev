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
all: build code-analysis test test-acceptance

.PHONY: build-py2
build-py2: ## Create virtualenv and run buildout
	@echo "$(GREEN)==> Setup Virtual Env$(RESET)"
	virtualenv -p python2 --clear .
	bin/pip install pip --upgrade
	bin/pip install -r requirements.txt --upgrade
	bin/buildout

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

.PHONY: code-analysis
code-analysis: ## Run static code analysis
	@echo "$(GREEN)==> Run static code analysis$(RESET)"
	bin/code-analysis

.PHONY: test
test: ## Run tests
	@echo "$(GREEN)==> Run Tests$(RESET)"
	bin/alltests --xml

.PHONY: test-acceptance
test-acceptance: ## Run acceptance tests
	@echo "$(GREEN)==> Run Acceptance Tests$(RESET)"
	export ROBOTSUITE_PREFIX=ONLYROBOT && bin/alltests -t ONLYROBOT --all --xml
