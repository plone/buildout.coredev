# Notes for AI agents

## General

- This is the Plone 6.0 branch. It is based on Zope 5.13 and supports
  Python 3.9 up to 3.13. So the oldest supported Python is 3.9 and the
  newest is 3.13.
- This branch uses buildout for development. There is no mxdev and no
  `mx.ini`. The virtualenv is the repository root itself (`bin/python`,
  `bin/buildout`), and the eggs are in the buildout `eggs-directory`, not in
  the virtualenv.
- For pip users there is `release/constraints.txt`, generated from the
  buildout version files (see below).

- Don't install anything into the virtualenv, don't run `bin/buildout` and
  don't commit unless asked. When asked to commit, do it on a new branch.
- Put temporary files and helper scripts in a scratch directory, not in the
  repo.
- After changing pins, regenerate `release/constraints.txt` and do the
  verification steps under "Verifying" below.

## Checking pins for security vulnerabilities

Use this when asked to check pins for releases that fix vulnerabilities, and
to update the pins.

### How the version files fit together

- `versions.cfg` is the source of truth for core. It extends the Zope versions
  for this Plone version (see its `extends` line).
- `versions-extra.cfg` has pins for tools (zest.releaser and friends) and
  `versions-ecosystem.cfg` has pins for add-ons. `core.cfg` extends
  `versions-extra.cfg` first and then `bare.cfg` (which extends
  `versions.cfg`), so a pin in `versions.cfg` wins over one in
  `versions-extra.cfg`. `ecosystem.cfg` extends `core.cfg` and
  `versions-ecosystem.cfg`.
- The `# Basics` section of `versions.cfg` (packaging, pip, setuptools,
  wheel, zc.buildout) must match `requirements.txt`, including the
  Python-specific pins (e.g. pip, which has a `python_version == "3.9"` line
  in `requirements.txt` and a pin in `[versions:python39]`).
- To override a Zope pin, add it to the `# OVERRIDES` section of
  `versions.cfg`. Buildout simply uses the last pin it reads, and our files
  extend the Zope files, so no other change is needed.
- Python-specific pins go in `[versions:python39]`, `[versions:python310]`
  etc. in `versions.cfg`. Each of these sections applies to exactly **one**
  Python version, and overrides `[versions]` in the same file. So a pin that
  should apply to 3.9 and 3.10 needs to be in both sections.
- `release/constraints.txt` is **generated**: one flat list of all effective
  pins (ours and Zope's, from `ecosystem.cfg`), with `python_version`
  markers where the pins differ per Python. Never edit it by hand. It is
  not always in sync with the buildout files: the release manager syncs it
  when preparing a Plone release. Regenerate it with:

  ```bash
  uvx tox -q -p auto -c release/tox.ini \
      -e constraints39,constraints310,constraints311,constraints312,constraints313,constraints
  ```

  This needs `python3.9` up to `python3.13` on the `PATH`, and takes a few
  seconds. It runs buildout's own config parsing for each Python
  (`release/create-constraints.py`) and combines the results
  (`release/combine-constraints.py`). Plain `tox -c release/tox.ini` also
  runs the `gather` env, which copies files to `release/dist/` for the
  release; that is not needed here (but harmless: it is ignored by git).

### Running the audit

Use `uvx pip-audit`. Don't install it into the virtualenv. Put temporary
files in a scratch directory, not in the repo.

First regenerate `release/constraints.txt` (see above), so it matches the
buildout files. If that gives a diff before you changed anything, tell the
user: the file was out of sync. Then:

```bash
uvx --python 3.13 pip-audit -r release/constraints.txt --no-deps --disable-pip
uvx --python 3.13 pip-audit -r requirements.txt --no-deps --disable-pip
```

Environment markers are evaluated for the Python that runs pip-audit, so
run both again with `uvx --python 3.9 ...` and `uvx --python 3.10 ...` for
the pins that only apply there.

Some installed packages aren't pinned anywhere. Buildout reports them as
"Versions had to be automatically picked" at the end of `bin/buildout`, and
plone.versioncheck shows them with state `X`. When you find such a package,
consider pinning it in `versions.cfg` or `versions-extra.cfg`.

### Before changing a pin

- Prefer the latest release over the lowest fixed version, unless there's a
  reason not to.
- Check `requires_python` on PyPI against the oldest supported Python (3.9).
  If the fix needs a newer Python, pin the fixed version in `[versions]` and
  keep the old pin explicitly in the sections for the older Pythons (see the
  Pillow pins: 13.0.0 in `[versions]`, 12.3.0 for 3.10, 11.3.0 for 3.9).
  This also goes for **new** pins, e.g. a new dependency: on Plone 6.2,
  platformdirs 4.14.4 was added for zc.buildout 6, but needs Python 3.11+,
  and broke buildout on Python 3.10 in CI.
- "Dependency not found on PyPI" from pip-audit usually means the pinned
  version doesn't exist (a typo). Check the release list on PyPI.
- For a new major version (e.g. zc.buildout), read the changelog and check
  `requires_dist` for new dependencies that need a pin.
- Zope pins for packages that aren't even installed (e.g. filelock, msgpack)
  are still worth overriding when the user asks.

### Verifying

1. Regenerate `release/constraints.txt` (see above) and check that its diff
   only contains the intended changes, with the right `python_version`
   markers. Commit the regenerated file together with the pin changes.
2. Re-run the audit on `release/constraints.txt` and `requirements.txt`, for
   Python 3.9, 3.10 and 3.13.
3. Check that every pinned version can be installed on each supported
   Python. For `release/constraints.txt` and `requirements.txt`:
   `uv pip compile --quiet --no-deps --python-version 3.9.25 --python-platform linux <file> -o $TMP/out.txt`
   (and again for 3.10 up to 3.13). This fails on any pin whose
   `requires_python` excludes that Python. Leave out Windows-only lines
   (`pywin32`), they don't resolve on Linux. Use `--python-version 3.9.25`
   instead of `3.9`: cryptography excludes Python 3.9.0 and 3.9.1.
   Known failures on Python 3.9, which you can leave out of the check,
   because these packages are never installed on Python 3.9:
   - legacy-cgi 2.6.2 needs Python 3.10+. It is only installed on Python
     3.13, where the `cgi` module was removed from the standard library.
   - feedparser-sgmllib 2.1.0 needs Python 3.10+. It is only a dependency of
     feedparser 6.0.13+. On Python 3.9 we pin feedparser 6.0.12, which uses
     sgmllib3k instead.
   This check also applies to `versions-ecosystem.cfg`, which has its own
   `[versions:python39]` section (e.g. collective.z3cform.datagridfield).
   Those pins are only tested on Python 3.10 in CI
   (`.github/workflows/ecosystem.yml`), so this check is the only one for 3.9.
4. Only when the user asks: run `bin/buildout` (with Python 3.9 and a newer
   Python) and check for "Versions had to be automatically picked" at the
   end. Otherwise leave this to CI (`.github/workflows/run-buildout.yml`
   tests Python 3.9 up to 3.13).

## Checking pins for bugfix releases

"Bugfix release" means a newer final release with the same major.minor as the
pin: 5.0.1 → 5.0.3, not 5.1.0. For two-part versions like `7.4`, look for
`7.4.x`. Ignore pre-releases, dev releases and fully yanked releases.
Report minor and major updates to the user, but don't bump them unless asked.

For CalVer packages (first version component is a year, e.g. certifi
`2026.10.19`, tzdata `2026.3`, trove-classifiers `2026.6.1.19`, rpds-py
`2026.6.3`), "bugfix" means nothing: look for the latest final release
instead. (plone.versioncheck reports these as `Major`, `Minor` or `Bugfix`
updates: take the newest.) Leave out releases whose first component is not a
year (e.g. rpds-py `0.30.0`, from before it switched to CalVer). On this
branch rpds-py is still pinned to `0.22.3`: report the CalVer releases to the
user, but don't switch to them unless asked.
For CalVer packages it is fine to override Zope pins (e.g. certifi, pytz):
mostly these are data packages (certificates, time zones, classifiers) where
newer is simply better.

### Finding updates with plone.versioncheck

Use [plone.versioncheck](https://pypi.org/project/plone.versioncheck/), the
same tool as the weekly `.github/workflows/versioncheck.yml`. There's no need
to use `bin/versioncheck`: run the latest release with uvx.

```bash
PYTHONWARNINGS=ignore uvx --from plone.versioncheck versioncheck \
    -p -n -r -m -o $TMP/versioncheck.json ecosystem.cfg
```

- Use `ecosystem.cfg`: it extends `core.cfg` (with `versions.cfg` and
  `versions-extra.cfg`) plus `versions-ecosystem.cfg`, so all our pins are
  checked. `buildout.cfg` leaves out the ecosystem pins.
- `-p` checks PyPI, `-n` only shows packages with updates, `-r` adds
  "required by", `-m -o` writes JSON. Progress goes to stderr.
- Per package, the JSON has a list of `versions`. The entry with state `A`
  (active) or `O` (orphaned: pinned, but not installed) is the current pin,
  and its `description` is the cfg file that pins it. So you can tell our pins
  (`versions*.cfg` here) from Zope's (remote URLs). Entries with state `U`
  (final) or `P` (pre-release) are updates, with `description` `Major`,
  `Minor` or `Bugfix` (or `...pre`). `I` entries are pins in other files that
  the active one overrides.
- It follows the buildout `extends` chain, including Zope's cfg files, and
  shows `[versionannotations]`.
- States `X` (unpinned) and `O` come from `.plone.versioncheck.tracked.json`,
  which only buildout writes. The uvx run reads it, but doesn't update it,
  so these states describe the last buildout run.

### What plone.versioncheck misses

Check these by hand, with a few requests to
`https://pypi.org/pypi/<name>/json`:

- **Python-specific sections.** It only reads `[versions]`, not
  `[versions:python39]` etc. Pins that only exist there, or differ there
  (currently backports.tarfile, docutils, pip, Pillow and RestrictedPython in
  `versions.cfg`, and docutils in the Zope `versions.cfg`), are missing,
  reported as unpinned, or compared against the `[versions]` pin instead.
  `release/constraints.txt` (regenerated) shows all of them, with markers.
- **Fourth version component.** It only compares major.minor.bugfix, so it
  doesn't report e.g. types-PyYAML `6.0.12.10` → `6.0.12.20261103`. Check
  pins with four components by hand.
- **`requires_python`.** It doesn't check whether an update supports the
  oldest Python we support (3.9). If the newest release needs a newer
  Python, look for the newest release that still supports 3.9, and see
  "Before changing a pin" above.
- **Yanked releases.** It reports yanked releases as updates (e.g. smmap
  6.0.0). Check that a candidate has at least one file that isn't
  yanked.
- **Security.** Use pip-audit for that (see above).

### Before bumping

- Check that the new version still supports Python 3.9. If it doesn't, keep
  the old pin for the older Pythons in their `[versions:pythonXY]` sections.
- Pins in a `[versions:pythonXY]` section: check that the new version still
  supports that Python.
- Check `requires_dist` of the new version for new dependencies that need a
  pin, even for bugfix releases. Example: feedparser 6.0.13 replaced
  `sgmllib3k` with `feedparser-sgmllib`, and buildout then warned that it had
  to pick a version for it. Unpinned dependencies also show up as "Versions
  had to be automatically picked" at the end of `bin/buildout`.
- Read the comments and `[versionannotations]` next to a pin. They may give a
  reason to hold it back. Check that the reason still holds (e.g. with
  `requires_dist` of the package mentioned). Remove comments that no longer
  apply.
- A newer bugfix release isn't necessarily safer. Example: filelock 3.32.7 has
  more open CVEs than 3.32.2. When a pin was chosen for security reasons,
  run pip-audit on the candidate version first.
- Keep the Zope pins the same: don't override them for bugfix releases.
  Overriding Zope pins is only for security fixes, and for CalVer packages
  (see above).
- This includes Zope pins that apply to only one Python version (the
  `[versions:python39]` section of the Zope `versions.cfg`). Report the newer
  Zope bugfix releases to the user instead; they're for Zope to make.
- If a package isn't pinned by Zope and its pin is the same for all Python
  versions after the bump, remove the pins from the `[versions:pythonXY]`
  sections and keep a single pin in `[versions]`.

Commit bugfix bumps separately from security fixes.
