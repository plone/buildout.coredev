======================
FunkLoad_ bench report
======================


:date: 2009-09-02 13:22:17
:abstract: Content creation load test scenario
           Bench result of ``Contentcreation.test_ContentCreation``: 
           Content creation load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 13:22:17
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

* 163 tests, 25 error(s)
* 992 pages, 25 error(s)
* 1444 requests, 25 error(s)


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.108      13      13   0.00%
       2   0.217      26      26   0.00%
       3   0.267      32      32   0.00%
       5   0.325      43      39   9.30%
      10   0.233      49      28  42.86%
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
       1   0.692   2.000      83      83   0.00%   0.009   0.262   1.675   0.010   0.188   0.566   0.611
       2   1.342   4.000     161     161   0.00%   0.009   0.289   1.644   0.010   0.191   0.664   0.793
       3   1.667   3.000     200     200   0.00%   0.009   0.464   4.126   0.011   0.140   1.140   2.018
       5   2.150   6.000     262     258   1.53%   0.009   0.979  10.726   0.021   0.269   3.026   5.001
      10   2.208   8.000     286     265   7.34%   0.011   2.238  16.759   0.327   1.831   4.640   6.194
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   1.033   4.000     124     124   0.00%   0.007   0.175   1.675   0.009   0.191   0.350   0.396
       2   2.008   5.000     241     241   0.00%   0.008   0.193   1.442   0.010   0.197   0.428   0.466
       3   2.492   6.000     299     299   0.00%   0.007   0.310   3.576   0.010   0.205   0.719   1.096
       5   3.217   9.000     386     382   1.04%   0.008   0.768  10.597   0.020   0.271   1.779   4.526
      10   3.283   9.000     394     373   5.33%   0.011   2.253  15.123   0.351   1.507   3.548  10.590
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 003 post: /coreloadtests/Members/mzfyiuqgwl/folder/portal_factory/Document/document.2009-09-02.2347607011/edit took **3.556s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 002 post: /coreloadtests/Members/yzvftbedr/portal_factory/Folder/folder.2009-09-02.2364180506/edit took **1.566s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 002 redirect: /coreloadtests/Members/yzvftbedr/folder-1/ took **0.392s**
  ``
* In page 003 redirect: /coreloadtests/Members/mzfyiuqgwl/folder/brevis-variegatus-indicus-oeos-di took **0.383s**
  ``
* In page 001 post: /coreloadtests/login_form took **0.335s**
  `Post /coreloadtests/login_form`

Page detail stats
-----------------


PAGE 001: Post /coreloadtests/login_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/login_form

     .. image:: request_001.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.186   0.298   1.675   0.188   0.191   0.201   1.675
           2      26      26   0.00%   0.086   0.214   0.504   0.095   0.197   0.419   0.423
           3      32      32   0.00%   0.067   0.324   2.018   0.086   0.205   0.684   1.580
           5      42      42   0.00%   0.066   0.335   1.321   0.087   0.244   0.607   0.919
          10      51      51   0.00%   0.189   1.526   7.658   0.470   1.353   2.344   2.928
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/yobhqaeflg/createObject?type_name=Folder

     .. image:: request_001.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.009   0.016   0.085   0.009   0.010   0.020   0.085
           2      28      28   0.00%   0.009   0.025   0.156   0.010   0.020   0.056   0.059
           3      35      35   0.00%   0.009   0.028   0.140   0.009   0.019   0.070   0.110
           5      47      47   0.00%   0.009   0.085   1.162   0.009   0.028   0.196   0.211
          10      54      54   0.00%   0.011   0.984   2.615   0.047   0.937   2.061   2.264
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/yobhqaeflg/portal_factory/Folder/folder.2009-09-02.8553654850/edit

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.249   0.282   0.640   0.250   0.255   0.259   0.640
           2      27      27   0.00%   0.229   0.340   1.189   0.257   0.276   0.496   0.632
           3      35      35   0.00%   0.268   0.610   2.299   0.278   0.326   1.854   2.290
           5      45      45   0.00%   0.278   1.566   6.111   0.300   0.921   4.745   5.654
          10      54      51   5.56%   0.691   3.020  11.163   1.080   2.114   8.413  10.289
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/yobhqaeflg/folder/

     .. image:: request_002.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.216   0.276   0.911   0.216   0.231   0.237   0.911
           2      27      27   0.00%   0.217   0.267   0.577   0.218   0.234   0.374   0.446
           3      35      35   0.00%   0.199   0.281   0.523   0.224   0.243   0.492   0.515
           5      45      45   0.00%   0.219   0.392   1.156   0.243   0.332   0.541   0.658
          10      51      51   0.00%   0.229   1.520   4.127   0.492   1.424   2.697   3.009
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/yobhqaeflg/folder/createObject?type_name=Document

     .. image:: request_002.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.009   0.011   0.020   0.009   0.010   0.010   0.020
           2      27      27   0.00%   0.009   0.033   0.215   0.009   0.020   0.050   0.160
           3      34      34   0.00%   0.009   0.044   0.228   0.009   0.021   0.130   0.161
           5      45      45   0.00%   0.010   0.151   0.855   0.011   0.061   0.418   0.703
          10      51      51   0.00%   0.028   1.264   3.475   0.296   1.252   2.286   2.515
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/yobhqaeflg/folder/portal_factory/Document/document.2009-09-02.8565275193/edit

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.324   0.363   0.424   0.327   0.356   0.410   0.424
           2      27      27   0.00%   0.397   0.489   1.442   0.406   0.437   0.617   0.706
           3      32      32   0.00%   0.431   1.092   3.576   0.452   0.825   2.475   2.587
           5      44      40   9.09%   0.494   3.556  10.597   0.910   2.449   8.650  10.406
          10      48      30  37.50%   1.215   7.081  15.123   1.898   5.756  13.086  13.926
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/yobhqaeflg/folder/maculatus-lipsem-pedis-bradus-cyanos

     .. image:: request_003.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.170   0.209   0.348   0.180   0.200   0.221   0.348
           2      27      27   0.00%   0.181   0.243   0.583   0.188   0.204   0.362   0.508
           3      32      32   0.00%   0.181   0.272   0.584   0.198   0.219   0.467   0.550
           5      40      40   0.00%   0.193   0.383   1.058   0.209   0.315   0.735   0.955
          10      29      29   0.00%   0.352   1.671   4.420   0.559   1.522   3.176   3.231
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.007   0.014   0.041   0.008   0.009   0.026   0.041
           2      26      26   0.00%   0.008   0.021   0.184   0.008   0.008   0.041   0.057
           3      32      32   0.00%   0.007   0.028   0.198   0.008   0.009   0.053   0.185
           5      39      39   0.00%   0.008   0.101   0.593   0.008   0.041   0.353   0.504
          10      28      28   0.00%   0.018   1.361   3.478   0.070   1.443   2.553   2.593
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_004.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.057   0.093   0.283   0.058   0.077   0.123   0.283
           2      26      26   0.00%   0.057   0.102   0.384   0.058   0.073   0.238   0.368
           3      32      32   0.00%   0.059   0.131   0.401   0.073   0.083   0.290   0.399
           5      39      39   0.00%   0.059   0.202   0.600   0.069   0.130   0.450   0.455
          10      28      28   0.00%   0.095   0.898   2.691   0.149   0.760   1.882   2.382
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 9 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in Connection.py, line 594: See the server error log for details
* 16 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
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