================
PLIP 10886 Notes
================

# This PLIP is ready for review - nearly, now only completion of this doc is
# missiing.

PLIP ticket: https://dev.plone.org/ticket/10886


Documentation
-------------

Overview
--------



Known issues, weak points and TODOs
-----------------------------------

- One test fails only from time to time (Microsecond comparison bug):
    plone.app.event.tests.test_atevent.PAEventATTest.test_edit, 156-162
  Maybe we should remove the (partial) support of Microseconds alltogether and
  use a more tolerant comparing function for datetime objects (which doesn't
  compare below a minute or so).

- We use Products.DateRecurringIndex instead of
  Products.PluginIndexes.DateIndex. While it is as efficient for indexing
  events without recurrence, events with recurrence take longer. For each
  occurrence of an recurring event, an index entry is created. We have an
  hardcoded recurrence limit set to 1000 in plone.event.recurrence, which
  should be enough for most use cases.

- For recurring events, plone.app.event.recurrence.RecurrenceSupport.occurrence
  goes through the whole recurrence set, which is inefficient. This is, because
  we turn the recurrence set, which is a generator to a list, waking all
  objects too. While this is mainly a problem with recurring events, it should
  be changed and optimized.
  One (soft) reason, which hinders us from doing so, is that in the event view,
  we want to show only the first 7 occurrences and the very last occurrence in.
  To get the last occurrence, we have to walk through the whole recurrence set.
  This problem is documented here:
  https://github.com/plone/plone.app.event/issues/60

- We use plone.event.IEventAccessor as a wrapper for Archetypes and Dexterity
  based events. While this is a good and flexible concept, the EventAccessor
  implementations always adapt the object itself. We use this whereever
  possible, even when accessing a brain's information would be sufficient. This
  might be inefficient too, in some cases.


Dependencies
------------


Tests and test coverage
-----------------------


Further ideas
-------------

