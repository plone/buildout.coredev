.. -*- coding: utf-8 -*-

==================
git best practices
==================
Collection of best practices that would help the overall community to work with git more efficiently.

Basics
======
Some introductory definitions and concepts.

Working model
-------------
In ``git``
(as well as all modern `DVCS <http://en.wikipedia.org/wiki/Distributed_revision_control>`_),
distributing changes to others is a two steps process
(contrary to traditional VCS like ``svn``).

This way what on svn is a single ``svn ci`` in git is two commands:
``git commit`` and ``git push``.

This may seem to be a drawback,
but instead it's a feature.

**You are working locally until you decide to push your changes.**

Not a single commit anymore,
but a series of them,
meaning that all those fears,
concerns,
doubts are taken away!

You can freely fix/change/remove/rework/update/... your commits afterwards.

Just push your changes whenever you are sure they are what you,
and others,
expect them to be.

Concepts
--------
In git there are:

commits
   A patch made out of changes (additions, removals) on files tracked by git.

branches
   Series of commits that have a name.

tags
   A name attached to a single commit.

``HEAD``
   A pointer that always tells you where you are
   (extremely useful when doing some operations).

The index
  A temporal staging storage with changes on files that are pending to be added to a commit.
  If your git output is colored,
  green filenames are those in the index.

Working tree
  Your current modified files.
  This is the only place where you can loose your changes.
  If your git output is colored,
  red filenames are those in the working tree.

Stash
  Temporal storage for changes,
  again,
  extremely useful in some scenarios,
  see further below for examples.

Branches
--------
Another great feature of DVCS is cheap branching,
i.e. branching in git is effortless and really useful.
As it's no longer too much effort to branch,
there is no need to always work on the master branch.
A developer can branch easily for each fix/feature.

Branches allow you to tinker with your changes while keeping the master branch clean.

Not only that,
it also allows you to keep modifying your changes until you and your peers are fine with them.

Further documentation:
`Introduction to branching <http://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell>`_.


Commands
--------
Some of the most useful/common commands
(note that most of them have switches that enhance/*completely twist* their functionality):

Just append ``--help`` on all of them to get their full definitions and options,
i.e. ``git add --help``.

clone
   Download a repository from a given remote URL.

add
   Add the given files to the index.

   .. note::
      **pro tip**: once a file is add via ``git add`` your changes will never be lost!
      As long as you don't remove the ``.git`` folder,
      even if you remove the file you just added,
      the changes you made before doing ``git add`` are still there ready to be recovered at any time!

status
   Get an overview of the repository status.

   If there are files on the index,
   or files not tracked by git,
   or the status of your local branch with regards to the remote,
   etc.

diff
   See the current changes made to the files already tracked by git.

   .. note::
      Fear not, if you used ``git add SOME_FILE`` and then ``git diff`` doesn't output anything you haven't lost your changes!

      Just try ``git diff --cached``.
      Now you know how to see the working tree changes (``git diff``) and index changes (``git diff --cached``).

commit
   Create/record changes to the repository
   (locally only, nothing is sent over the wire).

push
   Send your changes,
   either commits or a complete new branch,
   to the configured remote repository.

show
   Display the given commit(s) details.

log
   Shows the repository history.
   Sorted by date (last commit at the top),
   and like all other commands,
   extremely versatile with all its switches.

   See further below for an example of a powerful combination of switches.

branch
   Create a branch.

fetch
   Download changes from the remote repository.

   **Without** changing the current ``HEAD`` (see rebase and pull commands).

pull
   Fetch and integrate changes from remote repository.

   Internally that means to do a ``git fetch`` plus either ``git merge`` or ``git rebase``.

   .. note::
      Used careless most probably adds extra superfluous commits.
      See further down.

merge
   Join two,
   or more,
   branches together.

rebase
   Forward-port your current local commits (or branch) to be based on top of another commit.

   An image is worth 1000 words: http://git-scm.com/docs/git-rebase

checkout
   Change to the given branch or get the given file to its latest committed version.

   .. note::
      If git is criticized for being complex,
      this command is one of the main sources of complains.

      You can compare it with ``svn switch`` if you happen to know it.

      Fear not though,
      two main use cases are:
      change branches and reset a file to its last committed version.
      Still,
      the syntax for both cases is really simple.

cherry-pick
   Apply a commit(s) to the current working branch.

stash
   Use a temporal storage to save/restore current changes still not meant to be used on a commit.

   .. note::
      Seems a bit not so useful on a first look,
      but it is indeed.

      Think about this scenario:
      you are working on your branch coding away.
      All of the sudden you notice a small fix that should be done directly on master.
      Thanks to ``git stash`` you can save your changes quickly and safely,
      move to master branch,
      do the quick fix,
      commit and push it,
      move back to your branch and ``git stash pop`` to recover your changes and continue hacking away.

reflog
   When things go bad you will **love** this command.

   It effectively shows you a histogram of what happened on the repository,
   allowing you to rollback you repository to a previous stage.

   Extremely useful once a bad interactive rebase has happened.

