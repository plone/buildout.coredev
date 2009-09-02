======================
FunkLoad_ bench report
======================


:date: 2009-09-02 11:49:41
:abstract: Content creation load test scenario
           Bench result of ``Contentcreation.test_ContentCreation``: 
           Content creation load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 11:49:41
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

* 179 tests, 27 error(s)
* 1062 pages, 27 error(s)
* 1550 requests, 27 error(s)


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.108      13      13   0.00%
       2   0.217      26      26   0.00%
       3   0.300      36      36   0.00%
       5   0.383      50      46   8.00%
      10   0.258      54      31  42.59%
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
       1   0.650   3.000      78      78   0.00%   0.010   0.263   1.664   0.018   0.188   0.564   0.688
       2   1.325   3.000     159     159   0.00%   0.009   0.338   2.705   0.010   0.191   0.870   1.265
       3   1.842   4.000     221     221   0.00%   0.009   0.376   3.062   0.010   0.134   0.930   1.273
       5   2.458   7.000     299     295   1.34%   0.009   0.720   6.287   0.021   0.255   2.142   3.425
      10   2.350   8.000     305     282   7.54%   0.010   1.926  13.281   0.303   1.629   4.063   5.447
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.975   4.000     117     117   0.00%   0.008   0.176   1.664   0.010   0.191   0.352   0.391
       2   1.983   5.000     238     238   0.00%   0.008   0.226   2.485   0.009   0.205   0.435   0.773
       3   2.767   7.000     332     332   0.00%   0.007   0.250   2.532   0.010   0.196   0.515   0.739
       5   3.692   8.000     443     439   0.90%   0.008   0.568  10.439   0.021   0.242   1.392   2.614
      10   3.500   9.000     420     397   5.48%   0.010   1.986  15.533   0.364   1.279   3.384   8.792
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 003 post: /coreloadtests/Members/zulcnrmkf/folder-3/portal_factory/Document/document.2009-09-02.6784598284/edit took **2.292s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 002 post: /coreloadtests/Members/axrgmizsd/portal_factory/Folder/folder.2009-09-02.6800241731/edit took **1.071s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 001 post: /coreloadtests/login_form took **0.522s**
  `Post /coreloadtests/login_form`
* In page 002 redirect: /coreloadtests/Members/axrgmizsd/folder-2/ took **0.346s**
  ``
* In page 003 redirect: /coreloadtests/Members/zulcnrmkf/folder-3/biscortborealis-nothos-platy-montanus-officinalis took **0.320s**
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
           1      13      13   0.00%   0.188   0.305   1.664   0.189   0.191   0.200   1.664
           2      26      26   0.00%   0.085   0.207   0.525   0.089   0.201   0.262   0.382
           3      35      35   0.00%   0.084   0.188   0.515   0.086   0.203   0.299   0.389
           5      50      50   0.00%   0.086   0.522   3.696   0.095   0.252   1.660   2.051
          10      58      57   1.72%   0.255   1.398   6.158   0.374   1.224   2.355   3.361
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/lpksgmtuiv/createObject?type_name=Folder

     .. image:: request_001.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.010   0.021   0.086   0.010   0.020   0.021   0.086
           2      28      28   0.00%   0.009   0.023   0.158   0.009   0.013   0.040   0.075
           3      38      38   0.00%   0.009   0.024   0.109   0.009   0.011   0.050   0.096
           5      51      51   0.00%   0.009   0.078   0.341   0.010   0.048   0.166   0.271
          10      58      58   0.00%   0.010   0.886   2.740   0.116   0.767   1.949   2.301
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/lpksgmtuiv/portal_factory/Folder/folder.2009-09-02.2962462486/edit

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.246   0.301   0.630   0.249   0.253   0.472   0.630
           2      27      27   0.00%   0.251   0.410   1.445   0.259   0.272   1.049   1.281
           3      37      37   0.00%   0.263   0.500   2.349   0.274   0.325   0.690   2.076
           5      52      52   0.00%   0.256   1.071   4.491   0.287   0.628   2.614   3.200
          10      59      53  10.17%   0.417   2.804  11.244   0.648   1.757   8.209   9.134
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/lpksgmtuiv/folder/

     .. image:: request_002.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.215   0.281   0.926   0.216   0.228   0.237   0.926
           2      27      27   0.00%   0.208   0.268   0.890   0.216   0.233   0.388   0.425
           3      37      37   0.00%   0.214   0.269   0.698   0.217   0.235   0.403   0.593
           5      52      52   0.00%   0.217   0.346   1.036   0.225   0.297   0.494   0.708
          10      53      53   0.00%   0.364   1.420   2.893   0.610   1.328   2.411   2.619
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/lpksgmtuiv/folder/createObject?type_name=Document

     .. image:: request_002.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.010   0.019   0.023   0.010   0.020   0.021   0.023
           2      26      26   0.00%   0.009   0.033   0.220   0.009   0.018   0.107   0.154
           3      37      37   0.00%   0.009   0.043   0.344   0.010   0.020   0.115   0.196
           5      50      50   0.00%   0.009   0.112   0.644   0.011   0.069   0.269   0.385
          10      52      52   0.00%   0.021   0.934   2.593   0.128   0.836   1.860   2.214
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/lpksgmtuiv/folder/portal_factory/Document/document.2009-09-02.2973330752/edit

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.323   0.352   0.393   0.326   0.352   0.391   0.393
           2      26      26   0.00%   0.394   0.749   2.485   0.415   0.445   1.686   1.984
           3      37      37   0.00%   0.418   0.831   2.532   0.437   0.622   1.988   2.336
           5      50      46   8.00%   0.438   2.292  10.439   0.484   1.471   5.846   7.937
          10      47      31  34.04%   1.109   6.378  15.533   1.667   4.097  13.029  13.656
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/lpksgmtuiv/folder/noveboracensis-volans-ad-bradus-vulgaris

     .. image:: request_003.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.194   0.215   0.360   0.199   0.202   0.210   0.360
           2      26      26   0.00%   0.181   0.229   0.440   0.201   0.220   0.268   0.317
           3      37      37   0.00%   0.183   0.267   0.765   0.191   0.214   0.488   0.620
           5      46      46   0.00%   0.183   0.320   0.733   0.211   0.263   0.545   0.612
          10      31      31   0.00%   0.215   1.227   2.784   0.466   1.218   1.931   2.318
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.008   0.013   0.031   0.008   0.009   0.019   0.031
           2      26      26   0.00%   0.008   0.027   0.224   0.008   0.009   0.031   0.184
           3      37      37   0.00%   0.007   0.032   0.180   0.008   0.009   0.129   0.154
           5      46      46   0.00%   0.008   0.080   1.025   0.009   0.042   0.162   0.260
          10      31      31   0.00%   0.128   1.261   2.388   0.529   1.178   2.009   2.387
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_004.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.058   0.073   0.149   0.058   0.068   0.079   0.149
           2      26      26   0.00%   0.058   0.093   0.323   0.059   0.077   0.117   0.313
           3      37      37   0.00%   0.058   0.101   0.327   0.060   0.078   0.166   0.306
           5      46      46   0.00%   0.058   0.203   0.874   0.064   0.124   0.439   0.642
          10      31      31   0.00%   0.133   1.148   2.905   0.360   0.965   1.936   2.402
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 13 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
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