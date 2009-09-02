======================
FunkLoad_ bench report
======================


:date: 2009-09-02 15:11:39
:abstract: Read only load test scenario
           Bench result of ``Readonly.test_ReadOnly``: 
           Read only load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 15:11:39
* Test: ``collective.coreloadtests.tests.test_Readonly.py Readonly.test_ReadOnly``
* Server: http://localhost:8080
* Cycles of concurrent users: [1, 2, 3, 5, 10, 15, 20]
* Cycle duration: 60s
* Sleeptime between request: from 0.0s to 2.0s
* Sleeptime between test case: 1.0s
* Startup delay between thread: 0.2s
* FunkLoad_ version: 1.10.0


Bench content
-------------

The test ``Readonly.test_ReadOnly`` contains: 

* 5 page(s)
* 0 redirect(s)
* 0 link(s)
* 0 image(s)
* 0 XML RPC call(s)

The bench contains:

* 424 tests
* 2189 pages
* 2189 requests


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.133       8       8   0.00%
       2   0.283      17      17   0.00%
       3   0.467      28      28   0.00%
       5   0.750      45      45   0.00%
      10   1.367      82      82   0.00%
      15   1.900     114     114   0.00%
      20   2.167     130     130   0.00%
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
       1   0.717   2.000      43      43   0.00%   0.079   0.103   0.236   0.080   0.099   0.125   0.128
       2   1.383   4.000      83      83   0.00%   0.076   0.115   0.700   0.079   0.096   0.127   0.214
       3   2.433   5.000     146     146   0.00%   0.059   0.109   0.623   0.079   0.097   0.138   0.168
       5   3.850   8.000     231     231   0.00%   0.060   0.125   0.610   0.079   0.105   0.192   0.257
      10   6.967  10.000     418     418   0.00%   0.059   0.229   1.044   0.082   0.175   0.442   0.633
      15   9.867  14.000     592     592   0.00%   0.058   0.327   1.205   0.094   0.257   0.694   0.871
      20  11.267  18.000     676     676   0.00%   0.061   0.594   1.680   0.261   0.529   1.034   1.182
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.717   2.000      43      43   0.00%   0.079   0.103   0.236   0.080   0.099   0.125   0.128
       2   1.383   4.000      83      83   0.00%   0.076   0.115   0.700   0.079   0.096   0.127   0.214
       3   2.433   5.000     146     146   0.00%   0.059   0.109   0.623   0.079   0.097   0.138   0.168
       5   3.850   8.000     231     231   0.00%   0.060   0.125   0.610   0.079   0.105   0.192   0.257
      10   6.967  10.000     418     418   0.00%   0.059   0.229   1.044   0.082   0.175   0.442   0.633
      15   9.867  14.000     592     592   0.00%   0.058   0.327   1.205   0.094   0.257   0.694   0.871
      20  11.267  18.000     676     676   0.00%   0.061   0.594   1.680   0.261   0.529   1.034   1.182
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **20** CUs:

* In page 002 get: /coreloadtests/news took **0.667s**
  `Get /coreloadtests/news`
* In page 001 get: /coreloadtests took **0.612s**
  `Get /coreloadtests`
* In page 004 get: /coreloadtests/folder_listing took **0.584s**
  `Get coreloadtests/folder_listing`
* In page 003 get: /coreloadtests/contact-info took **0.577s**
  `Get /coreloadtests/contact-info`
* In page 005 get: /coreloadtests/sitemap took **0.531s**
  `Get coreloadtests/sitemap`

Page detail stats
-----------------


PAGE 001: Get /coreloadtests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests

     .. image:: request_001.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.095   0.101   0.106   0.095   0.104   0.106   0.106
           2      16      16   0.00%   0.093   0.110   0.242   0.094   0.104   0.106   0.242
           3      28      28   0.00%   0.074   0.107   0.203   0.094   0.104   0.139   0.197
           5      44      44   0.00%   0.086   0.129   0.342   0.094   0.105   0.206   0.273
          10      82      82   0.00%   0.073   0.224   0.853   0.096   0.168   0.460   0.610
          15     115     115   0.00%   0.073   0.374   1.175   0.100   0.312   0.849   0.970
          20     133     133   0.00%   0.074   0.612   1.373   0.302   0.597   0.986   1.162
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/news
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/news

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.109   0.133   0.236   0.109   0.124   0.236   0.236
           2      16      16   0.00%   0.109   0.137   0.245   0.114   0.124   0.214   0.245
           3      30      30   0.00%   0.086   0.140   0.591   0.113   0.121   0.186   0.216
           5      46      46   0.00%   0.083   0.143   0.303   0.104   0.127   0.218   0.257
          10      88      88   0.00%   0.085   0.277   0.857   0.114   0.226   0.578   0.711
          15     117     117   0.00%   0.082   0.362   1.205   0.124   0.285   0.694   0.854
          20     135     135   0.00%   0.124   0.667   1.680   0.339   0.613   1.197   1.309
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Get /coreloadtests/contact-info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/contact-info

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.080   0.088   0.122   0.080   0.082   0.122   0.122
           2      17      17   0.00%   0.076   0.086   0.158   0.080   0.081   0.087   0.158
           3      30      30   0.00%   0.060   0.110   0.623   0.080   0.081   0.159   0.167
           5      48      48   0.00%   0.060   0.101   0.391   0.074   0.081   0.147   0.180
          10      83      83   0.00%   0.061   0.208   0.856   0.080   0.167   0.429   0.481
          15     120     120   0.00%   0.059   0.313   1.127   0.082   0.243   0.688   0.886
          20     139     139   0.00%   0.061   0.577   1.462   0.239   0.505   1.084   1.255
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get coreloadtests/folder_listing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/folder_listing

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.088   0.106   0.132   0.088   0.106   0.132   0.132
           2      17      17   0.00%   0.082   0.124   0.514   0.089   0.102   0.110   0.514
           3      29      29   0.00%   0.090   0.108   0.185   0.096   0.106   0.118   0.127
           5      48      48   0.00%   0.076   0.147   0.610   0.096   0.107   0.251   0.285
          10      83      83   0.00%   0.076   0.235   1.044   0.098   0.188   0.419   0.474
          15     121     121   0.00%   0.075   0.328   1.131   0.100   0.252   0.695   0.816
          20     137     137   0.00%   0.095   0.584   1.375   0.261   0.542   0.995   1.095
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get coreloadtests/sitemap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/sitemap

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.079   0.083   0.099   0.079   0.080   0.099   0.099
           2      17      17   0.00%   0.078   0.121   0.700   0.078   0.080   0.155   0.700
           3      29      29   0.00%   0.059   0.080   0.106   0.075   0.079   0.088   0.099
           5      45      45   0.00%   0.060   0.108   0.545   0.079   0.081   0.158   0.167
          10      82      82   0.00%   0.059   0.199   0.879   0.079   0.156   0.357   0.588
          15     119     119   0.00%   0.058   0.263   0.997   0.079   0.200   0.533   0.816
          20     132     132   0.00%   0.126   0.531   1.232   0.243   0.474   0.964   1.117
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

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