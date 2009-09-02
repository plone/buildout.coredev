======================
FunkLoad_ bench report
======================


:date: 2009-09-02 17:31:32
:abstract: Heavy write load test scenario
           Bench result of ``Writeheavy.test_WriteHeavy``: 
           Heavy write load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 17:31:32
* Test: ``collective.coreloadtests.tests.test_Writeheavy.py Writeheavy.test_WriteHeavy``
* Server: http://localhost:8080
* Cycles of concurrent users: [1, 2, 3, 5, 10]
* Cycle duration: 120s
* Sleeptime between request: from 0.0s to 2.0s
* Sleeptime between test case: 1.0s
* Startup delay between thread: 0.2s
* FunkLoad_ version: 1.10.0


Bench content
-------------

The test ``Writeheavy.test_WriteHeavy`` contains: 

* 11 page(s)
* 3 redirect(s)
* 0 link(s)
* 0 image(s)
* 0 XML RPC call(s)

The bench contains:

* 117 tests, 20 error(s)
* 1321 pages, 20 error(s)
* 1629 requests, 20 error(s)


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.067       8       8   0.00%
       2   0.125      17      15  11.76%
       3   0.183      22      22   0.00%
       5   0.275      35      33   5.71%
      10   0.158      35      19  45.71%
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
       1   0.733   2.000      88      88   0.00%   0.010   0.211   1.250   0.010   0.102   0.689   0.708
       2   1.525   4.000     185     183   1.08%   0.009   0.241   2.107   0.020   0.102   0.695   0.855
       3   2.117   4.000     254     254   0.00%   0.009   0.276   2.272   0.020   0.126   0.727   1.031
       5   3.208   8.000     387     385   0.52%   0.010   0.464   5.273   0.055   0.178   1.109   1.992
      10   3.258  10.000     407     391   3.93%   0.010   1.369  15.953   0.154   0.822   3.338   4.822
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.933   3.000     112     112   0.00%   0.008   0.166   0.987   0.010   0.106   0.318   0.485
       2   1.917   5.000     230     228   0.87%   0.008   0.198   1.871   0.011   0.109   0.398   0.543
       3   2.675   5.000     321     321   0.00%   0.008   0.218   1.837   0.017   0.135   0.485   0.575
       5   4.058   8.000     487     485   0.41%   0.008   0.371   5.006   0.042   0.208   0.770   1.318
      10   3.992  10.000     479     463   3.34%   0.010   1.517  15.896   0.165   0.822   2.738   5.894
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 008 post: /coreloadtests/Members/maculatus/folder-5/portal_factory/Document/document.2009-09-02.2087831542/edit took **1.399s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 007 post: /coreloadtests/Members/variegatus/portal_factory/Folder/folder.2009-09-02.2097161344/edit took **1.151s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 006 get: /coreloadtests/Members/sinensis/view took **0.402s**
  `Get /coreloadtests/Members/user/view`
* In page 008 redirect: /coreloadtests/Members/maculatus/folder-5/pachys-rhiza-so-sativus-cauda took **0.376s**
  ``
* In page 007 redirect: /coreloadtests/Members/sinensis/folder-8/ took **0.366s**
  ``

Page detail stats
-----------------


PAGE 001: Get /coreloadtests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests

     .. image:: request_001.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.096   0.107   0.116   0.096   0.108   0.116   0.116
           2      17      17   0.00%   0.095   0.123   0.355   0.095   0.097   0.230   0.355
           3      22      22   0.00%   0.078   0.160   0.444   0.095   0.106   0.304   0.373
           5      33      33   0.00%   0.075   0.217   0.875   0.095   0.120   0.628   0.790
          10      35      35   0.00%   0.095   0.755   2.831   0.148   0.596   1.475   2.263
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/join_form

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.073   0.080   0.108   0.073   0.076   0.108   0.108
           2      19      19   0.00%   0.056   0.078   0.129   0.067   0.077   0.082   0.129
           3      25      25   0.00%   0.056   0.092   0.307   0.066   0.076   0.100   0.256
           5      38      38   0.00%   0.056   0.132   0.385   0.058   0.089   0.262   0.352
          10      40      40   0.00%   0.076   0.620   2.759   0.141   0.425   1.279   2.557
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/join_form

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.081   0.095   0.160   0.081   0.091   0.160   0.160
           2      19      19   0.00%   0.077   0.093   0.165   0.080   0.082   0.156   0.165
           3      24      24   0.00%   0.080   0.140   0.382   0.081   0.101   0.261   0.326
           5      37      37   0.00%   0.071   0.226   0.822   0.084   0.145   0.588   0.821
          10      43      43   0.00%   0.082   0.606   2.074   0.146   0.388   1.466   1.675
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Post /coreloadtests/login_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/login_form

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.093   0.101   0.105   0.093   0.102   0.105   0.105
           2      18      18   0.00%   0.088   0.144   0.695   0.090   0.104   0.205   0.695
           3      23      23   0.00%   0.072   0.141   0.492   0.091   0.104   0.220   0.252
           5      36      36   0.00%   0.093   0.253   1.500   0.102   0.159   0.473   0.880
          10      43      43   0.00%   0.102   0.889   2.686   0.198   0.737   1.692   2.077
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get /coreloadtests/dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/dashboard

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.137   0.234   0.793   0.137   0.150   0.793   0.793
           2      18      18   0.00%   0.085   0.145   0.279   0.124   0.131   0.205   0.279
           3      23      23   0.00%   0.124   0.195   0.520   0.129   0.140   0.381   0.409
           5      36      36   0.00%   0.122   0.244   1.269   0.128   0.163   0.381   0.586
          10      42      42   0.00%   0.095   0.755   1.995   0.162   0.680   1.662   1.766
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 006: Get /coreloadtests/Members/user/view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/Members/protos/view

     .. image:: request_006.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.228   0.255   0.297   0.228   0.248   0.297   0.297
           2      17      16   5.88%   0.244   0.306   0.468   0.244   0.292   0.398   0.468
           3      23      23   0.00%   0.228   0.316   0.701   0.239   0.282   0.365   0.552
           5      36      36   0.00%   0.208   0.402   0.900   0.234   0.345   0.703   0.770
          10      42      41   2.38%   0.274   1.149   2.756   0.385   1.006   1.867   2.166
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/protos/createObject?type_name=Folder

     .. image:: request_006.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.010   0.011   0.020   0.010   0.010   0.020   0.020
           2      16      16   0.00%   0.009   0.036   0.204   0.010   0.020   0.146   0.204
           3      23      23   0.00%   0.009   0.043   0.190   0.010   0.020   0.141   0.176
           5      36      36   0.00%   0.010   0.096   0.587   0.011   0.050   0.251   0.395
          10      41      41   0.00%   0.010   0.784   2.750   0.056   0.651   1.652   2.214
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 007: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/protos/portal_factory/Folder/folder.2009-09-02.8042930516/edit

     .. image:: request_007.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.295   0.394   0.987   0.295   0.313   0.987   0.987
           2      16      15   6.25%   0.309   0.416   1.000   0.310   0.328   0.716   1.000
           3      23      23   0.00%   0.292   0.518   1.837   0.310   0.337   1.075   1.445
           5      36      34   5.56%   0.298   1.151   5.006   0.327   0.500   4.119   4.655
          10      39      33  15.38%   0.674   3.672  12.966   0.925   2.154  10.050  11.625
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/protos/folder-5/

     .. image:: request_007.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.224   0.241   0.263   0.224   0.245   0.263   0.263
           2      15      15   0.00%   0.230   0.259   0.316   0.247   0.252   0.301   0.316
           3      23      23   0.00%   0.229   0.338   0.904   0.235   0.269   0.503   0.533
           5      34      34   0.00%   0.231   0.366   1.519   0.249   0.296   0.574   0.647
          10      33      33   0.00%   0.290   1.123   2.536   0.413   0.996   1.931   2.321
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/protos/folder-5/createObject?type_name=Document

     .. image:: request_007.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.010   0.012   0.020   0.010   0.011   0.020   0.020
           2      15      15   0.00%   0.009   0.044   0.470   0.010   0.011   0.021   0.470
           3      23      23   0.00%   0.009   0.032   0.206   0.010   0.020   0.055   0.104
           5      33      33   0.00%   0.010   0.118   1.467   0.010   0.042   0.203   0.232
          10      33      33   0.00%   0.013   0.862   2.818   0.044   0.844   1.840   2.212
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 008: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/protos/folder-5/portal_factory/Document/document.2009-09-02.8083669111/edit

     .. image:: request_008.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.454   0.482   0.501   0.454   0.485   0.501   0.501
           2      15      15   0.00%   0.472   0.839   1.871   0.476   0.543   1.732   1.871
           3      23      23   0.00%   0.452   0.644   1.189   0.474   0.542   0.924   1.154
           5      33      33   0.00%   0.434   1.399   3.701   0.481   1.172   2.518   3.399
          10      30      21  30.00%   0.940   7.621  15.896   1.854   6.821  15.104  15.409
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/protos/folder-5/silvestris-oeos-australis-melanus-erythro

     .. image:: request_008.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.211   0.218   0.242   0.211   0.213   0.242   0.242
           2      15      15   0.00%   0.197   0.252   0.358   0.197   0.236   0.314   0.358
           3      22      22   0.00%   0.218   0.297   0.549   0.219   0.256   0.485   0.506
           5      33      33   0.00%   0.207   0.376   1.191   0.235   0.285   0.685   1.029
          10      20      20   0.00%   0.407   1.240   2.993   0.630   1.104   2.309   2.993
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 009: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_009.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.008   0.012   0.019   0.008   0.009   0.019   0.019
           2      15      15   0.00%   0.008   0.020   0.115   0.008   0.009   0.055   0.115
           3      22      22   0.00%   0.008   0.045   0.575   0.008   0.009   0.041   0.138
           5      33      33   0.00%   0.008   0.087   0.527   0.009   0.041   0.211   0.445
          10      19      19   0.00%   0.033   1.002   2.226   0.085   0.711   2.154   2.226
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_009.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.064   0.080   0.093   0.064   0.082   0.093   0.093
           2      15      15   0.00%   0.063   0.091   0.166   0.064   0.084   0.111   0.166
           3      22      22   0.00%   0.064   0.095   0.306   0.073   0.085   0.113   0.120
           5      33      33   0.00%   0.063   0.152   0.498   0.066   0.103   0.331   0.463
          10      19      19   0.00%   0.119   0.942   2.338   0.273   0.801   2.319   2.338
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 5 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in Connection.py, line 594: See the server error log for details
* 8 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in FileStorage.py, line 514: See the server error log for details
* 7 time(s), code: 503::

    No traceback.


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