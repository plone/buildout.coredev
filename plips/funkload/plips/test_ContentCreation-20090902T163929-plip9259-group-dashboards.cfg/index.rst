======================
FunkLoad_ bench report
======================


:date: 2009-09-02 16:39:29
:abstract: Content creation load test scenario
           Bench result of ``Contentcreation.test_ContentCreation``: 
           Content creation load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 16:39:29
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

* 166 tests, 18 error(s)
* 1000 pages, 18 error(s)
* 1472 requests, 18 error(s)


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.100      12      12   0.00%
       2   0.225      27      27   0.00%
       3   0.292      35      35   0.00%
       5   0.392      48      47   2.08%
      10   0.225      44      27  38.64%
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
       1   0.608   2.000      73      73   0.00%   0.010   0.490  15.875   0.010   0.093   0.699   0.915
       2   1.358   4.000     163     163   0.00%   0.009   0.329   2.714   0.010   0.100   0.825   1.086
       3   1.833   6.000     220     220   0.00%   0.009   0.454   5.537   0.010   0.111   1.095   1.976
       5   2.375   6.000     286     285   0.35%   0.009   0.877   8.125   0.025   0.298   2.423   3.676
      10   2.008   8.000     258     241   6.59%   0.013   2.636  14.604   0.297   2.079   5.961   7.835
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.908   4.000     109     109   0.00%   0.008   0.328  15.875   0.010   0.102   0.450   0.576
       2   2.042   5.000     245     245   0.00%   0.008   0.219   2.473   0.010   0.114   0.475   0.638
       3   2.758   6.000     331     331   0.00%   0.008   0.302   5.291   0.010   0.197   0.582   1.092
       5   3.567   8.000     428     427   0.23%   0.008   0.602   7.771   0.020   0.266   1.341   2.369
      10   2.992  10.000     359     342   4.74%   0.013   2.488  14.720   0.308   1.754   4.953  11.171
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 003 post: /coreloadtests/Members/adwutlzfj/folder-8/portal_factory/Document/document.2009-09-02.0810038557/edit took **2.174s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 002 post: /coreloadtests/Members/gxvrkjzcb/portal_factory/Folder/folder.2009-09-02.0803138262/edit took **1.610s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 003 redirect: /coreloadtests/Members/adwutlzfj/folder-8/bradus-pachys-ad-tetra-officinalis took **0.389s**
  ``
* In page 002 redirect: /coreloadtests/Members/gxvrkjzcb/folder-10/ took **0.374s**
  ``
* In page 001 post: /coreloadtests/login_form took **0.327s**
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
           1      13      13   0.00%   0.090   1.312  15.875   0.090   0.100   0.117  15.875
           2      27      27   0.00%   0.089   0.141   0.912   0.090   0.101   0.181   0.251
           3      35      35   0.00%   0.070   0.162   0.584   0.091   0.105   0.315   0.579
           5      47      47   0.00%   0.089   0.327   1.102   0.100   0.275   0.697   0.768
          10      45      45   0.00%   0.339   1.482   4.953   0.428   1.238   2.653   3.754
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/gxvrkjzcb/createObject?type_name=Folder

     .. image:: request_001.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      12      12   0.00%   0.010   0.019   0.093   0.010   0.010   0.020   0.093
           2      27      27   0.00%   0.009   0.042   0.335   0.009   0.010   0.172   0.206
           3      37      37   0.00%   0.009   0.073   0.510   0.010   0.020   0.197   0.368
           5      48      48   0.00%   0.009   0.118   0.512   0.017   0.069   0.290   0.416
          10      48      48   0.00%   0.014   1.082   5.075   0.069   0.770   2.414   3.428
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/gxvrkjzcb/portal_factory/Folder/folder.2009-09-02.6828669277/edit

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      12      12   0.00%   0.294   0.416   1.187   0.300   0.326   0.576   1.187
           2      28      28   0.00%   0.294   0.508   2.473   0.297   0.329   1.015   1.565
           3      37      37   0.00%   0.300   0.598   2.220   0.313   0.415   1.080   1.939
           5      49      48   2.04%   0.312   1.610   7.771   0.346   1.018   4.492   5.292
          10      50      48   4.00%   0.463   4.119  12.293   1.308   2.881  10.138  12.008
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/gxvrkjzcb/folder-9/

     .. image:: request_002.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      12      12   0.00%   0.219   0.278   0.688   0.228   0.247   0.261   0.688
           2      28      28   0.00%   0.231   0.266   0.577   0.233   0.248   0.292   0.326
           3      37      37   0.00%   0.230   0.340   1.125   0.238   0.266   0.542   0.687
           5      48      48   0.00%   0.241   0.374   1.146   0.252   0.339   0.510   0.651
          10      47      47   0.00%   0.289   1.936   4.706   0.479   1.967   3.354   3.560
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/gxvrkjzcb/folder-9/createObject?type_name=Document

     .. image:: request_002.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      12      12   0.00%   0.010   0.014   0.020   0.010   0.011   0.020   0.020
           2      27      27   0.00%   0.009   0.013   0.025   0.010   0.010   0.021   0.021
           3      37      37   0.00%   0.009   0.052   0.387   0.010   0.014   0.170   0.314
           5      48      48   0.00%   0.009   0.096   0.664   0.010   0.033   0.382   0.429
          10      46      46   0.00%   0.013   1.495   3.477   0.145   1.578   3.057   3.186
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/gxvrkjzcb/folder-9/portal_factory/Document/document.2009-09-02.6845014220/edit

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      12      12   0.00%   0.437   0.487   0.702   0.440   0.450   0.583   0.702
           2      27      27   0.00%   0.402   0.630   2.179   0.447   0.476   0.855   1.102
           3      37      37   0.00%   0.437   1.045   5.291   0.453   0.545   2.256   2.434
           5      47      47   0.00%   0.490   2.174   7.738   0.529   1.373   5.788   6.220
          10      42      27  35.71%   1.826   6.906  14.720   2.480   3.821  13.493  13.597
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/gxvrkjzcb/folder-9/stoma-officinalis-aquam-tetra-notos

     .. image:: request_003.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      12      12   0.00%   0.202   0.247   0.455   0.206   0.214   0.367   0.455
           2      27      27   0.00%   0.205   0.245   0.567   0.210   0.226   0.296   0.331
           3      37      37   0.00%   0.197   0.282   0.665   0.214   0.241   0.463   0.589
           5      47      47   0.00%   0.211   0.389   1.241   0.224   0.341   0.702   0.737
          10      27      27   0.00%   0.239   1.636   4.737   0.811   1.574   2.627   2.848
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      12      12   0.00%   0.008   0.013   0.041   0.008   0.009   0.022   0.041
           2      27      27   0.00%   0.008   0.028   0.261   0.008   0.009   0.059   0.146
           3      37      37   0.00%   0.008   0.036   0.481   0.008   0.009   0.089   0.127
           5      47      47   0.00%   0.008   0.083   0.483   0.008   0.036   0.248   0.263
          10      27      27   0.00%   0.059   1.585   3.569   0.165   1.509   2.862   2.867
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_004.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      12      12   0.00%   0.062   0.084   0.131   0.071   0.081   0.102   0.131
           2      27      27   0.00%   0.062   0.087   0.240   0.070   0.082   0.098   0.133
           3      37      37   0.00%   0.062   0.123   1.092   0.072   0.084   0.136   0.278
           5      47      47   0.00%   0.063   0.227   0.773   0.075   0.152   0.515   0.725
          10      27      27   0.00%   0.097   1.174   3.463   0.129   0.959   2.442   3.208
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 8 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in Connection.py, line 594: See the server error log for details
* 10 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
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