======================
FunkLoad_ bench report
======================


:date: 2009-09-02 14:46:52
:abstract: Heavy write load test scenario
           Bench result of ``Writeheavy.test_WriteHeavy``: 
           Heavy write load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 14:46:52
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

* 112 tests, 14 error(s)
* 1317 pages, 14 error(s)
* 1634 requests, 14 error(s)


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.067       8       8   0.00%
       2   0.133      16      16   0.00%
       3   0.175      21      21   0.00%
       5   0.258      31      31   0.00%
      10   0.183      36      22  38.89%
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
       1   0.742   2.000      89      89   0.00%   0.010   0.200   0.938   0.011   0.098   0.661   0.692
       2   1.492   4.000     179     179   0.00%   0.010   0.268   2.156   0.021   0.110   0.697   0.983
       3   2.100   5.000     252     252   0.00%   0.010   0.272   2.485   0.021   0.126   0.690   1.006
       5   3.108   7.000     373     373   0.00%   0.010   0.483   9.255   0.039   0.204   1.107   1.722
      10   3.417  11.000     424     410   3.30%   0.011   1.363  19.663   0.144   0.590   3.819   5.548
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.942   3.000     113     113   0.00%   0.009   0.158   0.710   0.011   0.104   0.317   0.479
       2   1.892   4.000     227     227   0.00%   0.009   0.211   1.928   0.012   0.116   0.488   0.607
       3   2.642   5.000     317     317   0.00%   0.009   0.216   2.260   0.021   0.131   0.462   0.609
       5   3.908   7.000     469     469   0.00%   0.009   0.384   8.862   0.031   0.225   0.726   1.161
      10   4.233  11.000     508     494   2.76%   0.011   1.438  16.086   0.148   0.631   3.064   4.449
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 008 post: /coreloadtests/Members/leucus/folder-3/portal_factory/Document/document.2009-09-02.3394769716/edit took **1.662s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 007 post: /coreloadtests/Members/leucus/portal_factory/Folder/folder.2009-09-02.3352347085/edit took **1.164s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 006 get: /coreloadtests/Members/rubra/view took **0.415s**
  `Get /coreloadtests/Members/user/view`
* In page 007 redirect: /coreloadtests/Members/leucus/folder-3/ took **0.352s**
  ``
* In page 008 redirect: /coreloadtests/Members/petra/folder-2/fulvus-occidentalis-oleum-rufus-tres took **0.310s**
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
           1       8       8   0.00%   0.094   0.099   0.104   0.094   0.102   0.104   0.104
           2      16      16   0.00%   0.094   0.108   0.153   0.094   0.105   0.135   0.153
           3      21      21   0.00%   0.074   0.137   0.363   0.103   0.106   0.194   0.207
           5      31      31   0.00%   0.074   0.192   0.765   0.094   0.136   0.304   0.556
          10      37      37   0.00%   0.095   0.785   3.503   0.125   0.497   2.039   3.412
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/join_form

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.075   0.080   0.108   0.075   0.076   0.108   0.108
           2      18      18   0.00%   0.055   0.080   0.168   0.055   0.075   0.095   0.168
           3      24      24   0.00%   0.075   0.097   0.230   0.075   0.076   0.151   0.186
           5      35      35   0.00%   0.055   0.156   0.735   0.058   0.092   0.278   0.472
          10      41      41   0.00%   0.077   0.552   3.064   0.107   0.339   1.217   1.375
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/join_form

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.080   0.107   0.170   0.080   0.095   0.170   0.170
           2      17      17   0.00%   0.070   0.112   0.453   0.072   0.089   0.117   0.453
           3      24      24   0.00%   0.060   0.120   0.240   0.079   0.093   0.209   0.217
           5      36      36   0.00%   0.060   0.228   0.895   0.080   0.150   0.585   0.757
          10      44      44   0.00%   0.063   0.512   2.419   0.115   0.352   0.976   2.264
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Post /coreloadtests/login_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/login_form

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.090   0.127   0.231   0.090   0.100   0.231   0.231
           2      16      16   0.00%   0.091   0.174   0.365   0.092   0.146   0.361   0.365
           3      24      24   0.00%   0.090   0.183   0.416   0.091   0.163   0.303   0.350
           5      35      35   0.00%   0.090   0.239   1.150   0.091   0.218   0.358   0.544
          10      42      42   0.00%   0.084   0.629   3.294   0.112   0.423   1.370   2.225
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get /coreloadtests/dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/dashboard

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.114   0.133   0.187   0.114   0.130   0.187   0.187
           2      16      16   0.00%   0.115   0.137   0.305   0.116   0.124   0.169   0.305
           3      24      24   0.00%   0.111   0.145   0.277   0.116   0.128   0.182   0.273
           5      35      35   0.00%   0.112   0.245   0.738   0.117   0.204   0.466   0.630
          10      42      42   0.00%   0.099   0.606   1.770   0.184   0.562   1.249   1.332
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 006: Get /coreloadtests/Members/user/view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/Members/pelagius/view

     .. image:: request_006.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.218   0.227   0.236   0.218   0.226   0.236   0.236
           2      16      16   0.00%   0.210   0.300   0.658   0.214   0.246   0.557   0.658
           3      24      24   0.00%   0.201   0.312   0.690   0.215   0.234   0.601   0.615
           5      35      35   0.00%   0.170   0.415   1.094   0.226   0.346   0.726   0.900
          10      41      41   0.00%   0.238   0.744   2.639   0.363   0.657   1.131   1.274
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/pelagius/createObject?type_name=Folder

     .. image:: request_006.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.010   0.012   0.021   0.010   0.011   0.021   0.021
           2      16      16   0.00%   0.010   0.040   0.164   0.010   0.022   0.093   0.164
           3      24      24   0.00%   0.010   0.028   0.131   0.011   0.021   0.042   0.090
           5      35      35   0.00%   0.010   0.052   0.419   0.011   0.021   0.112   0.190
          10      41      41   0.00%   0.011   0.680   3.378   0.063   0.254   2.372   2.516
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 007: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/pelagius/portal_factory/Folder/folder.2009-09-02.9253710270/edit

     .. image:: request_007.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.290   0.360   0.710   0.290   0.315   0.710   0.710
           2      16      16   0.00%   0.293   0.524   1.572   0.295   0.425   1.075   1.572
           3      23      23   0.00%   0.283   0.421   1.193   0.291   0.314   0.566   1.174
           5      33      33   0.00%   0.282   1.164   8.862   0.306   0.514   2.589   4.130
          10      41      38   7.32%   0.450   2.998  10.843   1.268   2.364   5.032  10.515
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/pelagius/folder-1/

     .. image:: request_007.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.223   0.281   0.642   0.223   0.230   0.642   0.642
           2      16      16   0.00%   0.203   0.253   0.337   0.222   0.254   0.294   0.337
           3      23      23   0.00%   0.223   0.322   0.819   0.228   0.244   0.548   0.767
           5      33      33   0.00%   0.208   0.352   0.827   0.237   0.283   0.591   0.709
          10      38      38   0.00%   0.234   1.386   4.240   0.288   1.323   2.602   3.325
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/pelagius/folder-1/createObject?type_name=Document

     .. image:: request_007.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.010   0.018   0.025   0.010   0.021   0.025   0.025
           2      16      16   0.00%   0.011   0.026   0.105   0.011   0.012   0.068   0.105
           3      22      22   0.00%   0.011   0.039   0.146   0.011   0.021   0.096   0.119
           5      33      33   0.00%   0.011   0.105   0.722   0.011   0.050   0.202   0.441
          10      38      38   0.00%   0.023   1.234   3.070   0.102   1.197   2.627   2.998
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 008: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/pelagius/folder-1/portal_factory/Document/document.2009-09-02.9281345389/edit

     .. image:: request_008.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.449   0.480   0.524   0.449   0.479   0.524   0.524
           2      16      16   0.00%   0.449   0.792   1.928   0.468   0.531   1.817   1.928
           3      21      21   0.00%   0.430   0.839   2.260   0.459   0.544   1.785   2.001
           5      33      33   0.00%   0.484   1.662   7.877   0.490   1.161   2.694   7.369
          10      35      24  31.43%   1.287   7.219  16.086   1.936   5.765  13.661  15.025
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/pelagius/folder-1/officinalis-it-brevis-minor-diplo

     .. image:: request_008.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.189   0.205   0.219   0.189   0.205   0.219   0.219
           2      16      16   0.00%   0.206   0.287   0.719   0.206   0.228   0.543   0.719
           3      21      21   0.00%   0.188   0.224   0.294   0.197   0.218   0.248   0.293
           5      32      32   0.00%   0.192   0.310   1.014   0.208   0.287   0.369   0.557
          10      24      24   0.00%   0.218   1.460   3.577   0.427   1.318   2.675   3.072
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 009: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_009.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.009   0.011   0.021   0.009   0.010   0.021   0.021
           2      16      16   0.00%   0.009   0.020   0.052   0.010   0.011   0.040   0.052
           3      21      21   0.00%   0.009   0.055   0.418   0.009   0.021   0.147   0.191
           5      32      32   0.00%   0.009   0.103   0.442   0.011   0.033   0.349   0.419
          10      22      22   0.00%   0.012   0.861   3.404   0.069   0.566   2.169   2.789
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_009.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.062   0.080   0.087   0.062   0.083   0.087   0.087
           2      16      16   0.00%   0.063   0.126   0.496   0.082   0.092   0.188   0.496
           3      21      21   0.00%   0.073   0.138   0.572   0.078   0.092   0.174   0.515
           5      31      31   0.00%   0.072   0.183   0.556   0.082   0.157   0.347   0.469
          10      22      22   0.00%   0.083   0.776   3.671   0.123   0.420   1.774   2.339
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 8 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in Connection.py, line 594: See the server error log for details
* 5 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in FileStorage.py, line 514: See the server error log for details
* 1 time(s), code: 503::

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