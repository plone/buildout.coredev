======================
FunkLoad_ bench report
======================


:date: 2009-09-02 17:12:41
:abstract: Content creation load test scenario
           Bench result of ``Contentcreation.test_ContentCreation``: 
           Content creation load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 17:12:41
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

* 161 tests, 19 error(s)
* 965 pages, 19 error(s)
* 1419 requests, 19 error(s)


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.092      11      11   0.00%
       2   0.225      27      27   0.00%
       3   0.292      35      35   0.00%
       5   0.333      42      40   4.76%
      10   0.242      46      29  36.96%
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
       1   0.550   2.000      66      66   0.00%   0.009   0.574  19.422   0.010   0.101   0.689   0.951
       2   1.375   3.000     165     165   0.00%   0.009   0.305   2.188   0.010   0.099   0.729   0.931
       3   1.775   5.000     213     213   0.00%   0.009   0.408   3.443   0.011   0.103   1.028   1.567
       5   2.133   6.000     258     256   0.78%   0.009   1.108  11.465   0.023   0.314   3.554   5.149
      10   2.050   7.000     263     246   6.46%   0.009   2.595  12.865   0.259   2.133   5.978   7.539
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.825   3.000      99      99   0.00%   0.008   0.382  19.422   0.009   0.104   0.451   0.578
       2   2.058   5.000     247     247   0.00%   0.008   0.204   1.954   0.009   0.108   0.456   0.603
       3   2.658   6.000     319     319   0.00%   0.007   0.272   3.214   0.010   0.164   0.552   0.907
       5   3.217   8.000     386     384   0.52%   0.008   0.790  11.670   0.023   0.290   2.014   3.787
      10   3.067   9.000     368     351   4.62%   0.009   2.420  16.550   0.291   1.664   4.915   9.103
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 003 post: /coreloadtests/Members/nobfxcywzq/folder-12/portal_factory/Document/document.2009-09-02.0501325844/edit took **3.463s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 002 post: /coreloadtests/Members/hlquedvwio/portal_factory/Folder/folder.2009-09-02.0474087612/edit took **1.703s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 003 redirect: /coreloadtests/Members/depotrswf/folder-13/petra-obscurus-campus-xanthos-pratensis took **0.472s**
  ``
* In page 002 redirect: /coreloadtests/Members/hlquedvwio/folder-8/ took **0.390s**
  ``
* In page 001 post: /coreloadtests/login_form took **0.353s**
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
           1      11      11   0.00%   0.090   1.877  19.422   0.091   0.102   0.324  19.422
           2      26      26   0.00%   0.076   0.109   0.385   0.089   0.099   0.115   0.153
           3      34      34   0.00%   0.070   0.176   0.554   0.090   0.103   0.449   0.525
           5      41      41   0.00%   0.081   0.353   1.324   0.101   0.218   0.814   0.921
          10      44      44   0.00%   0.194   1.680   4.747   0.291   1.534   3.177   3.730
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/ejnckdsypo/createObject?type_name=Folder

     .. image:: request_001.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      11      11   0.00%   0.009   0.022   0.095   0.009   0.011   0.030   0.095
           2      28      28   0.00%   0.009   0.047   0.342   0.009   0.011   0.232   0.305
           3      37      37   0.00%   0.009   0.027   0.166   0.009   0.019   0.066   0.098
           5      43      43   0.00%   0.010   0.112   0.515   0.013   0.064   0.266   0.342
          10      50      50   0.00%   0.009   1.037   2.845   0.122   0.889   2.474   2.589
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/ejnckdsypo/portal_factory/Folder/folder.2009-09-02.6730032624/edit

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      11      11   0.00%   0.309   0.429   1.293   0.325   0.334   0.395   1.293
           2      28      28   0.00%   0.268   0.378   1.145   0.294   0.314   0.564   0.923
           3      36      36   0.00%   0.278   0.724   3.100   0.302   0.397   1.835   2.746
           5      44      44   0.00%   0.306   1.703  10.355   0.318   0.742   3.702   4.918
          10      51      46   9.80%   0.544   4.238  14.589   1.176   3.123   8.845  10.800
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/ejnckdsypo/folder-14/

     .. image:: request_002.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      11      11   0.00%   0.207   0.279   0.715   0.225   0.239   0.257   0.715
           2      28      28   0.00%   0.233   0.286   0.786   0.239   0.254   0.287   0.590
           3      36      36   0.00%   0.227   0.322   1.498   0.237   0.263   0.354   0.769
           5      44      44   0.00%   0.235   0.390   1.151   0.253   0.314   0.659   0.915
          10      46      46   0.00%   0.411   2.008   4.376   0.989   1.905   3.104   3.190
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/ejnckdsypo/folder-14/createObject?type_name=Document

     .. image:: request_002.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      11      11   0.00%   0.009   0.012   0.021   0.010   0.010   0.020   0.021
           2      28      28   0.00%   0.009   0.035   0.254   0.010   0.020   0.104   0.104
           3      36      36   0.00%   0.009   0.051   0.251   0.010   0.020   0.166   0.227
           5      44      44   0.00%   0.009   0.166   0.990   0.012   0.083   0.469   0.633
          10      46      46   0.00%   0.012   1.397   4.499   0.203   1.437   3.163   3.397
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/ejnckdsypo/folder-14/portal_factory/Document/document.2009-09-02.6765071528/edit

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      11      11   0.00%   0.424   0.489   0.720   0.440   0.460   0.578   0.720
           2      28      28   0.00%   0.431   0.593   1.954   0.438   0.476   0.857   0.875
           3      35      35   0.00%   0.430   0.764   3.214   0.458   0.489   1.341   2.070
           5      44      42   4.55%   0.478   3.463  11.670   0.511   2.305   8.388  10.844
          10      43      31  27.91%   1.075   6.469  16.550   1.572   4.842  12.688  14.740
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/ejnckdsypo/folder-14/so-maximus-ennea-tetra-dodeca

     .. image:: request_003.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      11      11   0.00%   0.203   0.236   0.387   0.209   0.225   0.240   0.387
           2      27      27   0.00%   0.200   0.254   0.742   0.213   0.234   0.260   0.310
           3      35      35   0.00%   0.213   0.266   0.615   0.214   0.235   0.311   0.574
           5      42      42   0.00%   0.217   0.472   2.033   0.229   0.340   0.957   1.037
          10      30      30   0.00%   0.320   1.696   4.729   0.422   1.338   3.667   3.824
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      11      11   0.00%   0.008   0.012   0.030   0.008   0.008   0.019   0.030
           2      27      27   0.00%   0.008   0.021   0.239   0.008   0.009   0.033   0.068
           3      35      35   0.00%   0.007   0.029   0.244   0.008   0.009   0.084   0.102
           5      42      42   0.00%   0.008   0.130   0.923   0.009   0.037   0.246   0.711
          10      29      29   0.00%   0.017   1.004   3.060   0.033   0.646   2.792   2.794
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_004.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      11      11   0.00%   0.063   0.086   0.126   0.076   0.083   0.102   0.126
           2      27      27   0.00%   0.062   0.095   0.344   0.062   0.082   0.141   0.182
           3      35      35   0.00%   0.062   0.095   0.319   0.075   0.083   0.127   0.146
           5      42      42   0.00%   0.064   0.202   0.686   0.079   0.151   0.395   0.467
          10      29      29   0.00%   0.097   1.170   2.886   0.125   1.034   2.709   2.807
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 5 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in Connection.py, line 594: See the server error log for details
* 14 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
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