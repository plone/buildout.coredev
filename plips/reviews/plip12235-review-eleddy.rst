PLIP 12235: Unified Batch Implementation
========================================
Ticket: https://dev.plone.org/plone/ticket/12235

Review by Elizabeth Leddy (elizabeth.leddy@gmail.com, eleddy on irc)
The PLIP was reviewed on Mac OSX using python 2.6.5 and Google Chrome

Review Steps
------------
 - Reviewed code at https://github.com/tomgross/plone.batching and commented inline there
 - Reviewed code at https://github.com/tomgross/Products.CMFPlone/commit/84bdce6682fe408a8c3e41a826e0d44337f4ce6e
 - Reviewed cose at https://github.com/tomgross/plone.app.content
 - Ran sphinx documentation and reviewed 
 - Tested search and batching with search

Notes and Oberservations
------------------------
 - Code is really nice and clean. Good test coverage. Big ups for net removeal of code.
 
Little Bugs
-----------
 - In the search UI, if I search for something that returns exactly 10 items, the [1] is 
   displayed with no next or previous. In this case I don't think it should show anything.
 - There is no formatting for the currently selected page. I don't know if this is 
   because of this plip or not. At minimum, let's add some classes to the current page 
   so that it can be styled in the future. Currently it renders in a blank span. I suspect
   this was not intended.

Must Have Changes
-----------------
 - Currently documentation is very sparse. The sphinx docs are nice but basically not useful and
   and the doctest is not good reading. An updated page in collective docs on how to actually use 
   the batching interface would make me feel great about integrating this plip.
 - There is one XXX in the code which should be addressed or moved 
 - On a default install in plone, the error log has lots of deprecation warnings. These should be 
   handled by default with this plip. For example when searching the following line occurs 
   at least 20 times in my log::
   
   string>:1: DeprecationWarning: Using len() for getting the actual pagesize is deprecated. Use the `pagesize` attribute instead.


Conclusion
----------
I'm +1 after human readable developer documentation is added to collective docs and some html
markup for the batch template. Last but not least, a default plone install shouldn't be 
throwing deprecation errors. 
