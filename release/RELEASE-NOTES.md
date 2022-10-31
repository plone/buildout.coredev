# Release notes for Plone 5.2.10

Released: Monday October 31, 2022.

## Python compatibility

This release supports Python 2.7, 3.7, and 3.8.

**Python 3.6 is no longer supported.**
See the [community announcement](https://community.plone.org/t/plone-5-2-drops-python-3-6-support/15706).
Note that both Python 2.7 and 3.6 have reached end of life.
This means the wider Python community no longer supports it.
For example, the default WSGI server used by Plone, which is `waitress`, has a security problem that is only solved on Python 3.7 and higher.  If you use `waitress` on earlier Python versions, you are vulnerable.

Python 3.7 will reach end of life in June 2023.
See https://devguide.python.org/versions/ for the canonical information.
It will get harder to test and support Plone on unsupported Python versions.

Especially Python 2.7 should only be used as a temporary stepping stone before you migrate your Plone site to Python 3.

## Highlights

Interesting changes since 5.2.9:

* `Products.PluggableAuthService`: Set the Cookie Auth Helper cookies with `SameSite` set to `Lax` by default and allow admins to change the setting as well as the secure flag from the Properties tab in the ZMI.
* i18ndude: Add boolean `--no-line-numbers` option to `rebuild-pot`.  Use this to prevent including line numbers in pot files.
* diazo: Remove dependency on `future` package.
