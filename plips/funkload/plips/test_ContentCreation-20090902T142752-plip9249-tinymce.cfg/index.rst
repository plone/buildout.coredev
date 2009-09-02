======================
FunkLoad_ bench report
======================


:date: 2009-09-02 14:27:52
:abstract: Content creation load test scenario
           Bench result of ``Contentcreation.test_ContentCreation``: 
           Content creation load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 14:27:52
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

* 172 tests, 27 error(s)
* 1025 pages, 27 error(s)
* 1496 requests, 27 error(s)


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
       5   0.325      45      39  13.33%
      10   0.267      53      32  39.62%
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
       1   0.683   3.000      82      82   0.00%   0.011   0.278   1.760   0.021   0.098   0.675   0.737
       2   1.308   4.000     157     157   0.00%   0.010   0.331   2.412   0.011   0.094   0.827   1.163
       3   1.808   5.000     217     217   0.00%   0.010   0.440   4.527   0.012   0.132   1.065   1.894
       5   2.183   6.000     268     262   2.24%   0.010   0.842   9.313   0.022   0.257   2.571   3.697
      10   2.333   8.000     301     280   6.98%   0.016   2.006  13.378   0.225   1.595   4.572   5.901
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   1.017   4.000     122     122   0.00%   0.009   0.187   1.760   0.011   0.104   0.431   0.488
       2   1.967   5.000     236     236   0.00%   0.009   0.220   2.201   0.010   0.146   0.473   0.587
       3   2.700   8.000     324     324   0.00%   0.009   0.294   4.298   0.011   0.206   0.600   0.974
       5   3.275   8.000     393     387   1.53%   0.009   0.710   9.964   0.022   0.256   1.403   3.381
      10   3.508   9.000     421     400   4.99%   0.013   1.988  14.793   0.238   1.183   3.479   8.977
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 003 post: /coreloadtests/Members/scvmwqdtp/folder-4/portal_factory/Document/document.2009-09-02.1683976818/edit took **3.019s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 002 post: /coreloadtests/Members/fitgsudna/portal_factory/Folder/folder.2009-09-02.1693176415/edit took **1.664s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 003 redirect: /coreloadtests/Members/scvmwqdtp/folder-4/sinensis-ortho-platy-pachys-glycis took **0.431s**
  ``
* In page 002 redirect: /coreloadtests/Members/fitgsudna/folder-4/ took **0.366s**
  ``
* In page 001 post: /coreloadtests/login_form took **0.280s**
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
           1      14      14   0.00%   0.089   0.233   1.760   0.092   0.102   0.203   1.760
           2      25      25   0.00%   0.080   0.110   0.220   0.088   0.098   0.200   0.211
           3      35      35   0.00%   0.083   0.157   0.477   0.087   0.100   0.366   0.414
           5      45      45   0.00%   0.079   0.280   0.984   0.091   0.234   0.552   0.792
          10      52      52   0.00%   0.110   1.124   3.101   0.333   0.882   2.376   2.659
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/jlasboneuq/createObject?type_name=Folder

     .. image:: request_001.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.011   0.024   0.088   0.011   0.021   0.021   0.088
           2      27      27   0.00%   0.010   0.029   0.205   0.010   0.011   0.062   0.161
           3      38      38   0.00%   0.010   0.087   0.865   0.011   0.021   0.272   0.478
           5      47      47   0.00%   0.010   0.088   0.482   0.011   0.040   0.264   0.362
          10      57      57   0.00%   0.019   0.867   2.703   0.064   0.734   2.062   2.261
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/jlasboneuq/portal_factory/Folder/folder.2009-09-02.7898175922/edit

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.260   0.336   0.656   0.282   0.299   0.515   0.656
           2      27      27   0.00%   0.266   0.473   1.714   0.276   0.296   0.970   1.647
           3      38      38   0.00%   0.285   0.508   1.973   0.295   0.367   0.816   1.416
           5      47      45   4.26%   0.279   1.664   9.920   0.357   0.948   4.033   5.420
          10      62      54  12.90%   0.294   3.301  12.724   0.872   1.994   8.569   9.746
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/jlasboneuq/folder-3/

     .. image:: request_002.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.217   0.286   0.938   0.219   0.243   0.248   0.938
           2      27      27   0.00%   0.214   0.265   0.544   0.219   0.241   0.383   0.386
           3      37      37   0.00%   0.208   0.293   0.772   0.223   0.244   0.462   0.720
           5      45      45   0.00%   0.227   0.366   1.028   0.237   0.294   0.597   0.724
          10      54      54   0.00%   0.264   1.444   3.484   0.427   1.302   2.814   2.911
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/jlasboneuq/folder-3/createObject?type_name=Document

     .. image:: request_002.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      14      14   0.00%   0.011   0.018   0.022   0.011   0.021   0.022   0.022
           2      26      26   0.00%   0.010   0.034   0.184   0.010   0.014   0.088   0.162
           3      36      36   0.00%   0.010   0.068   0.365   0.011   0.026   0.194   0.229
           5      45      45   0.00%   0.010   0.083   0.337   0.011   0.041   0.219   0.240
          10      51      51   0.00%   0.016   1.098   3.250   0.099   0.879   2.095   2.594
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/kibvjqolx/folder-6/portal_factory/Document/document.2009-09-02.7819963604/edit

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.409   0.467   0.693   0.412   0.447   0.539   0.693
           2      26      26   0.00%   0.413   0.661   2.201   0.437   0.460   1.087   1.916
           3      35      35   0.00%   0.445   1.125   4.298   0.453   0.629   2.232   2.519
           5      44      40   9.09%   0.465   3.019   9.964   0.591   2.365   7.325   8.950
          10      46      33  28.26%   0.638   5.965  14.793   1.186   3.749  12.480  13.630
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/kibvjqolx/folder-6/arctos-pedis-cauda-xanthos-dermis

     .. image:: request_003.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.203   0.227   0.355   0.207   0.218   0.227   0.355
           2      26      26   0.00%   0.187   0.274   0.645   0.205   0.221   0.483   0.577
           3      35      35   0.00%   0.187   0.245   0.540   0.190   0.225   0.340   0.393
           5      40      40   0.00%   0.219   0.431   1.143   0.230   0.328   0.914   1.032
          10      33      33   0.00%   0.264   1.698   3.972   0.556   1.383   3.038   3.248
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.009   0.014   0.032   0.009   0.009   0.020   0.032
           2      26      26   0.00%   0.009   0.020   0.163   0.009   0.010   0.032   0.064
           3      35      35   0.00%   0.009   0.045   0.368   0.009   0.018   0.084   0.357
           5      40      40   0.00%   0.009   0.126   1.056   0.010   0.052   0.335   0.569
          10      33      33   0.00%   0.013   0.957   2.125   0.148   0.853   1.835   2.021
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_004.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      13      13   0.00%   0.061   0.082   0.133   0.071   0.081   0.101   0.133
           2      26      26   0.00%   0.061   0.105   0.489   0.066   0.081   0.163   0.207
           3      35      35   0.00%   0.061   0.126   0.401   0.063   0.082   0.254   0.352
           5      40      40   0.00%   0.071   0.215   1.116   0.081   0.151   0.422   0.699
          10      33      33   0.00%   0.105   0.867   3.861   0.121   0.689   2.323   2.805
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 13 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
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