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
    Something that i supposed to work does not work.
02 type :regression
    Something that used to be available or worked in a former version,
    is not available any more or does not work anymore.
03 type: feature (plip)
    Really new stuff or major change that needs to go through the Plone Improvement Proposal process.
04 type: enhancement
    Makes existing features, code or documentation better.
    Needs to be backward compatible.
05 type: question
    A general question or request for comments to be answered or discussed.

11 prio: blocker
    Need to be solved immediatly.
12 prio: high
    High Priority, needs a solution.
13 prio: normal
    Normal priority.
14 prio: low
    Low priority.

21 status: confirmed
    Issue or pull request was read and got confirmed.
22 status: in-progress
    Somebody works on that issue or pull request.
23 status: testing
    Pull request specific:
    test or similar is running, waiting for results or if failed for a solution.
    Note: `Jenkins pull request testing <http://jenkins.plone.org/job/pull-request-5.0/>`_ does report the state back to Github.
24 status: ready
    Pull request specific:
    Tests are passing, to be merged as soon as possible.
    Look for a reason in the comments why it was not merged already.
25 status: deferred
    Work on issue or pull request is scheduled for future.
    Look for a reason in the comments why it was deferred.

31: needs: help
    Anybody please help with this issue.
    Some issues or pull request need somebody with different skills to get solved.
    Others are new and unresolved or orphaned.
    Some times its an good entry point for newbies.
    Look if the level was set to get a first impression.
32: needs: review
    This issue needs a review, mostly pull requests.
    Often its good if more than one person looks after it and comment the opinion.
33: needs: docs
    Documentation is needed.
    This label is used for general documentation,
    but also to indicate missing change log entries.
    Look for a reason in the comments why exactly.
34: needs: tests
    This issue or pull request implies missing tests.
35: needs: rebase
    Pull request specific:
    needs a git rebase.
    This means the master or version-series branch diverged from the branch to merge.
    Github can no merge automatically into the requested main-line branch.
    The submitter is expected rebase the branch.
36: needs: cla
    Pull request specific:
    Submitter has not signed the `Plone contributor lienses agreement <https://plone.org/foundation/contributors-agreement>`_.
    For legal reasons its not possible to merge.

41 lvl: easy
    Beginner skills needed.
    Perfect to make your hands dirty and start contributing to Plone.
42 lvl: moderate
    Fair plone insight needed.
    If you develop with Plone for some time and know the common bits and pieces, thats kind is for you.
43 lvl: complex
    For wizards. If you know Plone in depth please help with this kind.

Colors codes are used as shown in the image.

.. img:: /_static/githublabels.png
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
    This is handled by Github already and does not need some extra label!

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
