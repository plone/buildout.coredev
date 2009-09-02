======================
FunkLoad_ bench report
======================


:date: 2009-09-02 15:00:43
:abstract: Content creation load test scenario
           Bench result of ``Contentcreation.test_ContentCreation``: 
           Content creation load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 15:00:43
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

* 166 tests, 20 error(s)
* 995 pages, 20 error(s)
* 1459 requests, 20 error(s)


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.108      13      13   0.00%
       2   0.217      26      26   0.00%
       3   0.292      35      35   0.00%
       5   0.350      43      42   2.33%
      10   0.250      49      30  38.78%
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
       1   0.683   3.000      82      82   0.00%   0.011   0.312   4.258   0.021   0.091   0.665   0.747
       2   1.325   4.000     159     159   0.00%   0.010   0.303   2.518   0.011   0.100   0.715   0.936
       3   1.808   4.000     217     217   0.00%   0.010   0.432   3.639   0.012   0.111   1.039   1.669
       5   2.150   6.000     259     258   0.39%   0.010   1.082  11.692   0.022   0.252   3.035   5.843
      10   2.158   8.000     278     259   6.83%   0.010   2.282  13.701   0.185   1.638   5.541   6.878
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   1.017   3.000     122     122   0.00%   0.009   0.210   4.258   0.011   0.103   0.437   0.502
       2   1.983   5.000     238     238   0.00%   0.009   0.202   2.310   0.010   0.147   0.462   0.582
       3   2.708   6.000     325     325   0.00%   0.009   0.288   3.373   0.012   0.207   0.595   0.944
       5   3.217   8.000     386     385   0.26%   0.010   0.745  11.456   0.021   0.248   1.817   3.623
      10   3.233  10.000     388     369   4.90%   0.010   2.176  14.232   0.195   1.359   4.140   9.708
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 003 post: /coreloadtests/Members/dgftonwmr/folder-5/portal_factory/Document/document.2009-09-02.1457572994/edit took **3.387s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 002 post: /coreloadtests/Members/gxolmfiwpj/portal_factory/Folder/folder.2009-09-02.1491580119/edit took **1.830s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 003 redirect: /coreloadtests/Members/dgftonwmr/folder-5/parvus-tinctorius-di-montanus-zygos took **0.393s**
  ``
* In page 002 redirect: /coreloadtests/Members/scvmwqdtp/folder-7/ took **0.325s**
  ``
* In page 001 post: /coreloadtests/login_form took **0.263s**
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
           1      14      14   0.00%   0.086   0.396   4.258   0.090   0.101   0.116   4.258
           2      26      26   0.00%   0.069   0.119   0.228   0.089   0.100   0.201   0.215
           3      35      35   0.00%   0.070   0.181   0.841   0.089   0.101   0.309   0.543
           5      42      42   0.00%   0.070   0.263   0.758   0.091   0.228   0.493   0.551
          10      51      51   0.00%   0.093   1.138   4.079   0.239   0.919   2.051   2.946
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/iorxnuykc/createObject?type_name=Folder

     .. image:: request_001.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.011   0.025   0.103   0.011   0.021   0.022   0.103
           2      27      27   0.00%   0.010   0.028   0.147   0.010   0.020   0.067   0.131
           3      37      37   0.00%   0.010   0.042   0.365   0.010   0.021   0.094   0.173
           5      46      46   0.00%   0.010   0.095   1.111   0.011   0.037   0.188   0.322
          10      50      50   0.00%   0.010   1.033   4.457   0.035   1.067   2.035   2.484
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/iorxnuykc/portal_factory/Folder/folder.2009-09-02.7619500398/edit

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.291   0.359   0.845   0.291   0.313   0.502   0.845
           2      27      27   0.00%   0.271   0.322   0.713   0.288   0.298   0.336   0.504
           3      37      37   0.00%   0.284   0.699   3.373   0.293   0.358   1.442   3.000
           5      45      44   2.22%   0.293   1.830  10.377   0.318   0.877   4.575   7.633
          10      57      50  12.28%   0.594   3.887  10.936   0.973   2.666   9.784  10.461
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/iorxnuykc/folder-4/

     .. image:: request_002.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.223   0.287   0.948   0.224   0.238   0.254   0.948
           2      27      27   0.00%   0.221   0.263   0.449   0.233   0.244   0.332   0.366
           3      37      37   0.00%   0.214   0.277   0.656   0.224   0.247   0.357   0.437
           5      43      43   0.00%   0.232   0.325   1.084   0.241   0.271   0.441   0.532
          10      49      49   0.00%   0.243   1.747   4.235   0.750   1.433   2.877   4.024
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/iorxnuykc/folder-4/createObject?type_name=Document

     .. image:: request_002.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.011   0.020   0.022   0.011   0.021   0.022   0.022
           2      27      27   0.00%   0.010   0.056   0.342   0.011   0.021   0.182   0.189
           3      37      37   0.00%   0.010   0.042   0.258   0.011   0.021   0.107   0.197
           5      42      42   0.00%   0.010   0.074   0.432   0.011   0.036   0.180   0.218
          10      47      47   0.00%   0.012   1.137   3.990   0.111   0.945   2.456   3.926
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/fitgsudna/folder-7/portal_factory/Document/document.2009-09-02.7547813922/edit

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.421   0.474   0.666   0.428   0.447   0.538   0.666
           2      26      26   0.00%   0.430   0.684   2.310   0.448   0.515   0.891   1.967
           3      36      36   0.00%   0.436   0.879   2.467   0.462   0.589   2.224   2.417
           5      42      42   0.00%   0.477   3.387  11.456   0.552   2.275   7.843   8.524
          10      43      31  27.91%   1.033   6.061  14.232   1.884   3.617  13.035  13.716
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/fitgsudna/folder-7/pteron-volans-fuscus-caulos-australis

     .. image:: request_003.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.203   0.227   0.362   0.205   0.217   0.231   0.362
           2      26      26   0.00%   0.186   0.223   0.416   0.190   0.215   0.259   0.281
           3      36      36   0.00%   0.197   0.283   0.740   0.208   0.244   0.431   0.575
           5      42      42   0.00%   0.200   0.393   1.395   0.221   0.289   0.725   0.925
          10      31      31   0.00%   0.232   1.805   4.826   0.503   1.895   3.075   3.350
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.009   0.014   0.042   0.009   0.010   0.020   0.042
           2      26      26   0.00%   0.009   0.038   0.279   0.009   0.009   0.215   0.221
           3      35      35   0.00%   0.009   0.075   0.595   0.009   0.020   0.168   0.374
           5      42      42   0.00%   0.010   0.103   0.633   0.011   0.049   0.321   0.389
          10      30      30   0.00%   0.016   1.164   3.726   0.124   1.189   2.551   2.614
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_004.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.061   0.080   0.126   0.061   0.081   0.081   0.126
           2      26      26   0.00%   0.060   0.094   0.372   0.062   0.081   0.105   0.146
           3      35      35   0.00%   0.062   0.102   0.256   0.071   0.082   0.156   0.229
           5      42      42   0.00%   0.062   0.228   0.720   0.081   0.166   0.457   0.570
          10      30      30   0.00%   0.063   0.751   1.931   0.124   0.693   1.670   1.753
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 5 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in Connection.py, line 594: See the server error log for details
* 15 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
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