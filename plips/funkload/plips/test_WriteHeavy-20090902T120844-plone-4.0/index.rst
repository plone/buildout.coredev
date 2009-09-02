======================
FunkLoad_ bench report
======================


:date: 2009-09-02 12:08:44
:abstract: Heavy write load test scenario
           Bench result of ``Writeheavy.test_WriteHeavy``: 
           Heavy write load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 12:08:44
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

* 117 tests, 16 error(s)
* 1355 pages, 16 error(s)
* 1678 requests, 16 error(s)


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
       5   0.267      32      32   0.00%
      10   0.192      39      23  41.03%
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
       1   0.808   3.000      97      97   0.00%   0.009   0.199   0.853   0.010   0.104   0.581   0.664
       2   1.508   4.000     181     181   0.00%   0.009   0.232   2.331   0.011   0.105   0.628   0.673
       3   2.108   4.000     253     253   0.00%   0.009   0.278   3.919   0.019   0.121   0.681   0.910
       5   3.108   7.000     373     373   0.00%   0.009   0.511   6.759   0.044   0.224   1.144   2.128
      10   3.625  11.000     451     435   3.55%   0.009   1.185  11.753   0.133   0.735   3.207   3.961
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   1.017   3.000     122     122   0.00%   0.009   0.158   0.581   0.010   0.117   0.287   0.459
       2   1.908   5.000     229     229   0.00%   0.008   0.184   1.639   0.010   0.126   0.429   0.480
       3   2.658   6.000     319     319   0.00%   0.008   0.220   3.919   0.011   0.126   0.468   0.633
       5   3.925   7.000     471     471   0.00%   0.008   0.404   6.426   0.031   0.227   0.711   1.440
      10   4.475  11.000     537     521   2.98%   0.009   1.324  15.110   0.130   0.730   2.423   4.297
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 008 post: /coreloadtests/Members/chloreus/folder/portal_factory/Document/document.2009-09-02.8274915667/edit took **2.080s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 007 post: /coreloadtests/Members/hortensis/portal_factory/Folder/folder.2009-09-02.8288520163/edit took **0.762s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 004 post: /coreloadtests/login_form took **0.606s**
  `Post /coreloadtests/login_form`
* In page 008 redirect: /coreloadtests/Members/chloreus/folder/archaeos-indicus-phyton-brevis-chloreus took **0.349s**
  ``
* In page 007 redirect: /coreloadtests/Members/hortensis/folder/ took **0.325s**
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
           1       8       8   0.00%   0.090   0.094   0.106   0.090   0.092   0.106   0.106
           2      15      15   0.00%   0.072   0.101   0.211   0.080   0.099   0.104   0.211
           3      22      22   0.00%   0.086   0.131   0.312   0.091   0.105   0.199   0.207
           5      32      32   0.00%   0.081   0.196   0.537   0.090   0.152   0.344   0.444
          10      39      39   0.00%   0.092   0.853   2.423   0.150   0.542   2.152   2.242
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/join_form

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.072   0.077   0.107   0.072   0.073   0.107   0.107
           2      17      17   0.00%   0.063   0.094   0.214   0.068   0.074   0.213   0.214
           3      25      25   0.00%   0.068   0.107   0.259   0.073   0.075   0.188   0.228
           5      35      35   0.00%   0.053   0.179   0.535   0.074   0.142   0.446   0.484
          10      43      43   0.00%   0.053   0.479   2.634   0.096   0.251   1.057   1.798
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/join_form

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.090   0.115   0.247   0.090   0.100   0.247   0.247
           2      17      17   0.00%   0.074   0.101   0.154   0.078   0.099   0.142   0.154
           3      25      25   0.00%   0.058   0.135   0.521   0.078   0.106   0.208   0.377
           5      35      35   0.00%   0.071   0.220   0.711   0.079   0.139   0.544   0.668
          10      46      46   0.00%   0.078   0.586   2.030   0.144   0.474   1.288   1.617
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Post /coreloadtests/login_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/login_form

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.202   0.250   0.581   0.202   0.209   0.581   0.581
           2      17      17   0.00%   0.086   0.242   0.480   0.090   0.210   0.457   0.480
           3      24      24   0.00%   0.075   0.417   3.919   0.090   0.206   0.753   0.861
           5      35      35   0.00%   0.087   0.606   2.498   0.089   0.314   1.969   2.128
          10      46      46   0.00%   0.127   1.414   6.483   0.228   0.978   3.240   4.271
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get /coreloadtests/dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/dashboard

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.115   0.125   0.161   0.115   0.123   0.161   0.161
           2      17      17   0.00%   0.115   0.178   0.610   0.117   0.126   0.288   0.610
           3      23      23   0.00%   0.116   0.147   0.416   0.117   0.126   0.194   0.256
           5      35      35   0.00%   0.088   0.271   1.225   0.117   0.153   0.457   0.882
          10      46      46   0.00%   0.117   0.812   2.521   0.179   0.864   1.547   1.594
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 006: Get /coreloadtests/Members/user/view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/Members/saurus/view

     .. image:: request_006.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.206   0.216   0.223   0.206   0.216   0.223   0.223
           2      17      17   0.00%   0.177   0.222   0.297   0.206   0.214   0.270   0.297
           3      23      23   0.00%   0.198   0.286   0.651   0.207   0.221   0.534   0.570
           5      35      35   0.00%   0.187   0.315   0.624   0.207   0.260   0.521   0.585
          10      46      46   0.00%   0.180   0.909   2.761   0.302   0.725   1.887   2.629
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/saurus/createObject?type_name=Folder

     .. image:: request_006.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.009   0.011   0.020   0.009   0.010   0.020   0.020
           2      17      17   0.00%   0.009   0.012   0.025   0.009   0.010   0.024   0.025
           3      23      23   0.00%   0.009   0.023   0.113   0.010   0.010   0.071   0.088
           5      35      35   0.00%   0.009   0.080   0.678   0.010   0.025   0.283   0.424
          10      45      45   0.00%   0.009   0.583   2.245   0.032   0.334   1.558   2.053
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 007: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/saurus/portal_factory/Folder/folder.2009-09-02.4414616434/edit

     .. image:: request_007.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.274   0.281   0.289   0.274   0.280   0.289   0.289
           2      16      16   0.00%   0.266   0.428   1.639   0.277   0.292   0.582   1.639
           3      22      22   0.00%   0.265   0.414   1.043   0.271   0.335   0.633   0.687
           5      34      34   0.00%   0.273   0.762   3.045   0.291   0.544   1.947   2.273
          10      44      38  13.64%   0.511   3.472  11.613   0.890   2.022   8.939   9.881
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/saurus/folder/

     .. image:: request_007.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.218   0.265   0.573   0.218   0.223   0.573   0.573
           2      16      16   0.00%   0.211   0.236   0.356   0.211   0.230   0.267   0.356
           3      22      22   0.00%   0.210   0.249   0.343   0.220   0.241   0.297   0.312
           5      34      34   0.00%   0.228   0.325   0.793   0.241   0.271   0.449   0.769
          10      37      37   0.00%   0.249   1.199   2.517   0.421   1.093   2.309   2.335
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/saurus/folder/createObject?type_name=Document

     .. image:: request_007.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.010   0.010   0.011   0.010   0.010   0.011   0.011
           2      16      16   0.00%   0.009   0.038   0.166   0.009   0.020   0.101   0.166
           3      22      22   0.00%   0.009   0.046   0.335   0.009   0.020   0.090   0.121
           5      33      33   0.00%   0.010   0.107   0.361   0.010   0.049   0.283   0.346
          10      37      37   0.00%   0.010   0.676   2.154   0.087   0.366   1.699   1.984
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 008: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/saurus/folder/portal_factory/Document/document.2009-09-02.4445262650/edit

     .. image:: request_008.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.428   0.453   0.470   0.428   0.459   0.470   0.470
           2      16      16   0.00%   0.429   0.583   1.639   0.434   0.455   0.811   1.639
           3      22      22   0.00%   0.449   0.760   2.424   0.455   0.586   1.531   2.101
           5      32      32   0.00%   0.427   2.080   6.426   0.477   1.095   5.592   5.752
          10      35      25  28.57%   0.505   5.356  15.110   1.027   2.663  12.234  13.426
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/so/folder/nothos-sativus-argentatus-rostra-indicus

     .. image:: request_008.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.193   0.202   0.214   0.193   0.202   0.214   0.214
           2      16      16   0.00%   0.184   0.247   0.692   0.184   0.207   0.339   0.692
           3      22      22   0.00%   0.194   0.287   0.930   0.199   0.223   0.490   0.654
           5      32      32   0.00%   0.199   0.349   0.747   0.210   0.324   0.571   0.668
          10      25      25   0.00%   0.268   1.038   2.933   0.324   0.730   2.108   2.571
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 009: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_009.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.009   0.009   0.010   0.009   0.009   0.010   0.010
           2      16      16   0.00%   0.008   0.015   0.067   0.008   0.010   0.040   0.067
           3      22      22   0.00%   0.008   0.024   0.105   0.009   0.010   0.055   0.094
           5      32      32   0.00%   0.008   0.077   0.345   0.010   0.037   0.193   0.207
          10      24      24   0.00%   0.011   0.502   2.172   0.040   0.304   1.808   1.925
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_009.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.060   0.074   0.084   0.060   0.076   0.084   0.084
           2      16      16   0.00%   0.060   0.083   0.231   0.061   0.074   0.084   0.231
           3      22      22   0.00%   0.060   0.077   0.122   0.060   0.078   0.096   0.108
           5      32      32   0.00%   0.059   0.156   0.589   0.068   0.109   0.321   0.411
          10      24      24   0.00%   0.086   0.505   1.790   0.093   0.271   1.323   1.449
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 5 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in Connection.py, line 594: See the server error log for details
* 11 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
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