======================
FunkLoad_ bench report
======================


:date: 2009-09-02 15:19:45
:abstract: Heavy write load test scenario
           Bench result of ``Writeheavy.test_WriteHeavy``: 
           Heavy write load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 15:19:45
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

* 114 tests, 21 error(s)
* 1334 pages, 21 error(s)
* 1641 requests, 21 error(s)


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.067       8       8   0.00%
       2   0.117      16      14  12.50%
       3   0.183      23      22   4.35%
       5   0.217      31      26  16.13%
      10   0.192      36      23  36.11%
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
       1   0.742   3.000      89      89   0.00%   0.011   0.206   1.185   0.021   0.100   0.681   0.692
       2   1.525   4.000     185     183   1.08%   0.010   0.211   1.127   0.020   0.105   0.653   0.703
       3   2.192   6.000     264     263   0.38%   0.011   0.279   2.754   0.025   0.117   0.727   0.899
       5   2.967   7.000     361     356   1.39%   0.011   0.512  11.221   0.052   0.214   1.300   2.189
      10   3.517  11.000     435     422   2.99%   0.013   1.325  18.155   0.132   0.680   3.565   4.861
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.942   3.000     113     113   0.00%   0.010   0.163   0.964   0.012   0.101   0.311   0.483
       2   1.900   4.000     228     226   0.88%   0.009   0.176   0.914   0.012   0.107   0.431   0.487
       3   2.767   6.000     332     331   0.30%   0.009   0.223   2.386   0.021   0.123   0.500   0.681
       5   3.725   8.000     447     442   1.12%   0.009   0.436  10.776   0.037   0.231   0.838   1.629
      10   4.342  11.000     521     508   2.50%   0.013   1.404  17.505   0.132   0.717   2.695   3.937
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 008 post: /coreloadtests/Members/brevis/folder-3/portal_factory/Document/document.2009-09-02.2886173241/edit took **2.200s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 007 post: /coreloadtests/Members/montanus/portal_factory/Folder/folder.2009-09-02.2897260235/edit took **1.238s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 006 get: /coreloadtests/Members/montanus/view took **0.439s**
  `Get /coreloadtests/Members/user/view`
* In page 007 redirect: /coreloadtests/Members/montanus/folder-4/ took **0.358s**
  ``
* In page 008 redirect: /coreloadtests/Members/montanus/folder-4/albus-fuscus-lutea-albus-silvestris took **0.324s**
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
           1       8       8   0.00%   0.095   0.103   0.115   0.095   0.105   0.115   0.115
           2      16      16   0.00%   0.093   0.124   0.281   0.095   0.104   0.255   0.281
           3      22      22   0.00%   0.074   0.107   0.152   0.077   0.105   0.123   0.132
           5      31      31   0.00%   0.094   0.263   0.752   0.103   0.227   0.437   0.744
          10      37      37   0.00%   0.108   0.593   1.576   0.192   0.491   1.301   1.489
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/join_form

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.076   0.080   0.107   0.076   0.076   0.107   0.107
           2      18      18   0.00%   0.054   0.085   0.245   0.056   0.075   0.105   0.245
           3      25      25   0.00%   0.056   0.102   0.240   0.075   0.077   0.162   0.164
           5      35      35   0.00%   0.055   0.173   0.514   0.075   0.146   0.324   0.481
          10      42      42   0.00%   0.055   0.640   1.946   0.085   0.387   1.384   1.587
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/join_form

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.079   0.092   0.160   0.079   0.080   0.160   0.160
           2      18      18   0.00%   0.070   0.105   0.297   0.078   0.089   0.160   0.297
           3      25      25   0.00%   0.070   0.162   0.789   0.080   0.090   0.377   0.734
           5      36      36   0.00%   0.061   0.175   0.617   0.081   0.109   0.303   0.584
          10      45      45   0.00%   0.081   0.589   2.747   0.094   0.356   1.406   1.691
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Post /coreloadtests/login_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/login_form

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.091   0.099   0.101   0.091   0.100   0.101   0.101
           2      18      18   0.00%   0.090   0.156   0.556   0.091   0.105   0.266   0.556
           3      25      25   0.00%   0.074   0.212   0.681   0.091   0.113   0.618   0.635
           5      36      36   0.00%   0.070   0.306   1.568   0.090   0.169   0.625   1.081
          10      45      45   0.00%   0.071   0.790   7.009   0.191   0.502   1.324   1.779
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get /coreloadtests/dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/dashboard

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.121   0.136   0.185   0.121   0.132   0.185   0.185
           2      18      18   0.00%   0.109   0.130   0.230   0.117   0.127   0.133   0.230
           3      25      25   0.00%   0.098   0.141   0.338   0.117   0.122   0.190   0.291
           5      36      36   0.00%   0.114   0.322   0.838   0.123   0.279   0.742   0.835
          10      45      45   0.00%   0.108   0.810   3.067   0.203   0.603   1.979   2.695
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 006: Get /coreloadtests/Members/user/view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/Members/diplo/view

     .. image:: request_006.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.226   0.236   0.246   0.226   0.236   0.246   0.246
           2      18      18   0.00%   0.216   0.263   0.435   0.226   0.239   0.348   0.435
           3      25      25   0.00%   0.198   0.284   0.727   0.227   0.236   0.461   0.536
           5      35      32   8.57%   0.224   0.439   1.069   0.246   0.361   0.804   1.048
          10      44      43   2.27%   0.294   0.852   3.231   0.383   0.731   1.534   1.635
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/diplo/createObject?type_name=Folder

     .. image:: request_006.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.011   0.018   0.022   0.011   0.021   0.022   0.022
           2      18      18   0.00%   0.010   0.047   0.487   0.011   0.012   0.098   0.487
           3      25      25   0.00%   0.011   0.060   0.377   0.011   0.025   0.148   0.254
           5      32      32   0.00%   0.011   0.078   0.304   0.012   0.041   0.214   0.292
          10      43      43   0.00%   0.013   0.697   2.709   0.041   0.425   1.902   2.387
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 007: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/diplo/portal_factory/Folder/folder.2009-09-02.8959948642/edit

     .. image:: request_007.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.295   0.369   0.784   0.295   0.311   0.784   0.784
           2      18      16  11.11%   0.292   0.433   0.755   0.296   0.338   0.754   0.755
           3      25      24   4.00%   0.262   0.395   1.459   0.291   0.325   0.484   0.596
           5      32      31   3.12%   0.312   1.238   5.080   0.325   0.656   2.702   4.625
          10      39      36   7.69%   0.466   3.294  14.044   0.976   2.128   9.765  11.556
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/diplo/folder-3/

     .. image:: request_007.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.225   0.233   0.246   0.225   0.234   0.246   0.246
           2      15      15   0.00%   0.226   0.242   0.312   0.228   0.235   0.261   0.312
           3      24      24   0.00%   0.226   0.293   0.783   0.230   0.260   0.338   0.503
           5      31      31   0.00%   0.233   0.358   0.858   0.245   0.300   0.602   0.718
          10      36      36   0.00%   0.264   1.281   2.693   0.336   1.275   2.417   2.644
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/diplo/folder-3/createObject?type_name=Document

     .. image:: request_007.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.011   0.018   0.023   0.011   0.021   0.023   0.023
           2      15      15   0.00%   0.011   0.022   0.058   0.011   0.021   0.028   0.058
           3      23      23   0.00%   0.011   0.039   0.405   0.011   0.021   0.040   0.067
           5      31      31   0.00%   0.011   0.081   0.545   0.012   0.047   0.169   0.244
          10      36      36   0.00%   0.025   0.702   2.408   0.067   0.576   1.719   2.347
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 008: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/diplo/folder-3/portal_factory/Document/document.2009-09-02.8984182536/edit

     .. image:: request_008.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.472   0.596   0.964   0.472   0.483   0.964   0.964
           2      14      14   0.00%   0.451   0.527   0.914   0.462   0.471   0.711   0.914
           3      22      22   0.00%   0.450   0.880   2.386   0.457   0.664   1.992   2.256
           5      30      29   3.33%   0.434   2.200  10.776   0.653   1.543   6.355   7.440
          10      35      26  25.71%   0.959   7.048  17.505   1.419   3.784  14.319  15.295
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/diplo/folder-3/punctatus-gaster-erythro-platy-petra

     .. image:: request_008.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.198   0.214   0.231   0.198   0.217   0.231   0.231
           2      14      14   0.00%   0.191   0.239   0.414   0.192   0.215   0.289   0.414
           3      22      22   0.00%   0.203   0.278   0.763   0.209   0.226   0.522   0.545
           5      28      28   0.00%   0.209   0.324   0.941   0.220   0.296   0.453   0.470
          10      26      26   0.00%   0.315   1.282   2.955   0.482   1.079   2.647   2.800
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 009: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_009.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.010   0.012   0.020   0.010   0.010   0.020   0.020
           2      14      14   0.00%   0.009   0.016   0.033   0.009   0.010   0.026   0.033
           3      22      22   0.00%   0.009   0.060   0.414   0.009   0.019   0.137   0.399
           5      27      27   0.00%   0.009   0.068   0.388   0.010   0.025   0.216   0.222
          10      24      24   0.00%   0.018   0.880   2.426   0.039   0.561   1.912   2.147
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_009.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.073   0.080   0.084   0.073   0.083   0.084   0.084
           2      14      14   0.00%   0.062   0.092   0.279   0.063   0.083   0.089   0.279
           3      22      22   0.00%   0.064   0.136   0.593   0.082   0.085   0.228   0.519
           5      27      27   0.00%   0.062   0.147   0.614   0.065   0.103   0.280   0.351
          10      24      24   0.00%   0.084   0.658   2.535   0.105   0.470   1.522   2.264
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 3 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in Connection.py, line 594: See the server error log for details
* 10 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in FileStorage.py, line 514: See the server error log for details
* 8 time(s), code: 503::

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