======================
FunkLoad_ bench report
======================


:date: 2009-09-02 15:33:04
:abstract: Content creation load test scenario
           Bench result of ``Contentcreation.test_ContentCreation``: 
           Content creation load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 15:33:04
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

* 171 tests, 19 error(s)
* 1040 pages, 19 error(s)
* 1527 requests, 19 error(s)


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.100      12      12   0.00%
       2   0.225      27      27   0.00%
       3   0.317      38      38   0.00%
       5   0.367      46      44   4.35%
      10   0.258      48      31  35.42%
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
       1   0.633   3.000      76      76   0.00%   0.009   0.363   8.084   0.009   0.095   0.670   0.781
       2   1.375   4.000     165     165   0.00%   0.009   0.289   1.728   0.010   0.096   0.750   0.841
       3   1.925   4.000     231     231   0.00%   0.009   0.419   8.798   0.012   0.129   0.928   1.284
       5   2.358   6.000     285     283   0.70%   0.009   0.867  10.593   0.030   0.248   2.634   3.540
      10   2.217   8.000     283     266   6.01%   0.012   2.329  16.583   0.250   1.677   5.050   6.147
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.942   3.000     113     113   0.00%   0.007   0.244   8.084   0.009   0.102   0.448   0.535
       2   2.058   6.000     247     247   0.00%   0.007   0.193   1.485   0.009   0.131   0.465   0.526
       3   2.900   6.000     348     348   0.00%   0.008   0.278   8.582   0.012   0.186   0.573   0.787
       5   3.533   9.000     424     422   0.47%   0.008   0.615  10.121   0.024   0.256   1.275   2.807
      10   3.292  10.000     395     378   4.30%   0.009   2.168  15.010   0.269   1.471   3.563   9.930
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 003 post: /coreloadtests/Members/ozpmrhwgj/folder-2/portal_factory/Document/document.2009-09-02.0748684274/edit took **2.728s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 002 post: /coreloadtests/Members/ktojzrqvsh/portal_factory/Folder/folder.2009-09-02.0878741788/edit took **1.170s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 002 redirect: /coreloadtests/Members/ktojzrqvsh/folder-4/ took **0.407s**
  ``
* In page 003 redirect: /coreloadtests/Members/ozpmrhwgj/folder-2/cristatus-maculatus-bradus-octa-cauda took **0.403s**
  ``
* In page 001 post: /coreloadtests/login_form took **0.277s**
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
           1      13      13   0.00%   0.083   0.713   8.084   0.086   0.102   0.112   8.084
           2      27      27   0.00%   0.088   0.123   0.443   0.089   0.093   0.202   0.288
           3      37      37   0.00%   0.068   0.158   0.478   0.089   0.109   0.331   0.422
           5      46      46   0.00%   0.068   0.277   1.055   0.090   0.207   0.559   0.676
          10      51      51   0.00%   0.222   1.356   2.928   0.403   1.193   2.710   2.782
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/gmtazeirk/createObject?type_name=Folder

     .. image:: request_001.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.009   0.018   0.102   0.009   0.010   0.020   0.102
           2      28      28   0.00%   0.009   0.026   0.216   0.009   0.010   0.075   0.118
           3      38      38   0.00%   0.010   0.059   0.474   0.010   0.025   0.148   0.203
           5      49      49   0.00%   0.009   0.091   0.515   0.012   0.053   0.218   0.267
          10      53      53   0.00%   0.012   0.792   2.357   0.072   0.708   1.877   2.185
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/gmtazeirk/portal_factory/Folder/folder.2009-09-02.7021505500/edit

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.279   0.377   0.859   0.285   0.300   0.547   0.859
           2      28      28   0.00%   0.276   0.411   1.485   0.282   0.311   0.644   0.791
           3      39      39   0.00%   0.261   0.562   1.979   0.289   0.363   1.174   1.827
           5      51      51   0.00%   0.280   1.170   5.191   0.327   0.764   2.807   3.649
          10      54      51   5.56%   0.810   3.115  12.545   1.272   2.106   6.822   9.735
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/gmtazeirk/folder-3/

     .. image:: request_002.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.220   0.289   0.944   0.222   0.239   0.246   0.944
           2      28      28   0.00%   0.221   0.280   0.585   0.232   0.250   0.406   0.531
           3      39      39   0.00%   0.222   0.307   0.722   0.233   0.261   0.549   0.614
           5      51      51   0.00%   0.226   0.407   1.203   0.246   0.299   0.717   0.946
          10      50      50   0.00%   0.287   1.795   4.066   0.609   1.883   2.943   3.007
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/gmtazeirk/folder-3/createObject?type_name=Document

     .. image:: request_002.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.009   0.011   0.020   0.009   0.010   0.018   0.020
           2      28      28   0.00%   0.009   0.034   0.171   0.010   0.011   0.131   0.156
           3      39      39   0.00%   0.009   0.039   0.484   0.010   0.020   0.069   0.146
           5      49      49   0.00%   0.009   0.121   0.500   0.012   0.083   0.307   0.324
          10      49      49   0.00%   0.028   1.073   3.002   0.109   0.986   2.126   2.715
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/gipxztjlqk/folder-6/portal_factory/Document/document.2009-09-02.6972085950/edit

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      12      12   0.00%   0.435   0.460   0.550   0.443   0.451   0.473   0.550
           2      27      27   0.00%   0.379   0.493   0.749   0.434   0.468   0.625   0.739
           3      39      39   0.00%   0.433   0.902   8.582   0.440   0.546   1.684   2.199
           5      46      44   4.35%   0.485   2.728  10.121   0.571   1.940   6.824   8.007
          10      45      31  31.11%   0.925   7.193  15.010   2.082   5.753  13.198  13.673
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/gipxztjlqk/folder-6/cephalus-deca-domesticus-nothos-notos

     .. image:: request_003.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      12      12   0.00%   0.187   0.222   0.357   0.205   0.209   0.227   0.357
           2      27      27   0.00%   0.193   0.246   0.705   0.208   0.226   0.284   0.291
           3      39      39   0.00%   0.186   0.289   0.697   0.208   0.241   0.519   0.691
           5      44      44   0.00%   0.196   0.403   1.202   0.237   0.325   0.760   0.807
          10      31      31   0.00%   0.394   1.524   3.035   0.730   1.452   2.580   2.591
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      12      12   0.00%   0.007   0.012   0.028   0.008   0.009   0.019   0.028
           2      27      27   0.00%   0.007   0.034   0.267   0.008   0.009   0.115   0.147
           3      39      39   0.00%   0.008   0.050   0.298   0.008   0.026   0.134   0.169
           5      44      44   0.00%   0.008   0.111   1.566   0.008   0.028   0.172   0.331
          10      31      31   0.00%   0.009   1.024   2.840   0.109   0.908   2.323   2.815
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_004.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      12      12   0.00%   0.060   0.080   0.135   0.061   0.079   0.086   0.135
           2      27      27   0.00%   0.060   0.091   0.218   0.061   0.080   0.152   0.198
           3      39      39   0.00%   0.061   0.125   0.810   0.062   0.082   0.249   0.362
           5      44      44   0.00%   0.062   0.204   0.756   0.072   0.158   0.443   0.506
          10      31      31   0.00%   0.101   1.028   2.939   0.136   0.732   2.361   2.741
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 7 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in Connection.py, line 594: See the server error log for details
* 12 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
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