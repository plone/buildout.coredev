.. -*- coding: utf-8 -*-

=================================
Managing Issues and Pull Requests
=================================

Introduction
============

We are using the Github issue trackers of the repositories at `github.com/plone/* <https://github.com/plone>`_
Here our issues for all Plone core repositories are handled.

Pull Requests are issue-like at Github.
They share the set of labels and milestones.

New issues should be created in `Products.CMFPlone <https://github.com/plone/Products.CMFPlone>`_.
If the submitter is sure the issue belongs to a specific package, the issue can be created there too.


Labels explained
================

Main Labels
-----------

We have a well defined set of labels for all Plone core packages and some related packages.
We tried to find a label system that is not too complex but covers several use cases.

01 type: bug
    something does not work
02 type
    regression missing stuff from former version
03 type: feature (plip)
    really new stuff or major change
04 type: enhancement
    makes existing code better
05 type: question
    discussing

11 prio: blocker
    need to be fixed immediatly
12 prio: high
    High Priority
13 prio: normal
    Normal priority
14 prio: low
    Low priority

21 status: confirmed
    issue was read and got confirmed
22 status: in-progress
    somebody works on that issue
23 status: testing
    pull request specific, a PR test or similar is running, waiting for results
24 status: ready
    pull request specific, tests are passing, merge me asap
25 status: deferred
    work on issue or pull request is scheduled for future

31: needs: help
    anybody lease help with this issue
32: needs: review
    this issue needs review, mostly PRs
33: needs: docs
    documentation is needed
34: needs: tests
    this issue implies missing tests
35: needs: rebase
    pull request specific, needs a git rebase
36: needs: cla
    submitter has not signed the contributor lienses agreement

41 lvl: easy
    beginner skills needed
42 lvl: moderate
    fair plone insight needed
43 lvl: complex
    for wizards

.. figure:: /_static/githublabels.png
   :align: center
   :alt: Github labels with its color codes explained


Special Labels
--------------

One can define arbitary labels using the scheme: "99 tag: short custom text"

We have a bunch of custom tags already around, and this makes sense.
They get their own namespace and can be labled free after the prefix


Anatomy of a Label
------------------

number-prefix
    We need this to have a sanely sorted list of the issues at Github.
    The widgets are sorting them alphabetically.
    Otherwise selecting and viewing them is a large headache.

group-prefix
    It makes things more clear to prefix, similar to a namespace

color
    while the main types should be easily to differenciate,
    the other groups are each one color, eventually using a gradient

open/closed
    This is handled by Github already and does not some extra label!

Issue vs. Pull Request
    Dont make a difference here, Github does it already. A PR is usally a 01-04.

State vs. Status
    For the non-native-english folks: http://english.stackexchange.com/questions/12958/status-vs-state


How to get this on all issue trackers
-------------------------------------

There is already a script `plone.github <https://github.com/plone/plone.github>`_ that takes care of it.
Also migration from old labels to new labels happens automatically.
For new repositories the script just need to be re-run.
Github-API FTW!
