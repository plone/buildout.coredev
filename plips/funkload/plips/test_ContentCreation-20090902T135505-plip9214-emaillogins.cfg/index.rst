======================
FunkLoad_ bench report
======================


:date: 2009-09-02 13:55:05
:abstract: Content creation load test scenario
           Bench result of ``Contentcreation.test_ContentCreation``: 
           Content creation load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 13:55:05
* Test: ``collective.coreloadtests.tests.test_Contentcreation.py Contentcreation.test_ContentCreation``
* Server: http://localhost:8080
* Cycles of concurrent users: [1, 2, 3, 5, 10]
* Cycle duration: 120s
* Sleeptime between request: from 0.0s to 2.0s
* Sleeptime between test case: 1.0s
* Startup delay between thread: 0.2s
* FunkLoad_ version: 1.10.0


Bench content
-------------

The test ``Contentcreation.test_ContentCreation`` contains: 

* 6 page(s)
* 3 redirect(s)
* 0 link(s)
* 0 image(s)
* 0 XML RPC call(s)

The bench contains:

* 170 tests, 24 error(s)
* 1027 pages, 24 error(s)
* 1504 requests, 24 error(s)


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.117      14      14   0.00%
       2   0.217      26      26   0.00%
       3   0.300      36      36   0.00%
       5   0.342      43      41   4.65%
      10   0.242      51      29  43.14%
 ======= ======= ======= ======= =======

Page stats
----------

The number of Successful **Page** Per Second (SPPS) over Concurrent Users (CUs).
Note that an XML RPC call count like a page.

 .. image:: pages_spps.png
 .. image:: pages.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs    SPPS maxSPPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.725   2.000      87      87   0.00%   0.011   0.267   1.749   0.011   0.188   0.575   0.642
       2   1.317   3.000     158     158   0.00%   0.010   0.307   2.901   0.011   0.135   0.693   0.821
       3   1.833   5.000     220     220   0.00%   0.010   0.380   4.113   0.013   0.184   0.909   1.271
       5   2.250   6.000     272     270   0.74%   0.010   0.946   9.804   0.022   0.297   2.723   3.440
      10   2.233   7.000     290     268   7.59%   0.023   2.042  16.102   0.330   1.701   4.848   6.037
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   1.083   3.000     130     130   0.00%   0.009   0.178   1.749   0.011   0.200   0.357   0.389
       2   1.975   5.000     237     237   0.00%   0.009   0.204   2.505   0.010   0.202   0.431   0.457
       3   2.758   6.000     331     331   0.00%   0.009   0.253   3.896   0.011   0.213   0.497   0.741
       5   3.367   8.000     404     402   0.50%   0.008   0.683   9.700   0.021   0.250   1.853   2.778
      10   3.350   8.000     402     380   5.47%   0.023   2.095  15.456   0.330   1.282   3.713   9.335
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 003 post: /coreloadtests/Members/axrgmizsd/folder/portal_factory/Document/document.2009-09-02.1993919299/edit took **2.940s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 002 post: /coreloadtests/Members/jpbqozndu/portal_factory/Folder/folder.2009-09-02.2006209263/edit took **1.268s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 001 post: /coreloadtests/login_form took **0.638s**
  `Post /coreloadtests/login_form`
* In page 003 redirect: /coreloadtests/Members/axrgmizsd/folder/mauro-domesticus-zygos-lipsem-protos took **0.415s**
  ``
* In page 002 redirect: /coreloadtests/Members/jpbqozndu/folder-1/ took **0.328s**
  ``

Page detail stats
-----------------


PAGE 001: Post /coreloadtests/login_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/login_form

     .. image:: request_001.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      15      15   0.00%   0.087   0.293   1.749   0.188   0.194   0.215   1.749
           2      25      25   0.00%   0.085   0.211   0.436   0.087   0.204   0.323   0.353
           3      35      35   0.00%   0.087   0.324   1.509   0.089   0.216   0.580   1.258
           5      43      43   0.00%   0.087   0.638   4.402   0.090   0.283   1.747   2.967
          10      49      49   0.00%   0.209   1.300   8.494   0.253   0.959   2.396   3.277
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/pwhgytmdv/createObject?type_name=Folder

     .. image:: request_001.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      15      15   0.00%   0.011   0.021   0.087   0.011   0.021   0.030   0.087
           2      27      27   0.00%   0.010   0.022   0.077   0.010   0.020   0.060   0.075
           3      36      36   0.00%   0.010   0.031   0.173   0.010   0.020   0.086   0.096
           5      48      48   0.00%   0.010   0.103   1.049   0.011   0.048   0.267   0.290
          10      53      53   0.00%   0.023   0.985   3.620   0.137   0.713   2.248   2.973
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/pwhgytmdv/portal_factory/Folder/folder.2009-09-02.8242978384/edit

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      15      15   0.00%   0.252   0.287   0.624   0.253   0.262   0.287   0.624
           2      27      27   0.00%   0.269   0.335   0.587   0.272   0.286   0.509   0.513
           3      38      38   0.00%   0.269   0.488   1.813   0.278   0.297   1.185   1.214
           5      47      47   0.00%   0.285   1.268   5.905   0.305   0.818   2.636   3.136
          10      56      54   3.57%   0.499   2.519   8.893   0.748   1.928   6.136   6.986
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/pwhgytmdv/folder/

     .. image:: request_002.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      15      15   0.00%   0.217   0.276   0.927   0.219   0.228   0.251   0.927
           2      27      27   0.00%   0.200   0.245   0.425   0.217   0.230   0.314   0.327
           3      38      38   0.00%   0.210   0.283   0.766   0.218   0.241   0.434   0.508
           5      47      47   0.00%   0.221   0.328   0.651   0.236   0.291   0.515   0.604
          10      53      53   0.00%   0.352   1.387   3.200   0.698   1.218   2.196   2.854
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/kcuasdeio/folder/createObject?type_name=Document

     .. image:: request_002.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.011   0.017   0.022   0.011   0.021   0.022   0.022
           2      27      27   0.00%   0.010   0.020   0.092   0.010   0.018   0.030   0.056
           3      38      38   0.00%   0.010   0.032   0.124   0.011   0.022   0.065   0.077
           5      47      47   0.00%   0.010   0.181   1.386   0.018   0.061   0.443   0.812
          10      52      52   0.00%   0.026   1.139   2.557   0.104   1.116   1.999   2.262
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/kcuasdeio/folder/portal_factory/Document/document.2009-09-02.8185934920/edit

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.326   0.368   0.427   0.327   0.368   0.413   0.427
           2      26      26   0.00%   0.397   0.627   2.505   0.412   0.437   1.657   1.808
           3      37      37   0.00%   0.398   0.700   3.896   0.423   0.470   1.027   2.358
           5      45      43   4.44%   0.484   2.940   9.700   0.648   2.009   8.339   9.249
          10      50      30  40.00%   1.120   6.851  15.456   1.466   5.459  12.929  13.718
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/kcuasdeio/folder/tinctorius-via-mono-ortho-deca

     .. image:: request_003.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.201   0.225   0.350   0.203   0.215   0.230   0.350
           2      26      26   0.00%   0.185   0.246   0.475   0.202   0.216   0.396   0.407
           3      37      37   0.00%   0.185   0.233   0.472   0.200   0.217   0.283   0.300
           5      43      43   0.00%   0.195   0.415   1.755   0.225   0.313   0.804   0.871
          10      30      30   0.00%   0.213   1.645   3.411   0.590   1.784   3.213   3.279
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.009   0.015   0.042   0.009   0.010   0.020   0.042
           2      26      26   0.00%   0.009   0.033   0.420   0.009   0.010   0.062   0.099
           3      36      36   0.00%   0.009   0.054   0.427   0.009   0.011   0.182   0.213
           5      42      42   0.00%   0.008   0.067   0.621   0.009   0.027   0.164   0.177
          10      30      30   0.00%   0.026   1.225   3.239   0.279   1.139   2.316   2.980
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_004.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.060   0.092   0.297   0.060   0.080   0.127   0.297
           2      26      26   0.00%   0.060   0.107   0.401   0.061   0.081   0.219   0.272
           3      36      36   0.00%   0.060   0.118   0.375   0.070   0.085   0.300   0.364
           5      42      42   0.00%   0.061   0.168   0.614   0.077   0.130   0.276   0.388
          10      29      29   0.00%   0.101   0.828   2.266   0.123   0.774   1.867   2.043
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 10 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in Connection.py, line 594: See the server error log for details
* 14 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in FileStorage.py, line 514: See the server error log for details

Definitions
-----------

* CUs: Concurrent users or number of concurrent threads executing tests.
* Request: a single GET/POST/redirect/xmlrpc request.
* Page: a request with redirects and ressource links (image, css, js) for an html page.
* STPS: Successful tests per second.
* SPPS: Successful pages per second.
* RPS: Requests per second successful or not.
* maxSPPS: Maximum SPPS during the cycle.
* maxRPS: Maximum RPS during the cycle.
* MIN: Minimum response time for a page or request.
* AVG: Average response time for a page or request.
* MAX: Maximmum response time for a page or request.
* P10: Percentil 10 or response time where 10 percent of pages or requests are delivred.
* MED: Median or Percentil 50, response time where half of pages or requests are delivred.
* P90: Percentil 90 or response time where 90 percent of pages or requests are delivred.
* P95: Percentil 95 or response time where 95 percent of pages or requests are delivred.

Report generated with FunkLoad_ 1.10.0, more information available on the `FunkLoad site <http://funkload.nuxeo.org/#benching>`_.