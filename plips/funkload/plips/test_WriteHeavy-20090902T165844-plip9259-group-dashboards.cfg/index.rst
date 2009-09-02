======================
FunkLoad_ bench report
======================


:date: 2009-09-02 16:58:44
:abstract: Heavy write load test scenario
           Bench result of ``Writeheavy.test_WriteHeavy``: 
           Heavy write load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 16:58:44
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
* 4 redirect(s)
* 0 link(s)
* 0 image(s)
* 0 XML RPC call(s)

The bench contains:

* 115 tests, 14 error(s)
* 1323 pages, 14 error(s)
* 1773 requests, 14 error(s)


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
       5   0.258      32      31   3.12%
      10   0.200      37      24  35.14%
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
       1   0.767   2.000      92      92   0.00%   0.009   0.199   1.310   0.010   0.095   0.561   0.695
       2   1.508   6.000     181     181   0.00%   0.009   0.260   2.457   0.011   0.097   0.736   1.045
       3   2.217   6.000     266     266   0.00%   0.009   0.316   5.025   0.015   0.114   0.862   1.220
       5   3.050   8.000     367     366   0.27%   0.009   0.519  10.479   0.047   0.187   1.224   2.134
      10   3.367  11.000     417     404   3.12%   0.010   1.364  14.953   0.116   0.644   3.589   5.646
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   1.042   3.000     125     125   0.00%   0.006   0.146   1.078   0.009   0.091   0.312   0.456
       2   2.050   7.000     246     246   0.00%   0.006   0.191   2.231   0.009   0.094   0.439   0.630
       3   3.017   8.000     362     362   0.00%   0.006   0.232   4.719   0.010   0.108   0.499   0.846
       5   4.142   9.000     497     496   0.20%   0.006   0.385  10.164   0.015   0.176   0.743   1.376
      10   4.525  11.000     543     530   2.39%   0.006   1.327  17.879   0.097   0.539   2.885   4.706
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 008 post: /coreloadtests/Members/mauro/folder-1/portal_factory/Document/document.2009-09-02.2374911972/edit took **2.405s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 007 post: /coreloadtests/Members/oeos/portal_factory/Folder/folder.2009-09-02.2405340355/edit took **0.929s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 006 get: /coreloadtests/Members/albus/view took **0.394s**
  `Get /coreloadtests/Members/user/view`
* In page 007 redirect: /coreloadtests/Members/oeos/folder-5/ took **0.338s**
  ``
* In page 008 redirect: /coreloadtests/Members/mauro/folder-1/lineatus-diplo-noveboracensis-parvus-brevis took **0.301s**
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
           1       8       8   0.00%   0.086   0.098   0.110   0.086   0.095   0.110   0.110
           2      15      15   0.00%   0.094   0.104   0.141   0.094   0.105   0.107   0.141
           3      22      22   0.00%   0.074   0.139   0.437   0.095   0.107   0.201   0.320
           5      31      31   0.00%   0.084   0.219   0.912   0.095   0.117   0.438   0.881
          10      36      36   0.00%   0.096   0.833   3.589   0.124   0.660   1.731   3.117
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/join_form

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.075   0.080   0.109   0.075   0.076   0.109   0.109
           2      17      17   0.00%   0.075   0.082   0.157   0.075   0.077   0.082   0.157
           3      24      24   0.00%   0.066   0.095   0.155   0.073   0.079   0.135   0.140
           5      35      35   0.00%   0.056   0.189   0.709   0.077   0.125   0.392   0.635
          10      42      42   0.00%   0.056   0.617   3.508   0.076   0.387   1.685   1.789
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/join_form

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.079   0.095   0.184   0.079   0.081   0.184   0.184
           2      17      17   0.00%   0.080   0.150   0.711   0.080   0.090   0.273   0.711
           3      25      25   0.00%   0.061   0.118   0.327   0.080   0.086   0.219   0.220
           5      35      35   0.00%   0.074   0.197   0.880   0.081   0.116   0.535   0.696
          10      43      43   0.00%   0.066   0.597   3.039   0.097   0.304   1.878   2.197
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Post /coreloadtests/login_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/login_form

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.090   0.097   0.105   0.090   0.101   0.105   0.105
           2      17      17   0.00%   0.070   0.123   0.408   0.081   0.102   0.232   0.408
           3      25      25   0.00%   0.073   0.170   0.812   0.080   0.103   0.355   0.392
           5      35      35   0.00%   0.070   0.216   1.376   0.092   0.112   0.388   0.564
          10      43      43   0.00%   0.073   0.799   4.760   0.122   0.460   1.699   1.974
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get /coreloadtests/dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/dashboard

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.006   0.007   0.009   0.006   0.007   0.009   0.009
           2      17      17   0.00%   0.006   0.011   0.059   0.007   0.007   0.017   0.059
           3      25      25   0.00%   0.006   0.017   0.111   0.007   0.008   0.036   0.056
           5      35      35   0.00%   0.006   0.044   0.310   0.007   0.011   0.090   0.205
          10      44      44   0.00%   0.006   0.291   1.375   0.011   0.108   0.885   1.183
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/acl_users/credentials_cookie_auth/require_login?came_from=http%3A//localhost%3A8080/coreloadtests/dashboard

     .. image:: request_005.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.070   0.098   0.131   0.070   0.094   0.131   0.131
           2      17      17   0.00%   0.079   0.098   0.195   0.081   0.090   0.136   0.195
           3      25      25   0.00%   0.069   0.104   0.183   0.087   0.101   0.129   0.134
           5      35      35   0.00%   0.074   0.165   0.812   0.090   0.102   0.267   0.743
          10      44      44   0.00%   0.071   0.415   1.569   0.095   0.285   0.949   1.218
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 006: Get /coreloadtests/Members/user/view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/Members/aquam/view

     .. image:: request_006.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.237   0.263   0.278   0.237   0.267   0.278   0.278
           2      17      17   0.00%   0.218   0.256   0.353   0.221   0.248   0.317   0.353
           3      25      25   0.00%   0.209   0.353   0.957   0.231   0.296   0.571   0.818
           5      35      34   2.86%   0.225   0.394   1.158   0.253   0.343   0.570   0.642
          10      41      41   0.00%   0.294   0.815   2.079   0.367   0.653   1.556   1.762
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/aquam/createObject?type_name=Folder

     .. image:: request_006.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.009   0.011   0.020   0.009   0.010   0.020   0.020
           2      17      17   0.00%   0.009   0.020   0.106   0.009   0.010   0.060   0.106
           3      25      25   0.00%   0.009   0.037   0.136   0.009   0.020   0.106   0.134
           5      34      34   0.00%   0.009   0.112   0.828   0.010   0.039   0.315   0.595
          10      40      40   0.00%   0.016   0.578   3.382   0.098   0.471   1.106   1.940
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 007: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/aquam/portal_factory/Folder/folder.2009-09-02.8341487346/edit

     .. image:: request_007.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.298   0.311   0.321   0.298   0.316   0.321   0.321
           2      16      16   0.00%   0.304   0.582   1.550   0.307   0.420   1.012   1.550
           3      24      24   0.00%   0.298   0.531   1.388   0.315   0.405   1.122   1.159
           5      33      33   0.00%   0.294   0.929   2.708   0.326   0.668   2.087   2.660
          10      39      34  12.82%   0.481   3.460  13.162   0.733   2.761   9.210  10.951
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/aquam/folder-7/

     .. image:: request_007.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.229   0.237   0.250   0.229   0.237   0.250   0.250
           2      16      16   0.00%   0.226   0.275   0.442   0.228   0.243   0.415   0.442
           3      24      24   0.00%   0.229   0.313   0.968   0.239   0.265   0.382   0.499
           5      33      33   0.00%   0.239   0.338   0.882   0.249   0.276   0.506   0.605
          10      34      34   0.00%   0.253   1.178   4.565   0.318   0.776   2.885   3.183
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/aquam/folder-7/createObject?type_name=Document

     .. image:: request_007.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.009   0.011   0.022   0.009   0.010   0.022   0.022
           2      16      16   0.00%   0.010   0.031   0.177   0.010   0.014   0.124   0.177
           3      24      24   0.00%   0.010   0.081   0.905   0.010   0.011   0.182   0.337
           5      32      32   0.00%   0.010   0.116   1.392   0.010   0.049   0.187   0.454
          10      33      33   0.00%   0.010   0.956   3.943   0.064   0.729   2.641   3.475
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 008: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/aquam/folder-7/portal_factory/Document/document.2009-09-02.8366008345/edit

     .. image:: request_008.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.454   0.622   1.078   0.454   0.485   1.078   1.078
           2      16      16   0.00%   0.439   0.830   2.231   0.465   0.541   2.116   2.231
           3      24      24   0.00%   0.449   1.063   4.719   0.485   0.795   2.005   2.142
           5      31      31   0.00%   0.502   2.405  10.164   0.590   1.737   4.489   9.043
          10      32      24  25.00%   1.436   7.858  17.879   2.278   7.387  14.266  16.082
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/aquam/folder-7/palustris-palustris-argentatus-punctatus-protos

     .. image:: request_008.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.209   0.221   0.237   0.209   0.217   0.237   0.237
           2      16      16   0.00%   0.203   0.242   0.333   0.206   0.232   0.303   0.333
           3      24      24   0.00%   0.202   0.273   0.445   0.212   0.262   0.362   0.378
           5      31      31   0.00%   0.196   0.301   0.618   0.213   0.299   0.371   0.499
          10      24      24   0.00%   0.267   1.379   4.332   0.345   1.052   3.156   3.725
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 009: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_009.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.008   0.009   0.009   0.008   0.009   0.009   0.009
           2      16      16   0.00%   0.008   0.010   0.021   0.008   0.009   0.019   0.021
           3      23      23   0.00%   0.008   0.035   0.204   0.008   0.012   0.108   0.109
           5      31      31   0.00%   0.008   0.128   0.813   0.008   0.029   0.450   0.609
          10      24      24   0.00%   0.009   0.658   2.578   0.019   0.539   1.694   1.902
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_009.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.067   0.082   0.092   0.067   0.083   0.092   0.092
           2      16      16   0.00%   0.063   0.082   0.120   0.064   0.081   0.114   0.120
           3      23      23   0.00%   0.073   0.161   0.846   0.082   0.098   0.277   0.319
           5      31      31   0.00%   0.063   0.161   0.644   0.077   0.117   0.336   0.379
          10      24      24   0.00%   0.091   0.426   1.625   0.096   0.332   0.911   1.222
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 4 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in Connection.py, line 594: See the server error log for details
* 7 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in FileStorage.py, line 514: See the server error log for details
* 3 time(s), code: 503::

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