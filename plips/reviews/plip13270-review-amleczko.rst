PLIP 13270: Move presentation mode out of core
==============================================

PLIP ticket: https://dev.plone.org/ticket/13270

Review by Andrew Mleczko (amleczko@redturtle.it, amleczko on irc)

The PLIP was reviewed on Ubuntu 12.04 using python 2.7.3 and Chromium 23.0,
Firefox 18.0.


Review steps
------------


- Ran buildout using the plip13270-presentation-mode.cfg file.

- Ran tests for plone.app.layout, Products.ATContentTypes,
  plone.app.s5slideshow

- Reviewed the code changes in plone.app.layout, Products.ATContentTypes,
  plone.app.s5slideshow


Notes and observations
----------------------


- the tests (plone.app.layout and Products.ATContentTypes) failed due to 
  errors in plone.app.collection and Products.CMFPlone. I have used following
  patches to proceed with tests::

        diff --git a/plone/app/collection/collection.py b/plone/app/collection/collection.py
        index 1b45716..5584c2d 100644
        --- a/plone/app/collection/collection.py
        +++ b/plone/app/collection/collection.py
        @@ -87,7 +87,6 @@ CollectionSchema = document.ATDocumentSchema.copy() + atapi.Schema((
        ))

        CollectionSchema.moveField('query', after='description')
       -CollectionSchema['presentation'].widget.visible = False
        CollectionSchema['tableContents'].widget.visible = False

  and::

        diff --git a/Products/CMFPlone/setuphandlers.py b/Products/CMFPlone/setuphandlers.py
        index 6c8f08d..0fdc77e 100644
        --- a/Products/CMFPlone/setuphandlers.py
        +++ b/Products/CMFPlone/setuphandlers.py
        @@ -217,9 +217,6 @@ def setupPortalContent(p):
                fp.setLanguage(language)
                fp.setText(front_text, mimetype='text/html')

        -       # Show off presentation mode
        -       fp.setPresentation(True)
        -
                # Mark as fully created
                fp.unmarkCreationFlag()

- after patching the packages (plone.app.collection and Products.ATContentTypes)
  all tests passed.

- code changes are minor, basically removing any presence of presentation mode.

- I didn't noticed any problems using the plone.app.s5slideshow - it's quite
  simple and straightforward.

- minor observations:

  - the plone.app.s5slideshow package has several not used imports that could be cleaned up.

  - declare_namespace is not needed in plone/app/s5slideshow/__init__.py


Conclusion
----------

I would be +1 on this PLIS. However first dependency packages need to be fixed,
(by removing completely the presentation mode) or a proper version pin
(plone.app.colllection >= 2.0) need to be added.
