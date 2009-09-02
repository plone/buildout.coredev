======================
FunkLoad_ bench report
======================


:date: 2009-09-02 14:05:54
:abstract: Read only load test scenario
           Bench result of ``Readonly.test_ReadOnly``: 
           Read only load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 14:05:54
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

* 434 tests
* 2206 pages
* 2206 requests


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.167      10      10   0.00%
       2   0.300      18      18   0.00%
       3   0.467      28      28   0.00%
       5   0.733      44      44   0.00%
      10   1.400      84      84   0.00%
      15   1.917     115     115   0.00%
      20   2.250     135     135   0.00%
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
       1   0.850   2.000      51      51   0.00%   0.057   0.107   0.575   0.078   0.099   0.123   0.126
       2   1.517   4.000      91      91   0.00%   0.057   0.101   0.449   0.078   0.100   0.122   0.124
       3   2.333   5.000     140     140   0.00%   0.057   0.113   0.447   0.078   0.104   0.172   0.194
       5   3.750   7.000     225     225   0.00%   0.057   0.120   0.575   0.077   0.105   0.184   0.198
      10   7.100  11.000     426     426   0.00%   0.057   0.189   0.693   0.080   0.151   0.366   0.421
      15   9.817  14.000     589     589   0.00%   0.058   0.324   1.094   0.117   0.275   0.590   0.739
      20  11.400  18.000     684     684   0.00%   0.057   0.566   1.437   0.244   0.548   0.915   1.011
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.850   2.000      51      51   0.00%   0.057   0.107   0.575   0.078   0.099   0.123   0.126
       2   1.517   4.000      91      91   0.00%   0.057   0.101   0.449   0.078   0.100   0.122   0.124
       3   2.333   5.000     140     140   0.00%   0.057   0.113   0.447   0.078   0.104   0.172   0.194
       5   3.750   7.000     225     225   0.00%   0.057   0.120   0.575   0.077   0.105   0.184   0.198
      10   7.100  11.000     426     426   0.00%   0.057   0.189   0.693   0.080   0.151   0.366   0.421
      15   9.817  14.000     589     589   0.00%   0.058   0.324   1.094   0.117   0.275   0.590   0.739
      20  11.400  18.000     684     684   0.00%   0.057   0.566   1.437   0.244   0.548   0.915   1.011
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **20** CUs:

* In page 004 get: /coreloadtests/folder_listing took **0.605s**
  `Get coreloadtests/folder_listing`
* In page 001 get: /coreloadtests took **0.582s**
  `Get /coreloadtests`
* In page 002 get: /coreloadtests/news took **0.568s**
  `Get /coreloadtests/news`
* In page 003 get: /coreloadtests/contact-info took **0.553s**
  `Get /coreloadtests/contact-info`
* In page 005 get: /coreloadtests/sitemap took **0.519s**
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
           1      10      10   0.00%   0.093   0.100   0.106   0.094   0.104   0.106   0.106
           2      18      18   0.00%   0.094   0.100   0.105   0.094   0.104   0.104   0.105
           3      27      27   0.00%   0.073   0.132   0.447   0.093   0.104   0.191   0.205
           5      43      43   0.00%   0.073   0.126   0.494   0.088   0.104   0.176   0.189
          10      82      82   0.00%   0.073   0.198   0.499   0.094   0.170   0.357   0.404
          15     113     113   0.00%   0.078   0.360   1.094   0.135   0.332   0.658   0.785
          20     135     135   0.00%   0.103   0.582   1.437   0.245   0.552   0.995   1.126
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/news
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/news

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      11      11   0.00%   0.113   0.161   0.575   0.113   0.123   0.126   0.575
           2      19      19   0.00%   0.102   0.140   0.449   0.102   0.122   0.228   0.449
           3      29      29   0.00%   0.101   0.132   0.231   0.103   0.123   0.194   0.202
           5      46      46   0.00%   0.081   0.151   0.575   0.102   0.123   0.210   0.265
          10      84      84   0.00%   0.082   0.230   0.636   0.114   0.180   0.421   0.489
          15     118     118   0.00%   0.112   0.384   1.049   0.145   0.364   0.662   0.789
          20     137     137   0.00%   0.083   0.568   1.234   0.270   0.588   0.820   0.961
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Get /coreloadtests/contact-info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/contact-info

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      10      10   0.00%   0.080   0.086   0.123   0.080   0.081   0.123   0.123
           2      18      18   0.00%   0.080   0.082   0.094   0.080   0.081   0.084   0.094
           3      28      28   0.00%   0.060   0.107   0.205   0.079   0.083   0.168   0.185
           5      47      47   0.00%   0.059   0.108   0.516   0.077   0.081   0.175   0.184
          10      88      88   0.00%   0.062   0.174   0.693   0.080   0.136   0.320   0.392
          15     120     120   0.00%   0.066   0.285   1.012   0.083   0.242   0.493   0.704
          20     141     141   0.00%   0.073   0.553   1.303   0.259   0.519   0.873   0.951
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get coreloadtests/folder_listing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/folder_listing

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      10      10   0.00%   0.075   0.103   0.130   0.095   0.105   0.130   0.130
           2      18      18   0.00%   0.095   0.105   0.119   0.095   0.105   0.109   0.119
           3      28      28   0.00%   0.086   0.110   0.197   0.095   0.105   0.131   0.189
           5      45      45   0.00%   0.075   0.118   0.202   0.095   0.105   0.174   0.197
          10      87      87   0.00%   0.075   0.218   0.659   0.095   0.187   0.391   0.420
          15     121     121   0.00%   0.085   0.325   1.030   0.142   0.270   0.622   0.725
          20     136     136   0.00%   0.087   0.605   1.284   0.271   0.592   0.954   1.035
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get coreloadtests/sitemap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/sitemap

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      10      10   0.00%   0.057   0.079   0.110   0.077   0.078   0.110   0.110
           2      18      18   0.00%   0.057   0.078   0.089   0.076   0.078   0.082   0.089
           3      28      28   0.00%   0.057   0.082   0.167   0.058   0.078   0.093   0.147
           5      44      44   0.00%   0.057   0.095   0.231   0.058   0.078   0.156   0.172
          10      85      85   0.00%   0.057   0.125   0.569   0.065   0.096   0.194   0.306
          15     117     117   0.00%   0.058   0.269   0.828   0.100   0.232   0.494   0.615
          20     135     135   0.00%   0.057   0.519   1.245   0.189   0.493   0.863   0.980
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