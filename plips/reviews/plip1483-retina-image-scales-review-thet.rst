PLIP 1483: Retina Image Scales
==============================

PLIP ticket: https://github.com/plone/Products.CMFPlone/issues/1483

Review by Johannes Raggam (thetetet@gmail.com)

The PLIP was reviewed using Python 2.7.13 and Firefox 52.0 (64 bit) and Chrome 57.0 (64-bit) on Fedora 25.

The hardware is an Lenovo Yoga 910 13k with a 4k Display.


Review steps
------------

- Ran buildout::

    $ virtualenv .
    $ ./bin/pip install -r requirements.txt

  Running it with ``./bin/buildout -c ./plips/plip-1483-retina-image-scales.cfg`` didn't work, so I used a config like this::

    [buildout]
    extends =
        buildout.cfg
        https://raw.githubusercontent.com/bluedynamics/buildout-base/master/etc/dev.cfg
    versions = versions
    auto-checkout +=
        plone.app.contenttypes
        plone.app.portlets
        plone.app.upgrade
        plone.namedfile
        Products.CMFPlone

    [sources]
    plone.app.contenttypes = git ${remotes:plone}/plone.app.contenttypes.git pushurl=${remotes:plone_push}/plone.app.contenttypes.git branch=plip-1483-retina-image-scales
    plone.app.portlets = git ${remotes:plone}/plone.app.portlets.git pushurl=${remotes:plone_push}/plone.app.portlets.git branch=plip-1483-retina-image-scales
    plone.app.upgrade = git ${remotes:plone}/plone.app.upgrade.git pushurl=${remotes:plone_push}/plone.app.upgrade.git branch=plip-1483-retina-image-scales
    plone.namedfile = git ${remotes:plone}/plone.namedfile.git pushurl=${remotes:plone_push}/plone.namedfile.git branch=plip-1483-retina-image-scales
    Products.CMFPlone = git ${remotes:plone}/Products.CMFPlone.git pushurl=${remotes:plone_push}/Products.CMFPlone.git branch=plip-1483-retina-image-scales

  And ran it with::

    $ ./buildout -c local.cfg

- Started instance ``./bin/instance fg``

- Created Plone site.

- Opened: http://localhost:8080/Plone/@@imaging-controlpanel

- Changed setting "Retina mode" to "Enabled (2x, 3x)".

- Created News Item with an image.

- Created Image.

- Looked at rendered output + source.

- Did the same with "Retine mode" disabled.


Here are some Screenshots from my test:
https://github.com/plone/Products.CMFPlone/issues/1483#issuecomment-287036988

And here a comparison of the images and their file sizes:
https://github.com/plone/Products.CMFPlone/issues/1483#issuecomment-287040770


Notes and observations
----------------------

Manual testing
++++++++++++++

This PLIP with enabled retina mode gives a significant improvement for images on Hi-Res screens than without the Retina mode enabled.

The images do look amazing and a lot crispier than normal.

The individual scaled images (2x, 3x) have a rather bad quality, though.
This is due to their low quality setting, which ensures small download sizes.
I'm absolutly OK with the qulity settings, but the resulting images are not suitable for downloading.
This is not an issue, as there should a separate download link anyways, if images should be offered for downloading.


Code Review
+++++++++++

- The templates look a bit more concise, which is good.

- Instead of having to get the portal object, getting the ``@@image_scale`` view on it and calling the tag method via a python-TALES expression, passing some parameters, I would prefer it like so:

  - A view (``@@imagetag``) with a custom traverser, which can be called like so: ``@@imagetag/FIELDNAME/SCALENAME/optionalExtraCSSClass``.
  - This would be easier to remember and shorter to write.
  - Although I'm not sure if this is worth the effort - this doesn't easily allow customization of ``alt`` and ``title`` attributes.
  - This presumes, that a view can also be called on a brain object (not sure, if brains can be traversed like normal objects and views called like that?).
  - Caching the results for brains on portal root should still be possible.

- The already merged mockup changes are already compiled into the plone bundle and available on CMFPlone master.

- The ``plone.js`` bundle resource is a pragmatic place to put the ``@@image-controlpanel`` JavaScript code into, and it works.
  But IMO this is not the right place.
  Rather than there, this should go wether into a plain JavaScript file and added to the ``plone-legacy`` bundle resources or made a pattern out of it.

- TinyMCE Image handling is missing - but this is not a blocker and can be delivered later.


Documentation
+++++++++++++

- Developer documentation can be found in this PR: https://github.com/plone/documentation/pull/781

- User documentation is missing. There should at least a small chapter about how to activate and configure retina images.


Conclusion
----------

- This is a very nice feature addition for Plone with a relative low risk.
- I think, some testing in the wild would be good before merging it into core.
- I recommend to merge it into core for Plone 5.2.
- For that we need a Plone 5.1 release and create branches 5.1 branches of packages where this code is merged into.

- The bundle issue should be discussed and resolved.
- Some user-documentation should be written.
- The idea with the ``@@imagetag`` view traverser should be discussed.


