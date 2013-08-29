==================================================
Review of PLIP12267 / Folder Contents Improvements
==================================================

Reviewer: Johannes Raggam, thet, johannes@raggam.co.at

Plattform: Ubuntu 13.04, Python 2.7.3, Firefox 23.0

wildcard.foldercontents git rev: 3d319175eef87c0c7e11759e9d073941b763f129 


Just for reference: there is collective.folderorder, and it's ordering behavior
is quite good (if you choose the "prepend" mode. the other one has some side
effects): https://github.com/collective/collective.folderorder


I use the term "table sorting" and "persistent sorting". With "table sorting" i
mean the sorting of the displayed folder_contents table without changing the
persistent order of the objects in that folder. With "persistent sorting" I
mean changing the order of the objects in a folder persistently.

Steps
=====

- Installed wildcard.foldercontents in Plone 4.3 environment.


General Remarks
===============

- The project seems to depend on the Bootstrap framework, which is problematic
  for inclusion in Plone core. If Plone5 isn't going to depend on this, this
  dependency has to be removed and the styles reimplemented in another way. But
  IIRC Bootstrap is used for plone.app.toolbar, so at least if folder_contents
  isn't shown in the main user area but only in the toolbar, this dependency
  might be ok.

- The table sorting via the top right dropdown isn't what someone might expect.
  Better would be a sorting by clicking on the table headers including a
  possibility to do a reverse sort.

- The outer right sorting column in the table offers a dropdown menu with two
  entries. The dropdowns don't close when clicking on another sorting dropdown
  menu. I'd prefer icons to the dropdown menu anyways. It would be nice to have
  "move to top" and "move to bottom" options too. But anyways, this second
  sorting column is reduntant to the first sorting column, which offers
  drag/drop sorting. Thus, I suggest to remove the second one completly and
  merge missing functionality into the first one.

- The "persistent sort" dropdown at the bottom is missing a way to keep the
  manually set folderorder (the 'getObjPositionInParent') and do a reverse sort
  on it.

- There is no way to automatically sort newly added entries - they are always
  appended at the bottom, regardless which persistent sorting method was chosen
  before.
  I suggest, that a foldersorting is also applied for newly added entries and
  to add two new options: "Manual ordering, add new entries to the top" and
  "Manual ordering, add new entries to the bottom". So, if I had chosen
  "Manual, new to top", new entries are placed on the top of the folder while
  I'm still able to reorder something manually. This is quite useful for News
  Sites, where editors want to have new postings on top but want to be able to
  change the placement of some news items depending on their importance. Also,
  when I had chosen "Sort by title", a newly added content item should be put
  to the right place automatically.
  This suggestion assumes that a subscription adapter is registered which
  listens to some object-added-events and do a full folder resorting every time
  a item is added. This can be quite performance-costly for folders with a huge
  amount of items.
  Anyway, this one is a often requested key-feature, so we have to implement it
  in one or another way.
  Also see the package collective.folderorder mentioned above.

- In general, the tablesorting vs persistent sorting dualism is a bit
  confusing. We should rethink the UI to make it clearer, what the differences
  are. Or maybe we should only offer persistent sorting?


Feature ideas
=============

- Filter field: A field to filter the contents after a given keyword. The
  filter should be applied to values in the columns of the table. So, if I
  search for user "foo" all items created by "foo" should be displayed.

- Tablesorting and filtering should be done by AJAX calls instead of
  full page reloads.



Code Reviewing Remarks
======================

To be done.


Summary
=======

To be done.

