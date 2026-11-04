# Notes for AI agents

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
  the old one (see the filelock pins).
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
3. Check the mxdev result without touching the real environment: copy
   `mx.ini`, `requirements-test.txt` and all `constraints*.txt` files to a scratch
   directory, remove the `mx*.ini` includes from the copied `mx.ini`, and run
   `.venv/bin/mxdev -n -c mx.ini` there. In `constraints-mxdev.txt`, the
   overridden Zope pins must show up as `# ... -> mxdev disabled (override)`,
   with exactly one active line per package/marker.
4. For marker-specific pins, run a pip dry run per Python version against that
   `constraints-mxdev.txt`:
   `pip install --dry-run --report - <pkg> -c constraints-mxdev.txt`
   in a throwaway `uv venv --python 3.10 --seed` (and a newer Python).

Don't install anything into `.venv` or commit unless asked. When asked to
commit, do it on a new branch.
