# Release notes for Plone 5.2-dev

Last updated: Friday April 29, 2022.

## Highlights

Interesting changes since 5.2.7:

* `Zope`: Enhance cookie support. For details, see [issue 1010](https://github.com/zopefoundation/Zope/issues/1010)
  For more changes see https://zope.readthedocs.io/en/4.x/changes.html
* `waitress` is updated to version 2.1.1 to mitigate a vulnerability in that package. As waitress no longer supports Python versions less than 3.7 it is not advised to run Plone 5.2 on Python 2.7 or 3.6 any longer, even though they are still supported by Plone itself. You get an older `waitress` version then. If you must use an old Python version, please switch to a different WSGI server.  See the [recommendations](https://zope.readthedocs.io/en/latest/operation.html#recommended-wsgi-servers) in the Zope documentation.
* `plone.app.linkintegrity`: Track link integrity of referenced PDFs and other site objects in IFRAME SRC references.
* `plone.outputfilters`: Resolve UIDs in SRC attribute of of SOURCE and IFRAME elements.
* `plone.app.querystring`: Add lazy attribute to vocabularies to prevent fetching any results.
* `plone.schema`: Use indent in json.dumps to make JSON readable in the widget.
