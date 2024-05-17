# Plone releaser
PLONERELEASER_TARGET:=$(SENTINEL_FOLDER)/plonereleaser.sentinel
$(PLONERELEASER_TARGET): $(MXENV_TARGET)
	@echo "Install plone.releaser"
#	 @$(PYTHON_PACKAGE_COMMAND) install plone.releaser
	@$(PYTHON_PACKAGE_COMMAND) install git+https://github.com/plone/plone.releaser.git@maurits-pip-sources#plone.releaser
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
VERSIONS2CONSTRAINTS_TARGET:=constraints.txt
$(VERSIONS2CONSTRAINTS_TARGET): $(PLONERELEASER_TARGET)
	@echo "Generate constraints.txt from buildout"
	@manage versions2constraints



# buildout2pip
BUILDOUT2PIP_TARGET:=mxsources.txt mxcheckouts.txt
$(BUILDOUT2PIP_TARGET): $(PLONERELEASER_TARGET)
	@echo "Generate mx sources and checkouts from buildout"
	@manage buildout2pip


# configure to run pre sources
PRE_SOURCES_TARGETS+= $(BUILDOUT2PIP_TARGET)


