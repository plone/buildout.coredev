# Release notes for Plone 5.2-dev

Last updated: Friday April 29, 2022.

## Highlights

Interesting changes since 5.2.7:

* `Zope`: Enhance cookie support. For details, see [issue 1010](https://github.com/zopefoundation/Zope/issues/1010)
  For more changes see https://zope.readthedocs.io/en/4.x/changes.html
* `plone.app.linkintegrity`: Track link integrity of referenced PDFs and other site objects in IFRAME SRC references.
* `plone.outputfilters`: Resolve UIDs in SRC attribute of of SOURCE and IFRAME elements.
* `plone.app.querystring`: Add lazy attribute to vocabularies to prevent fetching any results.
* `plone.schema`: Use indent in json.dumps to make JSON readable in the widget.
