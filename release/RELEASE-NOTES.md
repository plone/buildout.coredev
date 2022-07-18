# Release notes for Plone 5.2.9

Last updated: Monday July 18, 2022.

## Python compatibility

As usual, this release supports Python 2.7, 3.6, 3.7, and 3.8.

But note that both Python 2.7 and 3.6 have reached end of life.
This means the wider Python community no longer supports it.
For example, the default WSGI server used by Plone, which is `waitress`, has a security problem that is only solved on Python 3.7 and higher.  If you use `waitress` on earlier Python versions, you are vulnerable.

Python 3.7 will reach end of life in June 2023.
See https://devguide.python.org/versions/ for the canonical information.
It will get harder to test and support Plone on unsupported Python versions.

Especially Python 2.7 should only be used as a temporary stepping stone before you migrate your Plone site to Python 3.

## Highlights

Interesting changes since 5.2.8:

* `waitress`: Updated to version 2.1.2, which has a bugfix for the previous security fix.
  Version 2.1.1 could cause Plone to crash and restart.  See also remark above on Python compatibility.
* `plone.app.querystring`:
  * Add negation-query operators `string.isNot` and `selection.none`.
  * Make SearchableText work when using `and` and `or` as search items.
* `zodbverify`: Improve debugging output: show all objects that reference an oid.
  See [Philip's blog post](https://www.starzel.de/blog/zodb-debugging)
  and [discussion in pull request](https://github.com/plone/zodbverify/pull/8) for more information.
