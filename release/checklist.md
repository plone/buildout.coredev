# Checklist for release

Create an issue in CMFPlone and copy the below text in it.
Edit where needed.
https://github.com/plone/Products.CMFPlone/issues/new?title=Release+checklist+Plone+6.0.x

See the [release schedule](https://plone.org/download/release-schedule).

- [ ] Check Jenkins Status: should be green. (This should be checked often during the release process.)
- [ ] In coredev, check packages for updates: `bin/manage report --interactive`
- [ ] Release individual packages from `checkouts.cfg`.
- [ ] Check that the version numbers of [`CMFPlone metadata.xml`](https://github.com/plone/Products.CMFPlone/blob/master/Products/CMFPlone/profiles/default/metadata.xml) and latest [`upgrade step`](https://github.com/plone/plone.app.upgrade/blob/master/plone/app/upgrade/v60/configure.zcml) are in sync, and that they are higher than in the previous Plone release.
- [ ] Ask Peter Holzer for an NPM release of https://github.com/plone/plonetheme.barceloneta, and make a Python release yourself.
- [ ] If needed, [ask the Plone REST api team](https://github.com/plone/plone.restapi/issues) for a new release of `plone.restapi` and `plone.rest`, and maybe `plone.volto`.
- [ ] Write an email to the translation team, asking them to do a plone.app.locales release. Or create an issue in https://github.com/collective/plone.app.locales/issues
- [ ] Update the versions of those packages.
- [ ] Make an alpha/beta/release candidate release of `Products.CMFPlone` (e.g. 6.0.0a1, later 6.0.0b1 and 6.0.0rc1). Fine to release this on PyPI.
- [ ] Adjust coredev branch `release/6.0-dev`. Most importantly, the `auto-checkout` list in `checkouts.cfg` should be empty, and the `versions.cfg` and `requirements.txt` should be the same.
- [ ] Update the `6.0-dev` directory on dist.plone.org, and gather files to put there:
  - [ ] You can use `tox -c release/tox.ini -p auto` to create or copy some files in `release/dist`.  But you need to create some of those files first.
  - [ ] Create a unified changelog based on the previous release: `bin/manage changelog --start=6.0.0a1 > release/changelog.txt`. Remove the uninteresting top lines.
  - [ ] Create a file `release/RELEASE-NOTES.md`. It may be enough to look through the changelog and copy interesting changes.
  - [ ] Get the versions.cfg file from coredev.
  - [ ] Create a `release/constraints.txt` file from this. The above tox command generates this.  Note: at some point I expect the constraints file to become leading, and we may need to generate a `versions.cfg` file instead.
  - [ ] Copy (`rsync`) these files to the pending release directory.  (We used to copy packages as well, but let's not do this for Plone 6 anymore.)
- [ ] Write a post on community.plone.org announcing a pending/soft release. See [example](https://community.plone.org/t/plone-5-2-4-soft-released/13495).  In the 6.0 alpha/beta/rc stage, we can skip pending releases and just make a real release.
- [ ] Wait for feedback, preferably at most a few days.  As said, in the alpha/beta/rc stage, we can probably skip this.
- [ ] Make final release of `Products.CMFPlone` to PyPI, update `versions.cfg`.
- [ ] Create tag of the release branch, e.g. 6.0.0a1, and push to GitHub.
- [ ] Make final release directory on dist.plone.org, with versions, requirements, constraints, changelog, release notes.
- [ ] Update the "-latest" links on dist.plone.org, e.g. `ln -sfT 6.0.0a1 6.0-latest`
- [ ] Create new release on launchpad (https://launchpad.net/plone/): `bin/manage launchpad <version>`.  Actually, since we do not create and upload universal installers for Plone 6, we could probably skip this.
- [ ] Notify Erico, perhaps on the `#install-and-deploy` Discord channel, that there is a new release.  He can create Docker images then.
- [ ] Create release page on https://plone.org/download/releases
- [ ] Announce on community.plone.org.  Perhaps wait until the Docker images are there, but don't wait long.
- [ ] Publish release page on plone.org. If the installer takes too long, publish it anyway. Coordinate with the Marketing Team.
- [ ] Marketing Team: Send out announcement to plone-announce, Twitter, update #plone irc channel topic, what you want.
- [ ] Ask the security team to update the https://plone.org/security/hotfixes/ page in the configuration control panel. (Configuration registry: `plone.securitysupport`, `plone.versions`, `plone.activemaintenance`)
