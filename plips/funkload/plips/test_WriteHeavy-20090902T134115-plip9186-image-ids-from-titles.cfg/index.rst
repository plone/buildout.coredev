======================
FunkLoad_ bench report
======================


:date: 2009-09-02 13:41:15
:abstract: Heavy write load test scenario
           Bench result of ``Writeheavy.test_WriteHeavy``: 
           Heavy write load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 13:41:15
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

* 113 tests, 15 error(s)
* 1330 pages, 15 error(s)
* 1646 requests, 15 error(s)


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.067       8       8   0.00%
       2   0.133      16      16   0.00%
       3   0.183      22      22   0.00%
       5   0.250      30      30   0.00%
      10   0.183      37      22  40.54%
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
       1   0.733   2.000      88      88   0.00%   0.009   0.200   0.992   0.010   0.108   0.552   0.648
       2   1.558   4.000     187     187   0.00%   0.009   0.242   2.370   0.010   0.106   0.641   0.766
       3   2.192   5.000     263     263   0.00%   0.009   0.274   3.244   0.019   0.130   0.698   0.930
       5   2.942   7.000     353     353   0.00%   0.009   0.561  10.409   0.026   0.193   1.360   2.253
      10   3.533  11.000     439     424   3.42%   0.010   1.242  13.389   0.145   0.610   3.214   5.237
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.933   3.000     112     112   0.00%   0.009   0.157   0.786   0.010   0.117   0.292   0.454
       2   1.967   4.000     236     236   0.00%   0.008   0.192   2.121   0.010   0.119   0.441   0.493
       3   2.758   6.000     331     331   0.00%   0.008   0.218   2.892   0.018   0.147   0.469   0.630
       5   3.708   8.000     445     445   0.00%   0.008   0.445  10.186   0.024   0.201   0.826   1.655
      10   4.350  11.000     522     507   2.87%   0.010   1.376  15.807   0.146   0.649   2.936   5.129
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 008 post: /coreloadtests/Members/leucus/folder/portal_factory/Document/document.2009-09-02.3958790963/edit took **2.405s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 007 post: /coreloadtests/Members/viridis/portal_factory/Folder/folder.2009-09-02.3937173098/edit took **1.274s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 004 post: /coreloadtests/login_form took **0.453s**
  `Post /coreloadtests/login_form`
* In page 006 get: /coreloadtests/Members/cristatus/view took **0.384s**
  `Get /coreloadtests/Members/user/view`
* In page 007 redirect: /coreloadtests/Members/viridis/folder-1/ took **0.355s**
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
           1       8       8   0.00%   0.091   0.099   0.112   0.091   0.102   0.112   0.112
           2      16      16   0.00%   0.091   0.147   0.658   0.091   0.093   0.333   0.658
           3      22      22   0.00%   0.087   0.141   0.521   0.091   0.102   0.208   0.237
           5      29      29   0.00%   0.071   0.177   0.637   0.091   0.110   0.302   0.414
          10      37      37   0.00%   0.090   0.562   1.901   0.125   0.381   1.381   1.619
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/join_form

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.073   0.078   0.108   0.073   0.074   0.108   0.108
           2      18      18   0.00%   0.072   0.097   0.457   0.073   0.074   0.094   0.457
           3      25      25   0.00%   0.054   0.097   0.413   0.073   0.074   0.157   0.168
           5      34      34   0.00%   0.054   0.127   0.565   0.065   0.075   0.187   0.505
          10      44      44   0.00%   0.055   0.408   1.394   0.128   0.314   0.892   1.067
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/join_form

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.089   0.115   0.237   0.089   0.099   0.237   0.237
           2      18      18   0.00%   0.072   0.106   0.352   0.077   0.093   0.111   0.352
           3      25      25   0.00%   0.069   0.136   0.351   0.078   0.102   0.270   0.325
           5      34      34   0.00%   0.058   0.250   1.138   0.079   0.118   0.516   0.724
          10      45      45   0.00%   0.068   0.485   2.312   0.119   0.337   1.221   1.383
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Post /coreloadtests/login_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/login_form

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.201   0.253   0.552   0.201   0.211   0.552   0.552
           2      18      18   0.00%   0.087   0.244   0.534   0.099   0.209   0.475   0.534
           3      25      25   0.00%   0.079   0.251   0.742   0.089   0.218   0.448   0.635
           5      33      33   0.00%   0.078   0.453   3.872   0.088   0.205   0.656   2.062
          10      44      44   0.00%   0.105   1.286   9.503   0.133   0.624   2.080   7.853
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get /coreloadtests/dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/dashboard

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.117   0.127   0.178   0.117   0.121   0.178   0.178
           2      17      17   0.00%   0.116   0.151   0.378   0.117   0.128   0.196   0.378
           3      25      25   0.00%   0.092   0.158   0.314   0.117   0.139   0.264   0.293
           5      33      33   0.00%   0.107   0.265   0.912   0.120   0.184   0.541   0.826
          10      44      44   0.00%   0.107   0.751   3.081   0.207   0.472   1.589   2.368
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 006: Get /coreloadtests/Members/user/view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/Members/australis/view

     .. image:: request_006.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.207   0.213   0.220   0.207   0.218   0.220   0.220
           2      17      17   0.00%   0.209   0.244   0.461   0.217   0.225   0.263   0.461
           3      25      25   0.00%   0.209   0.307   0.718   0.215   0.225   0.529   0.643
           5      33      33   0.00%   0.210   0.384   1.039   0.218   0.331   0.603   0.761
          10      44      44   0.00%   0.225   0.863   3.741   0.360   0.668   1.609   2.323
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/australis/createObject?type_name=Folder

     .. image:: request_006.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.009   0.011   0.020   0.009   0.010   0.020   0.020
           2      17      17   0.00%   0.009   0.013   0.021   0.010   0.010   0.021   0.021
           3      24      24   0.00%   0.009   0.049   0.409   0.010   0.020   0.054   0.311
           5      33      33   0.00%   0.009   0.080   0.744   0.009   0.026   0.114   0.638
          10      42      42   0.00%   0.010   0.584   3.179   0.066   0.328   1.230   1.698
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 007: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/australis/portal_factory/Folder/folder.2009-09-02.9871866600/edit

     .. image:: request_007.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.276   0.285   0.299   0.276   0.281   0.299   0.299
           2      17      17   0.00%   0.260   0.389   1.279   0.267   0.292   0.708   1.279
           3      24      24   0.00%   0.250   0.458   1.885   0.283   0.301   0.726   0.953
           5      32      32   0.00%   0.278   1.274   7.549   0.321   0.745   2.756   3.860
          10      42      39   7.14%   0.418   3.177  12.134   0.818   1.933   7.886  10.791
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/australis/folder/

     .. image:: request_007.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.219   0.225   0.234   0.219   0.228   0.234   0.234
           2      17      17   0.00%   0.219   0.241   0.276   0.220   0.239   0.266   0.276
           3      24      24   0.00%   0.200   0.292   0.640   0.202   0.245   0.564   0.630
           5      32      32   0.00%   0.221   0.355   1.281   0.233   0.290   0.500   0.756
          10      39      39   0.00%   0.218   1.268   3.346   0.348   0.950   2.598   3.090
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/australis/folder/createObject?type_name=Document

     .. image:: request_007.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.010   0.010   0.011   0.010   0.010   0.011   0.011
           2      17      17   0.00%   0.010   0.020   0.116   0.010   0.010   0.021   0.116
           3      24      24   0.00%   0.009   0.026   0.124   0.010   0.011   0.063   0.117
           5      32      32   0.00%   0.009   0.061   0.333   0.010   0.024   0.137   0.193
          10      39      39   0.00%   0.033   0.950   2.925   0.106   0.812   2.049   2.702
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 008: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/australis/folder/portal_factory/Document/document.2009-09-02.9905243548/edit

     .. image:: request_008.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.418   0.496   0.786   0.418   0.470   0.786   0.786
           2      16      16   0.00%   0.407   0.719   2.121   0.441   0.493   1.893   2.121
           3      22      22   0.00%   0.430   0.728   2.892   0.454   0.511   0.896   1.845
           5      30      30   0.00%   0.452   2.405  10.186   0.480   1.405   6.080   7.567
          10      36      24  33.33%   0.803   6.166  15.807   1.370   4.382  11.993  14.044
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/australis/folder/albus-dolicho-dulcis-dermis-octa

     .. image:: request_008.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.192   0.200   0.208   0.192   0.204   0.208   0.208
           2      16      16   0.00%   0.196   0.237   0.492   0.204   0.217   0.252   0.492
           3      22      22   0.00%   0.185   0.303   0.814   0.204   0.246   0.496   0.619
           5      30      30   0.00%   0.189   0.302   0.822   0.205   0.249   0.442   0.591
          10      22      22   0.00%   0.239   1.518   3.828   0.339   1.435   3.227   3.396
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 009: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_009.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.009   0.010   0.013   0.009   0.010   0.013   0.013
           2      16      16   0.00%   0.008   0.018   0.081   0.008   0.010   0.028   0.081
           3      22      22   0.00%   0.008   0.021   0.069   0.009   0.018   0.049   0.063
           5      30      30   0.00%   0.008   0.055   0.176   0.009   0.036   0.148   0.164
          10      22      22   0.00%   0.010   0.776   2.769   0.107   0.675   1.510   2.014
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_009.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.073   0.080   0.091   0.073   0.078   0.091   0.091
           2      16      16   0.00%   0.060   0.081   0.186   0.060   0.079   0.094   0.186
           3      22      22   0.00%   0.064   0.103   0.248   0.074   0.087   0.154   0.165
           5      30      30   0.00%   0.060   0.144   0.785   0.078   0.098   0.233   0.259
          10      22      22   0.00%   0.060   0.596   2.210   0.105   0.436   1.689   2.118
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 7 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in Connection.py, line 594: See the server error log for details
* 8 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
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