# Checklist for release

Create an issue in CMFPlone and copy the below text in it.
Edit where needed.
https://github.com/plone/Products.CMFPlone/issues/new?title=Release+checklist+Plone+6.2.x

## Release packages, update versions

- [ ] Check Jenkins Status: should be green.  (This should be checked often during the release process.)
- [ ] In coredev, check packages for updates: `bin/manage report --interactive`.  This is less needed now that we have `mr.roboto` to add packages to the checkouts.  Use `bin/versioncheck` to see if any new PyPI releases are worth adding, or check the artifact of the [versioncheck GitHub Action](https://github.com/plone/buildout.coredev/actions/workflows/versioncheck.yml).
- [ ] Release individual packages from `checkouts.cfg`.
- [ ] Check that the version numbers of [`CMFPlone metadata.xml`](https://github.com/plone/Products.CMFPlone/blob/master/Products/CMFPlone/profiles/default/metadata.xml) and latest [`upgrade step`](https://github.com/plone/plone.app.upgrade/blob/master/plone/app/upgrade/v61/configure.zcml) are in sync, and that they are higher than in the previous Plone release.
- [ ] Handle special packages, often handled by special people.  :-) You can can ping people in the release-team channel on Discord, in the current issue, or individually:
  - [ ] [`plonetheme.barceloneta`](https://github.com/plone/plonetheme.barceloneta) and [`plone.staticresources`](https://github.com/plone/plone.staticresources) need a release on PyPI and npmjs.  Maybe [`plone.classicui`](https://github.com/plone/plone.classicui).  Ask Peter Mathis (petschki), Johannes (thet) or Maik (MrTango).
  - [ ] [`plone.restapi`](https://github.com/plone/plone.restapi) and maybe [`plone.volto`](https://github.com/plone/plone.volto).  Ask David (davisagli) or Timo (tisto).
  - [ ] [`plone.app.locales`](https://github.com/collective/plone.app.locales).  Ask Mikel (erral).
  - [ ] Release `plone.app.upgrade`, `Plone` and `Products.CMFPlone` yourself.
  - [ ] Update the versions of those packages in `versions.cfg`.  This is done automatically if you are in a checkout of the package within `buildout.coredev` and run `../../bin/fullrelease`.  Or run `bin/manage set-package-version package-name new-version`.

## Release notes, constraints, dist.plone.org

- [ ] Adjust coredev branch [`release/6.2-dev`](https://github.com/plone/buildout.coredev/tree/release/6.2-dev).  Most importantly, the `auto-checkout` list in `checkouts.cfg` should be empty, and the `versions.cfg` and `requirements.txt` should be the same.  One way that works for me: `git switch release/6.2-dev; git reset --hard 6.2; git reset origin/release/6.2-dev; git checkout .package_ignores checkouts.cfg last_commit.txt mxcheckouts.ini`.  Then check which remaining changes you want to commit.
- [ ] Update the `6.2-dev` directory on dist.plone.org, and gather files to put there:
  - [ ] Create a unified changelog based on the previous release: `bin/manage changelog --start=6.2.0a1 > release/changelog.txt`.  Remove the uninteresting top lines.  You may want to link to the [Zope changelog](https://github.com/zopefoundation/Zope/blob/master/CHANGES.rst) with a specific tag.
  - [ ] Create a file `release/RELEASE-NOTES.md`.  It may be enough to look through the changelog and copy interesting changes.
  - [ ] Get the `versions*.cfg` file and any other versions files from coredev.
  - [ ] NEW.  Run `make install`.  This uses `mxdev` to install packages and generate some files.  Most importantly this generates `constraints-mxdev.txt`.  This contains *all* constraints, *and* makes sure no constraints are in there twice (provided that `mx.ini` is correct).  This is really the only constraints file that is needed and that is correct.  So for now I will only ship this one and call it `constraints.txt` on dist.plone.org.  This may need some more thought and updates in next releases.
  - [ ] Use `tox -c release/tox.ini` to copy these files to `release/dist`.
  - [ ] Copy (`rsync`) these files to the pending release directory: `scp release/dist/* dist.plone.org:release/6.2-dev/`

## Final release, Docker

- [ ] Create tag of the `release/6.2-dev` branch, e.g.  6.2.0a1, and push to GitHub.
- [ ] Make final release directory on dist.plone.org, with versions, requirements, constraints, changelog, release notes.
- [ ] Update the "-latest" links on dist.plone.org, e.g.  `ln -sfT 6.2.0a1 6.2-latest`
- [ ] Create a pull request for the [`plone-backend`](https://github.com/plone/plone-backend) Docker image with the new version number.  Get this reviewed, merged, tagged, released.

## Announcements

You probably want to wait until the Docker images are there, but don't wait long.

- [ ] Create release page on https://plone.org/download/releases.  This currently needs the Classic UI and some workarounds:
  - Go to the https://plone.org/ClassicUI/failsafe_login_form and login.  Not with your GitHub username, but a special user.  Ask the A/I team if you don't know.
  - In https://plone.org/ClassicUI/download/releases/ add a new Plone Release.
  - In the text you need the html of release notes.  What I do: create a new post on community.plone.org, copy the release notes (MarkDown) in there, copy the html output, and save as a draft.  Then paste the html in the Release notes field.  Copy `changelog.txt` in the other field.
  - Go to the folder contents: https://plone.org/ClassicUI/download/releases/folder_contents.  Go to the last batch page, and move the new release to the top of the folder.
  - Go to the ZMI: https://plone.org/ClassicUI/download/releases/manage_main.  Rename `plonerelease` to `new version number`.
  - The rest can be done on the Volto side.
- [ ] Publish release page on plone.org.
- [ ] Update the https://plone.org/security/hotfixes/ page.
- [ ] Update the [release schedule](https://plone.org/download/release-schedule): note the new release, and say when the next release in this series is expected.
- [ ] Edit the link on https://plone.org/download.
- [ ] Announce on community.plone.org.
- [ ] Maybe make a PR for [`docs.plone.org`](https://github.com/plone/documentation), search and replace the previous bugfix or minor release number.  Currently nothing to do in a bugfix release.
- [ ] Send mail to Marketing Team so they can prepare announcements.
- [ ] Ask Philip Bauer and/or Fred van Dijk to update the demo sites.  Here is a [sample PR](https://github.com/plone/demo.plone.org/pull/15).  Mostly just a search and replace, except when you want to update Volto as well.
