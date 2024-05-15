PYTHON_MIN_VERSION=3.10

# Plone releaser
PLONERELEASER_TARGET:=$(SENTINEL_FOLDER)/plonereleaser.sentinel
$(PLONERELEASER_TARGET): $(MXENV_TARGET)
	@echo "Install plone.releaser"
	@$(PYTHON_PACKAGE_COMMAND) install plone.releaser
#	@$(PYTHON_PACKAGE_COMMAND) install git+https://github.com/plone/plone.releaser.git@master#plone.releaser
	@touch $(PLONERELEASER_TARGET)

.PHONY: plonereleaser-dirty
plonereleaser-dirty:
	@rm -f $(PLONERELEASER_TARGET)

.PHONY: plonereleaser-clean
plonereleaser-clean: plonereleaser-dirty
	@test -e $(MXENV_PYTHON) && $(MXENV_PYTHON) -m pip uninstall -y plone.releaser || :

INSTALL_TARGETS+=$(PLONERELEASER_TARGET)
CHECK_TARGETS+=plonereleaser-check
FORMAT_TARGETS+=plonereleaser-format
DIRTY_TARGETS+=plonereleaser-dirty
CLEAN_TARGETS+=plonereleaser-clean

# versions2constraints
VERSIONS2CONSTRAINTS_TARGET:=constraints.txt constraints-ecosystem.txt constraints-extra.txt
$(VERSIONS2CONSTRAINTS_TARGET): $(PLONERELEASER_TARGET) versions.cfg versions-ecosystem.cfg versions-extra.cfg
	@echo "Generate pip constraints from buildout"
	@manage versions2constraints


# buildout2pip
BUILDOUT2PIP_TARGET:=mxsources.ini mxcheckouts.ini
$(BUILDOUT2PIP_TARGET): $(PLONERELEASER_TARGET) checkouts.cfg sources.cfg
	@echo "Generate mx sources and checkouts from buildout"
	@manage buildout2pip


# configure to run pre sources
PRE_SOURCES_TARGETS+=$(BUILDOUT2PIP_TARGET) $(VERSIONS2CONSTRAINTS_TARGET)

.PHONY: run-presources
run-presources: $(PRE_SOURCES_TARGETS)
	@echo "Manual run pre sources targets"

