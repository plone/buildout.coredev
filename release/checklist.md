# Checklist for release

Create an issue in CMFPlone and copy the below text in it.
Edit where needed.
https://github.com/plone/Products.CMFPlone/issues/new?title=Release+checklist+Plone+6.0.x

See the [release schedule](https://plone.org/download/release-schedule).

## Release packages, update versions

- [ ] Check Jenkins Status: should be green. (This should be checked often during the release process.)
- [ ] In coredev, check packages for updates: `bin/manage report --interactive`. This is less needed now that we have `mr.roboto` to add packages to the checkouts.  Use `bin/versioncheck` to see if any new PyPI releases are worth adding, or check the artifact of the [versioncheck GitHub Action](https://github.com/plone/buildout.coredev/actions/workflows/versioncheck.yml).
- [ ] Release individual packages from `checkouts.cfg`.
- [ ] Check that the version numbers of [`CMFPlone metadata.xml`](https://github.com/plone/Products.CMFPlone/blob/master/Products/CMFPlone/profiles/default/metadata.xml) and latest [`upgrade step`](https://github.com/plone/plone.app.upgrade/blob/master/plone/app/upgrade/v60/configure.zcml) are in sync, and that they are higher than in the previous Plone release.
- [ ] Handle special packages, often handled by special people. :-) You can can ping people in the release-team channel on Discord, in the current issue, or individually:
  - [ ] [plonetheme.barceloneta](https://github.com/plone/plonetheme.barceloneta) needs a release on PyPI and npmjs. Maybe ask Peter Holzer (agitator) or Peter Mathis (petschki) for assistence.
  - [ ] [`plone.staticresources`](https://github.com/plone/plone.staticresources) and [`mockup`](https://github.com/plone/mockup). Ask on Discord in the classic-ui or ask Johannes (thet), Peter Mathis (petschki) or Maik (MrTango).
  - [ ] `plone.restapi` and maybe `plone.volto`. If needed, [ask the Plone REST api team](https://github.com/plone/plone.restapi/issues) or Timo (tisto) for a new release.
  - [ ] [`plone.app.locales`](https://github.com/collective/plone.app.locales). Create an issue there or ask Mikel (erral).
  - [ ] Release `plone.app.upgrade` and `Plone` yourself.
  - [ ] Update the versions of those packages in `versions.cfg`.
- [ ] Make an alpha/beta/release candidate release of `Products.CMFPlone` (e.g. 6.0.0a1, later 6.0.0b1 and 6.0.0rc1). Fine to release this on PyPI.  Once Plone 6 is final, we can continue doing release candidates for the bugfix releases, so people can try it in a pending release.

## Release notes, constraints, dist.plone.org

- [ ] Adjust coredev branch [`release/6.0-dev`](https://github.com/plone/buildout.coredev/tree/release/6.0-dev). Most importantly, the `auto-checkout` list in `checkouts.cfg` should be empty, and the `versions.cfg` and `requirements.txt` should be the same.  One way that works for me: `git checkout release/6.0-dev; git reset --hard 6.0; git reset origin/release/6.0-dev`.  Then check which changes you want to commit.
- [ ] Update the `6.0-dev` directory on dist.plone.org, and gather files to put there:
  - [ ] You can use `tox -c release/tox.ini -p auto` to create or copy some files in `release/dist`.  But you need to create some of those files first.
  - [ ] Create a unified changelog based on the previous release: `bin/manage changelog --start=6.0.0a1 > release/changelog.txt`. Remove the uninteresting top lines.  You may want to link to the [Zope changelog](https://github.com/zopefoundation/Zope/blob/master/CHANGES.rst) with a specific tag.
  - [ ] Create a file `release/RELEASE-NOTES.md`. It may be enough to look through the changelog and copy interesting changes.
  - [ ] Get the `versions.cfg` file and any other versions files from coredev.
  - [ ] Create a `release/constraints.txt` file from this. The above tox command generates this.  Note: at some point I expect the constraints file to become leading, and we may need to generate a `versions.cfg` file instead.
  - [ ] Copy (`rsync`) these files to the pending release directory.  (We used to copy packages as well, but we do not do this for Plone 6 anymore.)
- [ ] Write a post on community.plone.org announcing a pending/soft release. See [example](https://community.plone.org/t/plone-6-0-0b3-released/15728).  In the 6.0 alpha/beta/rc stage, we can skip pending releases and just make a real release.
- [ ] Wait for feedback, preferably at most a few days.  As said, in the alpha/beta/rc stage, we can skip this.

## Final release, Docker

- [ ] Make final release of `Products.CMFPlone` to PyPI, update `versions.cfg`.
- [ ] In `release/6.0-dev` branch update changelog, release notes, `constraints.txt`.
- [ ] Create tag of the `release/6.0-dev` branch, e.g. 6.0.0a1, and push to GitHub.
- [ ] Make final release directory on dist.plone.org, with versions, requirements, constraints, changelog, release notes.
- [ ] Update the "-latest" links on dist.plone.org, e.g. `ln -sfT 6.0.0a1 6.0-latest`
- [ ] Notify Erico Andrei and/or Fred van Dijk, for example the `#release-team` Discord channel, that there is a new release, so they can create Docker images then.  Sample changes: [`README.md`](https://github.com/plone/plone-backend/commit/0e3ce3c190677c04874ebed6b527a845cc075bca) and [`version.txt`](https://github.com/plone/plone-backend/commit/cee1e0bbb17ed24c64cd42342929a020346e1da1).

## Announcements

You probably want to wait until the Docker images are there, but don't wait long.

- [ ] Create release page on https://plone.org/download/releases
- [ ] Send mail to Marketing Team so they can prepare announcements.
- [ ] Update the https://plone.org/security/hotfixes/ page in the configuration control panel. This is done in the configuration registry: `plone.securitysupport`, `plone.versions`, `plone.activemaintenance`.  You could ask the security team.
- [ ] Publish release page on plone.org.
- [ ] Update the [release schedule](https://plone.org/download/release-schedule): note the new release, and say when the next release in this series is expected.
- [ ] Edit the link on https://plone.org/download.
- [ ] Announce on community.plone.org.
- [ ] Update Plone version in documentation.  Ask Steve Piercy or do it yourself.  Here is a [sample PR](https://github.com/plone/documentation/pull/1492/files).
- [ ] Ask Philip Bauer and/or Fred van Dijk to update the demo sites.  Here is a [sample PR](https://github.com/plone/demo.plone.org/pull/15).
