PLIP 12908: Improved Syndication
================================

Framework team review by David Glick
2012-07-16

Review steps:
-------------

- Read code changes.
- Run tests.
- Confirm TTW that the feeds and control panel are available and
- functioning.

Notes:
------

- Seems to work well TTW.
- The code for obtaining the enclosed file only handles Archetypes content.
- The @@download view for Archetypes content should perhaps go in Products.Archetypes.
- BaseFeedData's link property still needs to check the appropriate setting
- I'm -1 on enabling feeds for all folders by default. Especially since the folder adapter doesn't apply a limit to the number of items returned, it could have negative performance implications when robots crawl the site. +1 for enabling it by default on collections though, since that's more often desired.
- Should we remove the settings relating to update frequency? I've never really understand what these are for.
- When linking collections on the home page, we should use the title of the collection in the feed title, not just the feed type.
- Various trivial matters and wording changes noted in github comments.
- Needs migration of settings to annotations
- Needs tests
- There are a bunch of test failures with bin/alltests but I don't think they're related to this PLIP. We really need to clean up the tests for 4.3.
- Needs documentation:
  1. (for users) what feeds are provided by default and what the settings are
  2. (for developers) how to customize feeds
  3. (for developers) how to update existing customized feeds

Overview:
---------

This implementation does a good job of both adding commonly needed
functionality to Plone the product and increasing the customizability of
Plone the platform, while adding a minimum of additional code and cleaning
up some old cruft. Good work! However, I'd say it's only about 70-80% done.
The lack of migration, tests and documentation in particular feel like
blockers. Once those are addressed I would be +1 for merging.
