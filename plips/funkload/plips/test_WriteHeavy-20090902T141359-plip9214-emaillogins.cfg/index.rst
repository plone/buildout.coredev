======================
FunkLoad_ bench report
======================


:date: 2009-09-02 14:13:59
:abstract: Heavy write load test scenario
           Bench result of ``Writeheavy.test_WriteHeavy``: 
           Heavy write load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 14:13:59
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

* 115 tests, 20 error(s)
* 1299 pages, 20 error(s)
* 1601 requests, 20 error(s)


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.058       8       7  12.50%
       2   0.125      15      15   0.00%
       3   0.175      22      21   4.55%
       5   0.242      30      29   3.33%
      10   0.192      40      23  42.50%
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
       1   0.742   3.000      90      89   1.11%   0.010   0.196   0.896   0.021   0.106   0.562   0.666
       2   1.408   3.000     169     169   0.00%   0.011   0.246   2.098   0.021   0.124   0.634   0.739
       3   2.142   5.000     258     257   0.39%   0.010   0.280   2.595   0.021   0.116   0.731   0.947
       5   2.958   7.000     356     355   0.28%   0.010   0.492   9.955   0.047   0.184   1.050   1.790
      10   3.408   9.000     426     409   3.99%   0.013   1.301  16.234   0.183   0.655   3.450   5.075
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.942   3.000     113     112   0.88%   0.007   0.158   0.613   0.021   0.113   0.287   0.472
       2   1.783   5.000     214     214   0.00%   0.011   0.194   1.892   0.021   0.146   0.381   0.503
       3   2.692   6.000     323     322   0.31%   0.009   0.225   2.223   0.021   0.121   0.469   0.640
       5   3.708   8.000     445     444   0.22%   0.009   0.417  10.673   0.033   0.211   0.677   1.433
      10   4.217  10.000     506     489   3.36%   0.013   1.369  14.003   0.183   0.671   2.770   5.075
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 008 post: /coreloadtests/Members/cyanos/folder-2/portal_factory/Document/document.2009-09-02.3404225006/edit took **2.380s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 007 post: /coreloadtests/Members/novaeseelandiae/portal_factory/Folder/folder.2009-09-02.3487765952/edit took **0.939s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 004 post: /coreloadtests/login_form took **0.458s**
  `Post /coreloadtests/login_form`
* In page 008 redirect: /coreloadtests/Members/cyanos/folder-2/arvensis-albus-arctos-punctatus-tomentosus took **0.370s**
  ``
* In page 007 redirect: /coreloadtests/Members/novaeseelandiae/folder/ took **0.356s**
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
           1       8       8   0.00%   0.095   0.104   0.107   0.095   0.105   0.107   0.107
           2      15      15   0.00%   0.094   0.130   0.265   0.095   0.106   0.233   0.265
           3      22      22   0.00%   0.093   0.116   0.366   0.094   0.104   0.114   0.145
           5      30      30   0.00%   0.077   0.227   0.694   0.095   0.158   0.590   0.677
          10      38      38   0.00%   0.096   0.621   3.010   0.129   0.357   1.704   2.933
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/join_form

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.074   0.079   0.112   0.074   0.075   0.112   0.112
           2      16      16   0.00%   0.055   0.096   0.284   0.074   0.075   0.147   0.284
           3      24      24   0.00%   0.075   0.135   0.444   0.075   0.077   0.292   0.336
           5      34      34   0.00%   0.055   0.144   0.492   0.075   0.083   0.359   0.392
          10      44      44   0.00%   0.063   0.467   1.844   0.154   0.312   1.022   1.130
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/join_form

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.080   0.119   0.264   0.080   0.103   0.264   0.264
           2      16      16   0.00%   0.072   0.144   0.407   0.091   0.106   0.369   0.407
           3      25      25   0.00%   0.074   0.121   0.470   0.080   0.094   0.185   0.207
           5      35      35   0.00%   0.060   0.178   0.527   0.080   0.122   0.362   0.448
          10      47      47   0.00%   0.082   0.874   2.754   0.144   0.677   1.712   2.082
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Post /coreloadtests/login_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/login_form

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.106   0.235   0.562   0.106   0.206   0.562   0.562
           2      16      16   0.00%   0.200   0.261   0.517   0.203   0.216   0.482   0.517
           3      25      25   0.00%   0.088   0.204   0.628   0.089   0.205   0.349   0.369
           5      35      35   0.00%   0.070   0.458   2.924   0.090   0.251   1.433   1.555
          10      47      46   2.13%   0.234   1.408   8.822   0.322   0.888   2.951   5.075
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get /coreloadtests/dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/dashboard

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.007   0.108   0.159   0.007   0.115   0.159   0.159
           2      16      16   0.00%   0.110   0.138   0.234   0.113   0.124   0.227   0.234
           3      25      25   0.00%   0.113   0.158   0.384   0.114   0.120   0.296   0.346
           5      35      35   0.00%   0.107   0.187   0.405   0.117   0.153   0.330   0.385
          10      45      45   0.00%   0.110   0.682   1.728   0.288   0.604   1.218   1.418
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/acl_users/credentials_cookie_auth/require_login?came_from=http%3A//localhost%3A8080/coreloadtests/dashboard

     .. image:: request_005.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       1       1   0.00%   0.097   0.097   0.097   0.097   0.097   0.097   0.097
          10       2       2   0.00%   1.212   1.220   1.229   1.212   1.229   1.229   1.229
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 006: Get /coreloadtests/Members/user/view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/Members/flora/view

     .. image:: request_006.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       8  11.11%   0.187   0.209   0.220   0.187   0.210   0.220   0.220
           2      15      15   0.00%   0.197   0.227   0.304   0.209   0.220   0.257   0.304
           3      24      24   0.00%   0.208   0.295   0.783   0.210   0.232   0.455   0.657
           5      33      33   0.00%   0.198   0.343   0.789   0.220   0.304   0.545   0.598
          10      43      39   9.30%   0.265   0.869   3.018   0.331   0.627   2.131   2.311
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/flora/createObject?type_name=Folder

     .. image:: request_006.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.010   0.017   0.022   0.010   0.021   0.022   0.022
           2      15      15   0.00%   0.011   0.021   0.056   0.011   0.021   0.031   0.056
           3      24      24   0.00%   0.010   0.036   0.241   0.010   0.021   0.080   0.171
           5      33      33   0.00%   0.010   0.097   0.386   0.011   0.047   0.264   0.372
          10      39      39   0.00%   0.047   0.631   2.568   0.079   0.413   1.490   2.227
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 007: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/flora/portal_factory/Folder/folder.2009-09-02.9580495910/edit

     .. image:: request_007.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.282   0.287   0.295   0.282   0.286   0.295   0.295
           2      15      15   0.00%   0.259   0.310   0.464   0.279   0.289   0.381   0.464
           3      24      23   4.17%   0.283   0.412   1.479   0.283   0.303   0.587   0.640
           5      31      31   0.00%   0.278   0.939   5.464   0.298   0.483   1.645   3.536
          10      37      33  10.81%   0.626   3.094  11.870   0.773   1.957   7.805   9.661
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/flora/folder/

     .. image:: request_007.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.210   0.279   0.613   0.210   0.241   0.613   0.613
           2      15      15   0.00%   0.222   0.279   0.612   0.232   0.244   0.334   0.612
           3      23      23   0.00%   0.222   0.308   0.618   0.225   0.257   0.466   0.474
           5      31      31   0.00%   0.221   0.356   0.986   0.232   0.309   0.490   0.738
          10      32      32   0.00%   0.344   1.213   2.933   0.414   1.040   2.507   2.632
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/vitis/folder/createObject?type_name=Document

     .. image:: request_007.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       7       7   0.00%   0.011   0.019   0.039   0.011   0.013   0.039   0.039
           2      15      15   0.00%   0.011   0.041   0.297   0.011   0.022   0.076   0.297
           3      23      23   0.00%   0.011   0.061   0.278   0.012   0.021   0.208   0.244
           5      31      31   0.00%   0.010   0.093   0.876   0.011   0.029   0.237   0.337
          10      32      32   0.00%   0.013   0.534   2.142   0.114   0.356   1.084   1.964
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 008: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/vitis/folder/portal_factory/Document/document.2009-09-02.9459224508/edit

     .. image:: request_008.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       7       7   0.00%   0.413   0.462   0.488   0.413   0.472   0.488   0.488
           2      15      15   0.00%   0.443   0.708   1.892   0.452   0.503   1.187   1.892
           3      21      21   0.00%   0.444   0.912   2.223   0.469   0.657   1.942   1.976
           5      30      29   3.33%   0.469   2.380  10.673   0.533   0.966   6.193   9.710
          10      31      23  25.81%   1.407   7.207  14.003   1.657   6.752  13.502  13.689
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/vitis/folder/chilensis-pedis-montanus-ennea-brachy

     .. image:: request_008.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       7       7   0.00%   0.184   0.205   0.221   0.184   0.205   0.221   0.221
           2      15      15   0.00%   0.185   0.224   0.274   0.204   0.218   0.271   0.274
           3      21      21   0.00%   0.197   0.301   1.040   0.207   0.228   0.548   0.577
           5      29      29   0.00%   0.196   0.370   1.144   0.213   0.287   0.823   0.846
          10      23      23   0.00%   0.293   1.070   3.033   0.315   0.833   2.231   2.490
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 009: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_009.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       7       7   0.00%   0.011   0.020   0.025   0.011   0.021   0.025   0.025
           2      15      15   0.00%   0.011   0.019   0.065   0.011   0.012   0.028   0.065
           3      21      21   0.00%   0.009   0.054   0.455   0.009   0.021   0.102   0.119
           5      29      29   0.00%   0.009   0.057   0.263   0.010   0.025   0.191   0.241
          10      23      23   0.00%   0.013   0.684   2.540   0.036   0.467   2.299   2.501
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_009.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       7       7   0.00%   0.072   0.076   0.087   0.072   0.072   0.087   0.087
           2      15      15   0.00%   0.072   0.134   0.623   0.072   0.085   0.240   0.623
           3      21      21   0.00%   0.063   0.092   0.328   0.071   0.082   0.101   0.110
           5      29      29   0.00%   0.064   0.133   0.536   0.072   0.095   0.206   0.238
          10      23      23   0.00%   0.112   0.513   2.492   0.119   0.334   1.151   1.284
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 3 time(s), code: 404::

    No traceback.

* 5 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in Connection.py, line 594: See the server error log for details
* 8 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in FileStorage.py, line 514: See the server error log for details
* 4 time(s), code: 503::

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