======================
FunkLoad_ bench report
======================


:date: 2009-09-02 15:52:11
:abstract: Heavy write load test scenario
           Bench result of ``Writeheavy.test_WriteHeavy``: 
           Heavy write load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 15:52:11
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

* 118 tests, 15 error(s)
* 1357 pages, 15 error(s)
* 1682 requests, 15 error(s)


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.067       8       8   0.00%
       2   0.133      16      16   0.00%
       3   0.192      24      23   4.17%
       5   0.242      33      29  12.12%
      10   0.225      37      27  27.03%
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
       1   0.742   2.000      89      89   0.00%   0.010   0.203   1.216   0.020   0.101   0.565   0.701
       2   1.508   3.000     181     181   0.00%   0.009   0.229   1.839   0.011   0.103   0.673   0.766
       3   2.225   5.000     268     267   0.37%   0.009   0.257   2.334   0.015   0.121   0.692   0.892
       5   3.142   7.000     381     377   1.05%   0.009   0.446   9.573   0.042   0.172   1.030   1.872
      10   3.567  11.000     438     428   2.28%   0.010   1.300  13.402   0.101   0.606   3.609   5.289
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.942   3.000     113     113   0.00%   0.008   0.160   0.984   0.011   0.101   0.301   0.472
       2   1.908   4.000     229     229   0.00%   0.008   0.181   1.631   0.010   0.108   0.447   0.480
       3   2.808   7.000     337     336   0.30%   0.008   0.207   2.049   0.010   0.134   0.465   0.585
       5   3.942   8.000     473     469   0.85%   0.008   0.413   9.100   0.037   0.202   0.724   1.334
      10   4.417  12.000     530     520   1.89%   0.010   1.300  16.694   0.110   0.619   2.846   4.264
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 008 post: /coreloadtests/Members/mono/folder-5/portal_factory/Document/document.2009-09-02.2574527498/edit took **2.289s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 007 post: /coreloadtests/Members/lutea/portal_factory/Folder/folder.2009-09-02.2565033066/edit took **0.998s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 006 get: /coreloadtests/Members/dolicho/view took **0.432s**
  `Get /coreloadtests/Members/user/view`
* In page 008 redirect: /coreloadtests/Members/lutea/folder-7/oleum-palustris-arvensis-campus-archaeos took **0.346s**
  ``
* In page 007 redirect: /coreloadtests/Members/lutea/folder-7/ took **0.345s**
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
           1       8       8   0.00%   0.094   0.103   0.113   0.094   0.105   0.113   0.113
           2      16      16   0.00%   0.079   0.162   0.825   0.094   0.105   0.287   0.825
           3      24      24   0.00%   0.094   0.160   0.608   0.095   0.107   0.292   0.467
           5      34      34   0.00%   0.074   0.220   0.853   0.103   0.156   0.414   0.702
          10      36      36   0.00%   0.074   0.564   3.143   0.134   0.409   1.251   1.669
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/join_form

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.055   0.076   0.098   0.055   0.076   0.098   0.098
           2      18      18   0.00%   0.074   0.088   0.304   0.075   0.076   0.078   0.304
           3      27      27   0.00%   0.056   0.136   0.574   0.075   0.076   0.340   0.382
           5      37      37   0.00%   0.054   0.121   0.437   0.066   0.083   0.233   0.266
          10      42      42   0.00%   0.056   0.455   2.093   0.095   0.305   0.888   1.212
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/join_form

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.079   0.093   0.160   0.079   0.082   0.160   0.160
           2      17      17   0.00%   0.070   0.085   0.122   0.079   0.081   0.097   0.122
           3      27      27   0.00%   0.064   0.113   0.282   0.076   0.084   0.236   0.240
           5      36      36   0.00%   0.069   0.195   0.533   0.079   0.148   0.400   0.510
          10      45      45   0.00%   0.072   0.440   3.034   0.092   0.245   0.932   1.576
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Post /coreloadtests/login_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/login_form

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.090   0.098   0.104   0.090   0.101   0.104   0.104
           2      17      17   0.00%   0.072   0.114   0.209   0.090   0.101   0.197   0.209
           3      26      26   0.00%   0.087   0.172   0.649   0.090   0.107   0.400   0.540
           5      36      36   0.00%   0.071   0.204   0.580   0.090   0.153   0.464   0.571
          10      46      46   0.00%   0.073   0.664   2.482   0.119   0.503   1.600   1.731
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get /coreloadtests/dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/dashboard

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.129   0.150   0.206   0.129   0.145   0.206   0.206
           2      17      17   0.00%   0.117   0.142   0.315   0.120   0.126   0.196   0.315
           3      25      25   0.00%   0.121   0.162   0.363   0.123   0.135   0.223   0.343
           5      36      36   0.00%   0.116   0.294   1.178   0.124   0.199   0.668   0.800
          10      44      44   0.00%   0.132   0.828   2.962   0.222   0.622   1.879   2.068
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 006: Get /coreloadtests/Members/user/view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/Members/dorsum/view

     .. image:: request_006.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.230   0.239   0.251   0.230   0.239   0.251   0.251
           2      16      16   0.00%   0.210   0.266   0.399   0.226   0.239   0.351   0.399
           3      24      23   4.17%   0.212   0.293   0.719   0.228   0.250   0.408   0.572
           5      36      36   0.00%   0.214   0.432   1.186   0.228   0.394   0.724   0.825
          10      43      43   0.00%   0.284   0.771   2.391   0.354   0.674   1.200   1.270
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/dorsum/createObject?type_name=Folder

     .. image:: request_006.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.010   0.016   0.021   0.010   0.020   0.021   0.021
           2      16      16   0.00%   0.009   0.023   0.187   0.009   0.010   0.034   0.187
           3      23      23   0.00%   0.009   0.060   0.491   0.009   0.010   0.192   0.268
           5      36      36   0.00%   0.009   0.061   0.256   0.010   0.026   0.190   0.239
          10      43      43   0.00%   0.010   0.702   3.693   0.028   0.294   1.656   2.625
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 007: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/dorsum/portal_factory/Folder/folder.2009-09-02.8415319558/edit

     .. image:: request_007.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.287   0.300   0.318   0.287   0.301   0.318   0.318
           2      16      16   0.00%   0.272   0.372   0.557   0.286   0.313   0.521   0.557
           3      23      23   0.00%   0.278   0.546   2.049   0.283   0.406   1.340   1.580
           5      35      33   5.71%   0.290   0.998   8.454   0.320   0.612   1.600   2.628
          10      40      38   5.00%   0.855   3.634  11.440   1.131   2.665  10.176  11.299
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/dorsum/folder-2/

     .. image:: request_007.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.223   0.239   0.258   0.223   0.238   0.258   0.258
           2      16      16   0.00%   0.223   0.276   0.808   0.226   0.241   0.278   0.808
           3      23      23   0.00%   0.224   0.253   0.307   0.227   0.249   0.299   0.305
           5      33      33   0.00%   0.228   0.345   0.790   0.237   0.283   0.531   0.686
          10      38      38   0.00%   0.243   1.480   5.210   0.383   1.103   3.417   4.129
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/dorsum/folder-2/createObject?type_name=Document

     .. image:: request_007.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.010   0.018   0.021   0.010   0.021   0.021   0.021
           2      16      16   0.00%   0.009   0.038   0.362   0.010   0.011   0.073   0.362
           3      23      23   0.00%   0.009   0.026   0.171   0.010   0.020   0.043   0.061
           5      33      33   0.00%   0.010   0.072   0.270   0.010   0.064   0.148   0.167
          10      37      37   0.00%   0.011   0.749   3.095   0.016   0.495   2.220   2.724
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 008: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/dorsum/folder-2/portal_factory/Document/document.2009-09-02.8440416889/edit

     .. image:: request_008.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.453   0.598   0.984   0.453   0.479   0.984   0.984
           2      16      16   0.00%   0.427   0.617   1.631   0.447   0.473   1.087   1.631
           3      23      23   0.00%   0.438   0.628   1.100   0.447   0.516   0.921   1.060
           5      33      31   6.06%   0.438   2.289   9.100   0.488   1.549   7.481   9.025
          10      35      27  22.86%   0.885   5.954  16.694   1.434   4.232  12.811  15.253
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/dorsum/folder-2/sinensis-tris-campus-campus-noveboracensis

     .. image:: request_008.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.209   0.225   0.233   0.209   0.228   0.233   0.233
           2      16      16   0.00%   0.190   0.216   0.252   0.199   0.212   0.245   0.252
           3      23      23   0.00%   0.202   0.277   0.707   0.205   0.228   0.376   0.404
           5      30      30   0.00%   0.205   0.346   0.760   0.218   0.345   0.486   0.504
          10      27      27   0.00%   0.259   1.089   3.194   0.326   0.673   2.304   2.747
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 009: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_009.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.008   0.009   0.009   0.008   0.009   0.009   0.009
           2      16      16   0.00%   0.008   0.010   0.019   0.008   0.009   0.015   0.019
           3      23      23   0.00%   0.008   0.020   0.077   0.008   0.009   0.052   0.068
           5      29      29   0.00%   0.008   0.090   0.597   0.009   0.037   0.271   0.344
          10      27      27   0.00%   0.019   0.715   2.717   0.082   0.597   1.514   1.821
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_009.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.062   0.081   0.093   0.062   0.083   0.093   0.093
           2      16      16   0.00%   0.063   0.147   1.068   0.072   0.084   0.114   1.068
           3      23      23   0.00%   0.063   0.085   0.162   0.070   0.083   0.093   0.098
           5      29      29   0.00%   0.062   0.128   0.386   0.063   0.102   0.216   0.273
          10      27      27   0.00%   0.093   0.487   1.337   0.119   0.318   1.314   1.321
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 8 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in Connection.py, line 594: See the server error log for details
* 5 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in FileStorage.py, line 514: See the server error log for details
* 2 time(s), code: 503::

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