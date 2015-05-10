PLIP 13350: Edit Member Schema TTW
==================================

PLIP ticket: https://dev.plone.org/ticket/13350

Review by Franco Pellegrini (frapell@gmail.com, frapell@irc.freenode.net)

The PLIP was reviewed on Kubuntu 15.04 using python 2.7.8 (https://github.com/collective/buildout.python) and Chromium 41.0.2272.76.

May 10, 2015


Review steps
------------

- Set up the buildout using the PLIP's config::

  $ ./bin/buildout -c plips/plip13350-edit-member-schema-ttw.cfg

- Ran tests for the PLIP's auto-checkout packages::

  $ bin/test -s plone.app.users
  $ bin/test -s Products.CMFPlone

- Reviewed code

- Manual testing TTW


Notes and observations
----------------------

Automated testing
+++++++++++++++++

- Tests for plone.app.users pass 100%

- Products.CMFPlone has some failing tests, with a bunch of them related to login (e.g. Products/CMFPlone/tests/emaillogin.txt) :

    Total: 1398 tests, 3 failures, 5 errors and 6 skipped

- I think we need to add more robot tests for different scenarios:

  * Test fields order are honored everywhere (user registration, user preferences, etc)
    
     Test added
    
  * Test different settings for each field, are being applied everywhere, such as a field being required, minimum and maximum lengths, restricting it from the "Where should this field be shown" option, etc...
    
     Test added
        
  * Test every field type (string, integer, bool, image, etc). Data should be saved and retrieved without loosing its original type.
    
     No tests for this
        
  * Test importing/exporting fields, making sure to test all possible types
    
     A test was added, but it doesn't cover different attributes are set, types of fields, etc...

- I think the code coverage by automated testing should be increased. These are the numbers I got, filtering only files affected by this work:

    +-------------+------------+---------------------------------------------+
    | cov% (prev) | cov% (cur) | module                                      |
    +=============+============+=============================================+
    |     86%     |     86%    | plone.app.users.browser.personalpreferences |
    +-------------+------------+---------------------------------------------+
    |     87%     |     87%    | plone.app.users.browser.register            |
    +-------------+------------+---------------------------------------------+
    |     74%     |     74%    | plone.app.users.browser.schemaeditor        |
    +-------------+------------+---------------------------------------------+
    |    100%     |    100%    | plone.app.users.browser.schemaprovider      |
    +-------------+------------+---------------------------------------------+
    |     77%     |     95%    | plone.app.users.browser.userdatapanel       |
    +-------------+------------+---------------------------------------------+
    |     94%     |    100%    | plone.app.users.field_extender              |
    +-------------+------------+---------------------------------------------+
    |     90%     |     89%    | plone.app.users.schema                      |
    +-------------+------------+---------------------------------------------+
    |     56%     |    100%    | plone.app.users.setuphandlers               |
    +-------------+------------+---------------------------------------------+
    |     44%     |     60%    | plone.app.users.upgrades                    |
    +-------------+------------+---------------------------------------------+
    |     98%     |     97%    | plone.app.users.vocabularies                |
    +-------------+------------+---------------------------------------------+

    cov% (prev) Means the code coverage found on previous review (Feb 8)

    cov% (cur) Means the code coverage found on current review


Manual testing
++++++++++++++

The following notes are regarding the @@member-fields view
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| (previous review) https://www.dropbox.com/s/v2zokbn2nud7rbe/members-ttw1.png?dl=0
| (current review) https://www.dropbox.com/s/gc8q8qtos4pftf5/member-fields.png?dl=0

- This template should use the same master template used by @@usergroup-userprefs, @@usergroup-groupprefs and @@usergroup-controlpanel, so when clicking the tab, still feels like a tab and that you are still in the members configuration area.

    This was not fixed

- In the upper right, there's an "Add new fieldset" button that opens a form to add a new fieldset, but after clicking "add", nothing new was added, if we don't intend to add fieldsets to the member profile, I think we should remove this button from here.

    This is fixed

- Style is broken (You can see in the screenshot), but I think is more of a schemaeditor problem, rather than in the scope of this PLIP.

    This is fixed

- Should we have default fields (fullname and email in this case) be "blurred" as are the ones for a content type when fields are included from a behavior?

    Question still unanswered

- When adding a field, what's the difference between "Full Name" type of field and "Text line (string)" ?

    I only see "Text line (string)" listed as field type, so I will assume this to be fixed now.

- When trying to change field order, I get "plone.protect Error checking for CSRF." in my terminal, and the new order is not saved.

    I now get another Javascript error, but still cannot change order: "Uncaught TypeError: Cannot read property 'dataTransfer' of null"

- There's a "Save Defaults" button at the bottom that when clicked it submits the form and fails with required fields (such as email). It also redirects to @@member-fields/@@edit, which doesn't make much sense. If random stuff is entered into the required fields so the validation passes, when the page is rendered again it shows the non-default fields (the ones added from the @@member-fields view) as blurred, and the default ones not. I think the form action should omit the /@@edit part, and also that the "Save Defaults" should be removed.

    This item was not addressed

- When deleting a field, I get "WARNING plone.protect error parsing dom, failure to add csrf token to response for url" in my terminal, however, the field is removed fine.

    This item was not addressed


The following notes are general functionality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The "Where should this field be shown" setting seems to not be working fine.

    This is fixed

- "required" and min-max lengths seem to be working fine in both registration and edit profile templates.

- Trying to add a "Relation List" type of field, throws a "TypeError: type not serializable RelationList"

    "Relation List" no longer present in type list, I consider this item fixed

- Trying to add a "Relation Choice" type of field, throws a "TypeError: type not serializable RelationChoice"

    "Relation Choice" no longer present in type list, I consider this item fixed

- Trying to add a "File Upload" type of field, throws a "TypeError: type not serializable NamedBlobFile"

    "File Upload" no longer present in type list, I consider this item fixed

- There are some types missmatches from the field type added TTW and the property added in "portal_memberdata". For instance, "Text line(String)" is created as text instead of string.

    This has been fixed

- If we add an "Image" type of field, it will get added to the list of fields for the member profile, but an error message gets printed in the terminal "INFO plone.app.users.browser.schemaeditor Unsupported field: portrait2 (NamedBlobImage)"

    This has been fixed

- When trying to remove the image field (I have called it 'portrait2'), we get an error and the field does not get removed: "ValueError: The property portrait2 does not exist"

    This has been fixed

- Since the image field is available, it shows up when editing your profile. Uploading an image here goes nowhere and does not get saved nor showed once the form gets submitted.

    This has been fixed

- When adding a "Date" type of field, and running the GenericSetup export, an exception is raised: http://pastie.org/private/mxxp7ocqwadndcory56zw (A fix for this is to provide a default initial value, such as login_time and last_login_time)

    This has been fixed

- Exporting the TTW definition seems to work fine to a "userschema.xml" file

- There is a typo for the import step, which is called "Export member custom TTW schema", however the import seems to work fine.

    This item was not addressed

- Running the provided Upgrade Step, raises an exception: http://pastie.org/private/8znjzpo25t7kicrm71ofa

    This has been fixed

- The import step is not ran automatically when creating a site from scratch, so by default, the member schema will only have "fullname" and "email".

    This item was not addressed
    
- Missing documentation on how to export/import member schema. Is the current documented IFormExtender method still relevant?

    This item was not addressed

- NEW: Added a "Choice" field called 'vocab', and chose the "plone.app.vocabularies.Weekdays" vocabulary. However, when trying to create a new user, I got: http://pastie.org/private/oqshlj6ox1ouvl8kon4bq

- NEW: I see a "Date" field type, which allows you to add a field for just date. There is no way to make that a "Datetime". Is there a reason for this?

- NEW: When adding a "Rich Text" field, the TinyMCE editor is not visible for anonymous when registering.

- NEW: I added an Image field, and when registering/editing profile, it worked just fine and image was stored. However, when I added a second "Image" field, it shows the same content as the previously created one (both fields display the same content, and changing either one, will change the other as well). Do we have a limitation of just 1 Image field? if so, shouldn't the @@member-fields provide some kind of validation when trying to add a second image field? Is there a way around it so we can have as many Image fields as desired for a user profile? (maybe we can add a way to say "use this field as portrait", so we can mark it)

- NEW: When adding a non required "Integer" field, if no data is entered when registering, you get: http://pastie.org/private/cvzrlp1rstnrchaiv8yrq

- NEW: When adding a non required "Float" field, if no data is entered when registering, you get: http://pastie.org/private/zx3ciwlpl6ksoxovpc9g

- NEW: For an "Image" field, the "Remove existing image" when editing your profile doesn't work. "Replace with new image" does work.

Code review
+++++++++++

- We should not group imports nor do relative imports. Also, please order them alphabetically
    
    http://ploneapi.readthedocs.org/en/latest/contribute/conventions.html#about-imports

- Overall it looks clean and readable and no obvious bugs were seen.

- There are some quality errors that we should fix before merging (using flake8):

    | (previous review) http://pastie.org/private/v0ow8527fwjdc6dcn6uhiw
    | (current review) http://pastie.org/private/82fi7yneemyudpgsodbpw


browser/account.py
^^^^^^^^^^^^^^^^^^

| 77:if self.schema[name].__class__.__name__ == 'NamedBlobImage'
| 91:if value.__class__.__name__ == 'NamedBlobImage'
    
    Why not use isinstance instead?
    

browser/schemaeditor.py
^^^^^^^^^^^^^^^^^^^^^^^

257: if field.__class__.__name__ in field_type_mapping

    Why not use isinstance instead?

- Would it make sense to have the ALLOWED_FIELDS coming from the registry or somewhere easy to change without the need to monkey patch?

    
schema.py
^^^^^^^^^

- Why do we need ProtectedTextLine and ProtectedEmail? Can't the "protection" come from an attribute in the schema definition? this way we can also make it possible define additional fields that cannot be edited or removed (Avoid users accidentally removing sensitive fields)


Conclusion
----------

Currently this is not in a state where it can be merged. It is in a far better situation than it was on previous review, however this is a critic Plone functionality, it should be rock solid and thoroughly tested.