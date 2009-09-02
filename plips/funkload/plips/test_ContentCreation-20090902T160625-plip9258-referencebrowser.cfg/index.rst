======================
FunkLoad_ bench report
======================


:date: 2009-09-02 16:06:25
:abstract: Content creation load test scenario
           Bench result of ``Contentcreation.test_ContentCreation``: 
           Content creation load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 16:06:25
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

* 165 tests, 19 error(s)
* 995 pages, 19 error(s)
* 1459 requests, 19 error(s)


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
       5   0.342      42      41   2.38%
      10   0.258      49      31  36.73%
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
       1   0.667   2.000      80      80   0.00%   0.010   0.407  11.837   0.010   0.093   0.678   0.784
       2   1.317   4.000     158     158   0.00%   0.010   0.284   2.042   0.011   0.100   0.694   0.790
       3   1.817   5.000     218     218   0.00%   0.010   0.447   4.557   0.011   0.132   1.148   1.860
       5   2.167   6.000     261     260   0.38%   0.010   1.061  10.104   0.025   0.257   3.693   4.842
      10   2.167   8.000     278     260   6.47%   0.014   2.306  11.236   0.251   1.486   6.075   7.500
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.992   3.000     119     119   0.00%   0.009   0.273  11.837   0.010   0.101   0.440   0.528
       2   1.975   5.000     237     237   0.00%   0.009   0.190   1.825   0.011   0.104   0.453   0.492
       3   2.717   6.000     326     326   0.00%   0.008   0.299   4.327   0.011   0.198   0.609   0.951
       5   3.250   9.000     390     389   0.26%   0.009   0.733   9.892   0.021   0.252   1.855   3.715
      10   3.225  11.000     387     369   4.65%   0.014   2.206  14.806   0.202   1.301   4.637   8.924
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 003 post: /coreloadtests/Members/tjbzrmfkyi/folder-6/portal_factory/Document/document.2009-09-02.0822817346/edit took **3.261s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 002 post: /coreloadtests/Members/depotrswf/portal_factory/Folder/folder.2009-09-02.0866300623/edit took **1.718s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 003 redirect: /coreloadtests/Members/tjbzrmfkyi/folder-6/hexa-maculatus-punctatus-cola-pelagius took **0.397s**
  ``
* In page 002 redirect: /coreloadtests/Members/depotrswf/folder-9/ took **0.378s**
  ``
* In page 001 post: /coreloadtests/login_form took **0.326s**
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
           1      14      14   0.00%   0.089   0.937  11.837   0.089   0.101   0.114  11.837
           2      26      26   0.00%   0.069   0.116   0.291   0.090   0.101   0.165   0.275
           3      35      35   0.00%   0.072   0.152   0.483   0.090   0.106   0.246   0.369
           5      41      41   0.00%   0.091   0.326   1.159   0.103   0.244   0.587   0.679
          10      49      49   0.00%   0.125   1.420   3.916   0.276   1.147   3.334   3.789
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/wmgqvcdao/createObject?type_name=Folder

     .. image:: request_001.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.010   0.016   0.093   0.010   0.011   0.011   0.093
           2      26      26   0.00%   0.011   0.029   0.131   0.011   0.020   0.047   0.107
           3      37      37   0.00%   0.010   0.042   0.294   0.010   0.016   0.156   0.227
           5      45      45   0.00%   0.010   0.084   0.390   0.015   0.051   0.218   0.239
          10      54      54   0.00%   0.014   0.705   4.216   0.077   0.549   1.603   2.615
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/yobhqaeflg/portal_factory/Folder/folder.2009-09-02.6972030436/edit

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.281   0.377   0.845   0.296   0.319   0.548   0.845
           2      27      27   0.00%   0.291   0.353   0.809   0.293   0.310   0.563   0.569
           3      38      38   0.00%   0.283   0.671   3.235   0.298   0.374   1.734   2.827
           5      45      44   2.22%   0.282   1.718   8.664   0.338   0.948   4.060   5.064
          10      54      48  11.11%   0.491   4.116  12.282   1.083   3.325  10.380  11.811
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/yobhqaeflg/folder-10/

     .. image:: request_002.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.225   0.309   0.947   0.226   0.245   0.455   0.947
           2      27      27   0.00%   0.215   0.280   0.745   0.227   0.251   0.319   0.490
           3      38      38   0.00%   0.224   0.364   0.951   0.231   0.269   0.710   0.821
           5      44      44   0.00%   0.245   0.378   1.006   0.255   0.329   0.532   0.579
          10      46      46   0.00%   0.275   1.855   4.361   0.453   1.660   3.622   4.105
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/yobhqaeflg/folder-10/createObject?type_name=Document

     .. image:: request_002.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.010   0.012   0.022   0.010   0.011   0.011   0.022
           2      27      27   0.00%   0.010   0.056   0.484   0.011   0.018   0.142   0.287
           3      38      38   0.00%   0.010   0.049   0.234   0.011   0.021   0.198   0.209
           5      44      44   0.00%   0.010   0.128   1.060   0.011   0.053   0.394   0.525
          10      45      45   0.00%   0.026   1.290   4.703   0.197   1.225   2.513   3.104
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/yobhqaeflg/folder-10/portal_factory/Document/document.2009-09-02.6994365415/edit

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.410   0.452   0.553   0.415   0.440   0.528   0.553
           2      26      26   0.00%   0.416   0.541   1.825   0.430   0.465   0.579   0.937
           3      35      35   0.00%   0.454   0.994   4.327   0.462   0.601   2.152   2.492
           5      43      43   0.00%   0.481   3.261   9.892   0.580   2.835   6.676   9.281
          10      44      32  27.27%   1.020   6.188  14.806   1.394   4.140  12.153  13.360
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/yobhqaeflg/folder-10/echinus-dermis-it-occidentalis-arctos

     .. image:: request_003.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.195   0.229   0.340   0.212   0.221   0.237   0.340
           2      26      26   0.00%   0.195   0.221   0.239   0.210   0.220   0.236   0.237
           3      35      35   0.00%   0.195   0.264   0.708   0.208   0.238   0.351   0.398
           5      43      43   0.00%   0.212   0.397   1.296   0.222   0.285   0.721   0.971
          10      32      32   0.00%   0.270   1.935   4.841   0.531   1.835   3.442   4.191
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.009   0.013   0.042   0.009   0.009   0.020   0.042
           2      26      26   0.00%   0.009   0.017   0.057   0.009   0.012   0.033   0.034
           3      35      35   0.00%   0.008   0.037   0.211   0.009   0.011   0.099   0.161
           5      43      43   0.00%   0.009   0.091   0.595   0.010   0.039   0.245   0.364
          10      32      32   0.00%   0.017   0.867   3.932   0.093   0.794   2.004   2.438
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_004.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.067   0.083   0.130   0.072   0.080   0.090   0.130
           2      26      26   0.00%   0.062   0.089   0.367   0.063   0.076   0.093   0.121
           3      35      35   0.00%   0.063   0.116   0.349   0.073   0.088   0.189   0.266
           5      42      42   0.00%   0.063   0.186   0.639   0.083   0.144   0.398   0.480
          10      31      31   0.00%   0.078   0.601   2.218   0.151   0.453   1.142   1.756
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 11 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
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