======================
FunkLoad_ bench report
======================


:date: 2009-09-02 15:44:06
:abstract: Read only load test scenario
           Bench result of ``Readonly.test_ReadOnly``: 
           Read only load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 15:44:06
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
* 2181 pages
* 2181 requests


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.150       9       9   0.00%
       2   0.283      17      17   0.00%
       3   0.450      27      27   0.00%
       5   0.733      44      44   0.00%
      10   1.417      85      85   0.00%
      15   1.883     113     113   0.00%
      20   2.150     129     129   0.00%
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
       1   0.750   2.000      45      45   0.00%   0.071   0.101   0.236   0.079   0.104   0.116   0.123
       2   1.467   3.000      88      88   0.00%   0.059   0.099   0.179   0.079   0.103   0.117   0.124
       3   2.267   5.000     136     136   0.00%   0.060   0.110   0.652   0.079   0.103   0.135   0.181
       5   3.817   7.000     229     229   0.00%   0.058   0.126   0.793   0.079   0.104   0.183   0.221
      10   7.150  11.000     429     429   0.00%   0.058   0.205   1.052   0.081   0.169   0.348   0.438
      15   9.550  15.000     573     573   0.00%   0.058   0.326   1.436   0.103   0.263   0.626   0.852
      20  11.350  18.000     681     681   0.00%   0.060   0.592   2.136   0.217   0.540   1.094   1.268
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.750   2.000      45      45   0.00%   0.071   0.101   0.236   0.079   0.104   0.116   0.123
       2   1.467   3.000      88      88   0.00%   0.059   0.099   0.179   0.079   0.103   0.117   0.124
       3   2.267   5.000     136     136   0.00%   0.060   0.110   0.652   0.079   0.103   0.135   0.181
       5   3.817   7.000     229     229   0.00%   0.058   0.126   0.793   0.079   0.104   0.183   0.221
      10   7.150  11.000     429     429   0.00%   0.058   0.205   1.052   0.081   0.169   0.348   0.438
      15   9.550  15.000     573     573   0.00%   0.058   0.326   1.436   0.103   0.263   0.626   0.852
      20  11.350  18.000     681     681   0.00%   0.060   0.592   2.136   0.217   0.540   1.094   1.268
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **20** CUs:

* In page 002 get: /coreloadtests/news took **0.672s**
  `Get /coreloadtests/news`
* In page 001 get: /coreloadtests took **0.603s**
  `Get /coreloadtests`
* In page 004 get: /coreloadtests/folder_listing took **0.591s**
  `Get coreloadtests/folder_listing`
* In page 003 get: /coreloadtests/contact-info took **0.583s**
  `Get /coreloadtests/contact-info`
* In page 005 get: /coreloadtests/sitemap took **0.514s**
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
           1       9       9   0.00%   0.094   0.109   0.157   0.094   0.104   0.157   0.157
           2      17      17   0.00%   0.093   0.106   0.164   0.094   0.103   0.108   0.164
           3      26      26   0.00%   0.073   0.106   0.212   0.093   0.103   0.126   0.159
           5      47      47   0.00%   0.075   0.165   0.755   0.093   0.105   0.221   0.718
          10      83      83   0.00%   0.083   0.224   1.052   0.103   0.184   0.390   0.439
          15     111     111   0.00%   0.076   0.343   1.018   0.115   0.285   0.645   0.837
          20     132     132   0.00%   0.102   0.603   1.585   0.248   0.551   1.094   1.266
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/news
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/news

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.106   0.127   0.236   0.106   0.114   0.236   0.236
           2      19      19   0.00%   0.113   0.119   0.179   0.113   0.114   0.124   0.179
           3      28      28   0.00%   0.082   0.127   0.234   0.084   0.124   0.168   0.219
           5      48      48   0.00%   0.083   0.156   0.793   0.103   0.124   0.219   0.312
          10      87      87   0.00%   0.083   0.245   0.969   0.113   0.201   0.406   0.453
          15     112     112   0.00%   0.083   0.338   1.314   0.124   0.278   0.623   0.852
          20     135     135   0.00%   0.094   0.672   2.136   0.289   0.637   1.167   1.322
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Get /coreloadtests/contact-info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/contact-info

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.071   0.083   0.109   0.071   0.080   0.109   0.109
           2      18      18   0.00%   0.059   0.085   0.169   0.077   0.080   0.097   0.169
           3      28      28   0.00%   0.060   0.114   0.652   0.080   0.081   0.181   0.220
           5      46      46   0.00%   0.060   0.085   0.203   0.060   0.080   0.111   0.123
          10      86      86   0.00%   0.059   0.200   0.909   0.080   0.162   0.326   0.534
          15     118     118   0.00%   0.060   0.333   1.271   0.082   0.263   0.668   0.882
          20     139     139   0.00%   0.060   0.583   1.545   0.181   0.533   1.180   1.239
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get coreloadtests/folder_listing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/folder_listing

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.096   0.105   0.121   0.096   0.106   0.121   0.121
           2      17      17   0.00%   0.086   0.104   0.117   0.093   0.106   0.117   0.117
           3      27      27   0.00%   0.086   0.108   0.188   0.094   0.106   0.130   0.145
           5      44      44   0.00%   0.075   0.120   0.198   0.096   0.106   0.174   0.188
          10      87      87   0.00%   0.075   0.198   0.885   0.096   0.158   0.310   0.363
          15     117     117   0.00%   0.075   0.365   1.436   0.121   0.273   0.792   1.014
          20     138     138   0.00%   0.086   0.591   1.502   0.232   0.540   1.094   1.303
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get coreloadtests/sitemap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/sitemap

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.071   0.082   0.111   0.071   0.079   0.111   0.111
           2      17      17   0.00%   0.078   0.080   0.086   0.078   0.079   0.084   0.086
           3      27      27   0.00%   0.061   0.092   0.175   0.070   0.080   0.133   0.135
           5      44      44   0.00%   0.058   0.101   0.250   0.071   0.080   0.172   0.232
          10      86      86   0.00%   0.058   0.157   0.884   0.079   0.134   0.276   0.306
          15     115     115   0.00%   0.058   0.253   1.061   0.079   0.190   0.499   0.665
          20     137     137   0.00%   0.060   0.514   1.498   0.162   0.478   0.965   1.267
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