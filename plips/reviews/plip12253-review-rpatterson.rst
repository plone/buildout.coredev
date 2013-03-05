PLIP 12253: Use z3c.form instead of zope.formlib in plone.app.users
===================================================================

PLIP ticket: https://dev.plone.org/ticket/12253

Review by Ross Patterson (me@rpatterson.net, zenwryly@irc.freenode.net)

The PLIP was reviewed on Ubuntu 12.04 using python 2.7.3 and Chromium 27.


Review steps
------------

- Set up the buildout using the PLIP's config::

  $ bin/buildout -c plips/plip12253-users-z3cform.cfg -N

- Ran tests for the PLIP's auto-checkout packages::

  $ bin/test -s plone.app.users -s collective.examples.userdata

- Reviewed the code changes the PLIP's auto-checkout packages

- Reviewed the control panels in chrome


Notes and observations
----------------------

- The plips/plip12253-users-z3cform.cfg config uses a different branch
  than mentioned in the Trac PLIP

- Two doctests fail::

  Running tests at level 1
  Running Products.PloneTestCase.layer.PloneSite tests:
    Set up Testing.ZopeTestCase.layer.ZopeLite in 3.408 seconds.
    Set up Products.PloneTestCase.layer.ZCML in 8.345 seconds.
    Set up Products.PloneTestCase.layer.PloneSite in 6.504 seconds.
    Running:
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/flexible_user_registration.txt (1.972 s)
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/forms_navigationroot.txt (0.825 s)
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/registration_forms.txt (2.851 s)
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/userdata.txt (0.814 s)
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/userdata_prefs_user_details.txt (0.698 s)
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/personal_preferences.txt (0.612 s)
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/personal_preferences_prefs_user_details.txt (0.871 s)
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/password.txt (0.810 s)
   test_new_user_as_site_administrator (plone.app.users.tests.test_new_user.TestNewUser) (0.165 s)
    Ran 9 tests with 0 failures and 0 errors in 9.619 seconds.
  Running collective.examples.userdata.testing.EnhancedUserdata:Functional tests:
    Tear down Products.PloneTestCase.layer.PloneSite in 0.103 seconds.
    Tear down Products.PloneTestCase.layer.ZCML in 0.007 seconds.
    Tear down Testing.ZopeTestCase.layer.ZopeLite in 0.000 seconds.
    Set up plone.testing.zca.LayerCleanup in 0.001 seconds.
    Set up plone.testing.z2.Startup in 0.066 seconds.
    Set up plone.app.testing.layers.PloneFixture in 3.611 seconds.
    Set up collective.examples.userdata.testing.EnhancedUserdata in 0.295 seconds.
    Set up collective.examples.userdata.testing.EnhancedUserdata:Functional in 0.000 seconds.
    Running:
   test_personalinformationextended (collective.examples.userdata.tests.test_userdataschema.TestUserDataSchema) (0.462 s)
   test_registerextended (collective.examples.userdata.tests.test_userdataschema.TestUserDataSchema) (0.147 s)
   test_setvalues (collective.examples.userdata.tests.test_userdataschema.TestUserDataSchema) (0.188 s)
   test_validateaccept (collective.examples.userdata.tests.test_userdataschema.TestUserDataSchema) (0.345 s)
    Ran 4 tests with 0 failures and 0 errors in 1.151 seconds.
  Running plone.app.users.tests.base.Z3CFormLayer tests:
    Tear down collective.examples.userdata.testing.EnhancedUserdata:Functional in 0.000 seconds.
    Tear down collective.examples.userdata.testing.EnhancedUserdata in 0.002 seconds.
    Tear down plone.app.testing.layers.PloneFixture in 0.041 seconds.
    Tear down plone.testing.z2.Startup in 0.003 seconds.
    Tear down plone.testing.zca.LayerCleanup in 0.003 seconds.
    Set up Testing.ZopeTestCase.layer.ZopeLite in 0.006 seconds.
    Set up Products.PloneTestCase.layer.ZCML in 1.919 seconds.
    Set up Products.PloneTestCase.layer.PloneSite in 2.634 seconds.
    Set up plone.app.users.tests.base.Z3CFormLayer in 0.010 seconds.
    Running:
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/flexible_user_registration.txt (1.541 s)
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/forms_navigationroot.txt (0.792 s)
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/registration_forms.txt (2.807 s)
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/userdata.txt (0.932 s)
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/userdata_prefs_user_details.txt (0.873 s)
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/personal_preferences.txt (0.890 s)
  
  
  Failure in test /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/personal_preferences.txt
  Traceback (most recent call last):
    File "/usr/lib/python2.7/unittest/case.py", line 327, in run
      testMethod()
    File "/usr/lib/python2.7/doctest.py", line 2201, in runTest
      raise self.failureException(self.format_failure(new.getvalue()))
  AssertionError: Failed doctest test for personal_preferences.txt
    File "/opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/personal_preferences.txt", line 0
  
  ----------------------------------------------------------------------
  File "/opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/personal_preferences.txt", line 40, in personal_preferences.txt
  Failed example:
      isEmptyMarker(self.browser.getControl('Wysiwyg editor').value)
  Expected:
      True
  Got:
      False
  ----------------------------------------------------------------------
  File "/opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/personal_preferences.txt", line 44, in personal_preferences.txt
  Failed example:
      isEmptyMarker(self.browser.getControl('Language', index=0).value)
  Expected:
      True
  Got:
      False
  
  
  
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/personal_preferences_prefs_user_details.txt (1.114 s)
  
  
  Failure in test /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/personal_preferences_prefs_user_details.txt
  Traceback (most recent call last):
    File "/usr/lib/python2.7/unittest/case.py", line 327, in run
      testMethod()
    File "/usr/lib/python2.7/doctest.py", line 2201, in runTest
      raise self.failureException(self.format_failure(new.getvalue()))
  AssertionError: Failed doctest test for personal_preferences_prefs_user_details.txt
    File "/opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/personal_preferences_prefs_user_details.txt", line 0
  
  ----------------------------------------------------------------------
  File "/opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/personal_preferences_prefs_user_details.txt", line 31, in personal_preferences_prefs_user_details.txt
  Failed example:
      isEmptyMarker(self.browser.getControl('Wysiwyg editor').value)
  Expected:
      True
  Got:
      False
  ----------------------------------------------------------------------
  File "/opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/personal_preferences_prefs_user_details.txt", line 35, in personal_preferences_prefs_user_details.txt
  Failed example:
      isEmptyMarker(self.browser.getControl('Language', index=0).value)
  Expected:
      True
  Got:
      False
  ----------------------------------------------------------------------
  File "/opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/personal_preferences_prefs_user_details.txt", line 100, in personal_preferences_prefs_user_details.txt
  Failed example:
      isEmptyMarker(self.browser.getControl('Wysiwyg editor').value)
  Expected:
      True
  Got:
      False
  ----------------------------------------------------------------------
  File "/opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/personal_preferences_prefs_user_details.txt", line 104, in personal_preferences_prefs_user_details.txt
  Failed example:
      isEmptyMarker(self.browser.getControl('Language', index=0).value)
  Expected:
      True
  Got:
      False
  
  
  
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/password.txt (0.863 s)
   /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/../vocabularies.py (0.017 s)
    Ran 9 tests with 2 failures and 0 errors in 9.994 seconds.
  Running zope.testing.testrunner.layer.UnitTests tests:
    Tear down plone.app.users.tests.base.Z3CFormLayer in 0.105 seconds.
    Tear down Products.PloneTestCase.layer.PloneSite in 0.001 seconds.
    Tear down Products.PloneTestCase.layer.ZCML in 0.006 seconds.
    Tear down Testing.ZopeTestCase.layer.ZopeLite in 0.000 seconds.
    Set up zope.testing.testrunner.layer.UnitTests in 0.000 seconds.
    Running:
   test__init__no_userid (plone.app.users.tests.test_account.TestAccountPanelSchemaAdapter) (0.000 s)
   test__init__userid_in_request_form_for_manager (plone.app.users.tests.test_account.TestAccountPanelSchemaAdapter) (0.000 s)
   test__init__userid_in_request_form_for_non_manager (plone.app.users.tests.test_account.TestAccountPanelSchemaAdapter) (0.000 s)
    Ran 3 tests with 0 failures and 0 errors in 0.001 seconds.
  Tearing down left over layers:
    Tear down zope.testing.testrunner.layer.UnitTests in 0.000 seconds.
  
  Tests with failures:
     /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/personal_preferences.txt
     /opt/src/buildout.coredev/src/plone.app.users/plone/app/users/tests/personal_preferences_prefs_user_details.txt
  Total: 25 tests, 2 failures, 0 errors in 48.885 seconds.

- "Wysiwyg editor" and "Language" fields show "Missing:" for newly added user::

    <div data-fieldname="form.wysiwyg_editor" class="field z3cformInlineValidation kssattr-fieldname-form.wysiwyg_editor" id="formfield-form-wysiwyg_editor">
    
        <label for="form-wysiwyg_editor" class="horizontal">
            Wysiwyg editor
    
            
            
            <span class="formHelp">Wysiwyg editor to use.</span>
        </label>
    
        <div class="fieldErrorBox"></div>
    
        
    <select id="form-wysiwyg_editor" name="form.wysiwyg_editor:list" class="select-widget choice-field" size="1">
    <option id="form-wysiwyg_editor-novalue" value="--NOVALUE--">Use site default</option>
    <option id="form-wysiwyg_editor-0" value="None">None</option>
    <option id="form-wysiwyg_editor-1" value="TinyMCE">TinyMCE</option>
    <option id="form-wysiwyg_editor-missing-0" value="" selected="selected">Missing: </option>
    </select>
    <input name="form.wysiwyg_editor-empty-marker" type="hidden" value="1" originalvalue="1">
    
    
    </div>

- No CHANGES.TXT entries

- Why are the formlib forms still in place?

- Some forms are neither z3c.form nor formlib:

  * @@usergroup-userprefs
  * @@usergroup-usermembership
  * @@usergroup-groupdetails
  * @@usergroup-groupmembership
  * @@manage-group-portlets
  * @@manage-group-dashboard
  * @@usergroup-groupprefs

  Fine for this PLIP, but worth noting

- The "Member Registration" field doesn't seem to have any effect on
  the @@register form


Conclusion
----------

I'm -1 for merge as is but think this is within striking distance.

Firstly, I think we have enough old code in Plone without adding more
as we make changes.  If we're going to merge this PLIP then we should
*replace* formlib with z3c.form, not keep both alongside each other.

Also important, the "Member Registration" has to work before merging.

Other than that, if the tests passed, I'd be +1 for merging.
