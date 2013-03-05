PLIP 12253: Use z3c.form instead of zope.formlib in plone.app.users
===================================================================

PLIP ticket: https://dev.plone.org/ticket/12253

Review by David Glick (dglick@gmail.com)

The PLIP was reviewed on OS X 10.8 using python 2.7.3.


Review steps
------------

- Set up the buildout using the PLIP's config::

  $ bin/buildout -c plips/plip12253-users-z3cform.cfg

- Ran tests for the PLIP's auto-checkout packages::

  $ bin/test -s plone.app.users -s collective.examples.userdata

- Reviewed the code changes in plone.app.users and collective.examples.userdata

- Tested control panels through the web


Notes and observations
----------------------

- The change does appear to make it easier to customize the forms,
  and it's great that this is covered in the documentation and that
  collective.examples.userdata will be updated to show how.

- I agree with Ross that we should replace the formlib forms entirely
  rather than adding the z3c.form ones as an option. This will help our
  effort to use a standard form library in Plone. The formlib forms
  can always be moved to a separate add-on package if some integrator
  depends on them so extensively that it would be hard to migrate.

- Two test failures

- The raising of errors during validation can be simplified by raising
  WidgetActionExecutionError (see https://dexterity-developer-manual.readthedocs.org/en/latest/schema-driven-forms/customising-form-behaviour/validation.html#validating-in-action-handlers)

- Please run a pep8 linter on the new code and make it compliant.

- The Language and Wysywyg editor fields on the Preferences form aren't
  getting valid defaults.

- Inline validation isn't working for the form fields (probably need
  to adjust something to deal with z3c.form fields with no prefix).


Merge tasks
-----------

- Make sure any fixes that have happened on p.a.users master recently
  are incorporated.
- Merge plone.app.users
- Merge collective.examples.userdata
- Update csrf.txt test in CMFPlone
- Move EmptyPrefixFieldWidgets to plone.z3cform or plone.app.z3cform
- Add collective.examples.userdata to packages tested in coredev
- Add changelog entries
- Add notes to upgrade guide on what integrators need to pay attention to
- Make sure p.a.users' readme is linked to an appropriate place
  in developer.plone.org


Conclusion
----------

This is good work, but I think we should adjust it so that the
package only has the z3c.form-based implementation.  Once that and the
minor issues are addressed, I'll be +1 for including this in 4.4.
