# Notes for AI agents

## General

- Don't install anything into `.venv` or commit unless asked. When asked to
  commit, do it on a new branch.
- Put temporary files and helper scripts in a scratch directory, not in the
  repo.
- After changing pins, run `bin/manage versions2constraints` and do the
  verification steps under "Verifying" below.

## Checking pins for security vulnerabilities

Use this when asked to check installed packages or pins for releases that fix
vulnerabilities, and to update the pins.

### How the version files fit together

- `versions.cfg` is the source of truth. It extends the Zope versions for this
  Plone version (see its `extends` line).
- `constraints.txt` (and `constraints-extra.txt`, `constraints-ecosystem.txt`)
  are **generated**: edit `versions.cfg`, then run `bin/manage versions2constraints`.
  Never edit `constraints.txt` by hand.
- The `# Basics` section of `versions.cfg` (pip, setuptools, wheel,
  zc.buildout, horse-with-no-namespace) must match `requirements.txt`.
- To override a Zope pin, add it to the `# OVERRIDES` section of
  `versions.cfg` **and** to `version-overrides` in `mx.ini`. Without the
  `mx.ini` entry, mxdev keeps both pins and pip fails on the conflict.
- Python-specific pins go in `[versions:python_version > "3.10"]` /
  `[versions:python_version == "3.10"]` in `versions.cfg`, and in `mx.ini` as
  `name==x.y; python_version ...` lines.
- mxdev quirk: `version-overrides` keeps **one line per package name**, and
  that name is case sensitive. If you need two marker-specific overrides for
  the same package, spell the second one differently
  (e.g. `filelock==...` and `FileLock==...`). A single override line also
  disables the Zope pin on **all** Python versions, so pin the other Python
  versions explicitly too.

### Running the audit

Use `uvx pip-audit`. Don't install it into `.venv`. Put temporary files in a
scratch directory, not in the repo.

```bash
# 1. Our own pins (strip the remote -c Zope line):
grep -v '^-c' constraints.txt > $TMP/own.txt
uvx --python 3.14 pip-audit -r $TMP/own.txt --no-deps --disable-pip
uvx --python 3.14 pip-audit -r constraints-extra.txt --no-deps --disable-pip
uvx --python 3.14 pip-audit -r constraints-ecosystem.txt --no-deps --disable-pip
uvx --python 3.14 pip-audit -r requirements.txt --no-deps --disable-pip

# 2. The Zope constraints (URL is on the first line of constraints.txt):
curl -s https://zopefoundation.github.io/Zope/releases/6.2/constraints.txt > $TMP/zope.txt
uvx --python 3.14 pip-audit -r $TMP/zope.txt --no-deps --disable-pip

# 3. Installed packages (skip the source checkouts in src/):
PIPAPI_PYTHON_LOCATION=.venv/bin/python uvx pip-audit --skip-editable
```

Environment markers are evaluated for the Python that runs pip-audit, so use
`uvx --python 3.10 ...` to check the 3.10 pins.

Step 3 mostly repeats steps 1 and 2. It's there because some installed
packages aren't pinned in any constraints file, and only this step checks
them. Examples are tooling like mxmake and cookiecutter and their
dependencies, and grpcio/protobuf (pinned exactly by robotframework-browser).
When it finds such a package, consider pinning it in `versions.cfg`.

### Before changing a pin

- Prefer the latest release over the lowest fixed version, unless there's a
  reason not to.
- Check `requires_python` on PyPI against the oldest supported Python (see the
  `python_version == "3.10"` section). If the fix needs a newer Python, pin the
  fixed version only for the newer Pythons and keep the old pin explicitly for
  the old one (see the filelock pins). This also goes for **new** pins, e.g.
  a new dependency: platformdirs 4.14.4 was added for zc.buildout 6, but
  needs Python 3.11+, and broke buildout on Python 3.10 in CI.
- "Dependency not found on PyPI" from pip-audit usually means the pinned
  version doesn't exist (a typo). Check the release list on PyPI.
- For a new major version (e.g. zc.buildout), read the changelog and check
  `requires_dist` for new dependencies that need a pin.
- Zope pins for packages that aren't even installed (e.g. filelock, msgpack)
  are still worth overriding when the user asks.

### Verifying

1. Run `bin/manage versions2constraints` and check that the `constraints.txt`
   diff only contains the intended changes.
2. Re-run the audit on the new `constraints.txt` and `requirements.txt`.
   Run it for Python 3.10 too, for the pins that only apply there.
3. Check that every pinned version can be installed on the oldest and the
   newest supported Python. For each of `constraints.txt` (without the `-c`
   line), `constraints-extra.txt`, `constraints-ecosystem.txt` and
   `requirements.txt`:
   `uv pip compile --quiet --no-deps --python-version 3.10 --python-platform linux <file> -o $TMP/out.txt`
   (and again with e.g. `--python-version 3.14`). This fails on any pin whose
   `requires_python` excludes that Python. Leave out Windows-only lines
   (`pywin32`), they don't resolve on Linux.
4. Check the mxdev result without touching the real environment: copy
   `mx.ini`, `requirements-test.txt` and all `constraints*.txt` files to a scratch
   directory, remove the `mx*.ini` includes from the copied `mx.ini`, and run
   `.venv/bin/mxdev -n -c mx.ini` there. In `constraints-mxdev.txt`, the
   overridden Zope pins must show up as `# ... -> mxdev disabled (override)`,
   with exactly one active line per package/marker.
5. For marker-specific pins, run a pip dry run per Python version against that
   `constraints-mxdev.txt`:
   `pip install --dry-run --report - <pkg> -c constraints-mxdev.txt`
   in a throwaway `uv venv --python 3.10 --seed` (and a newer Python).

## Checking pins for bugfix releases

"Bugfix release" means a newer final release with the same major.minor as the
pin: 5.0.1 → 5.0.3, not 5.1.0. For two-part versions like `7.4`, look for
`7.4.x`. Ignore pre-releases, dev releases and fully yanked releases.
Report minor and major updates to the user, but don't bump them unless asked.

For CalVer packages (first version component is a year, e.g. certifi
`2026.10.19`, tzdata `2026.3`, trove-classifiers `2026.6.1.19`, rpds-py
`2026.6.3`, horse-with-no-namespace `20260202.0`), "bugfix" means nothing:
look for the latest final release instead. (plone.versioncheck reports these
as `Major`, `Minor` or `Bugfix` updates: take the newest.) Leave out releases whose first
component is not a year (e.g. rpds-py `0.30.0`, from before it switched to
CalVer). Pins in `mx.ini` overrides (e.g. certifi) must be bumped there too.
For CalVer packages it is fine to override Zope pins (e.g. certifi, pytz):
mostly these are data packages (certificates, time zones, classifiers) where
newer is simply better.

### Finding updates with plone.versioncheck

Use [plone.versioncheck](https://pypi.org/project/plone.versioncheck/), the
same tool as the weekly `.github/workflows/versioncheck.yml`. There's no need
to run buildout first to get `bin/versioncheck`: run the latest release with
uvx.

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
  `[versions:python_version > "3.10"]` etc. Pins that only exist there
  (exceptiongroup, pillow, rpds-py, filelock, tomli in `versions-extra.cfg`)
  are missing, reported as unpinned, or compared against the Zope pin
  instead of ours.
- **Fourth version component.** It only compares major.minor.bugfix, so it
  doesn't report e.g. types-PyYAML `6.0.12.10` → `6.0.12.20261103`. Check
  pins with four components by hand.
- **`requires_python`.** It doesn't check whether an update supports the
  oldest Python we support (3.10). If the newest release needs a newer
  Python, look for the newest release that still supports 3.10.
- **Yanked releases.** It reports yanked releases as updates (e.g. smmap
  6.0.0). Check that a candidate has at least one file that isn't
  yanked.
- **Security.** Use pip-audit for that (see above).

### Before bumping

- Pins with a marker for Python 3.10: check that the new version still
  supports 3.10.
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
- This includes Zope pins that apply to only one Python version. Example:
  Zope pins exceptiongroup 1.3.0 on Python 3.10, so bump only our
  `python_version > "3.10"` pin and keep 1.3.0 for 3.10. Don't replace both
  with one unconditional pin: that would override the Zope pin. Report the
  newer Zope bugfix releases to the user instead; they're for Zope to make.
- If the pin of a package isn't pinned by Zope and is the same for all
  Python versions after the bump, replace the per-Python pins with a single
  pin in `[versions]`.

Commit bugfix bumps separately from security fixes.
