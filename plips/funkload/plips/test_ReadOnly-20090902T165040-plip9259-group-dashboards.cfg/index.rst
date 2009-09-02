======================
FunkLoad_ bench report
======================


:date: 2009-09-02 16:50:40
:abstract: Read only load test scenario
           Bench result of ``Readonly.test_ReadOnly``: 
           Read only load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 16:50:40
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

* 421 tests
* 2165 pages
* 2165 requests


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.150       9       9   0.00%
       2   0.283      17      17   0.00%
       3   0.433      26      26   0.00%
       5   0.733      44      44   0.00%
      10   1.367      82      82   0.00%
      15   1.900     114     114   0.00%
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
       1   0.750   2.000      45      45   0.00%   0.079   0.101   0.234   0.080   0.100   0.120   0.124
       2   1.483   3.000      89      89   0.00%   0.060   0.119   0.811   0.080   0.105   0.140   0.207
       3   2.267   4.000     136     136   0.00%   0.060   0.107   0.687   0.080   0.104   0.124   0.154
       5   3.733   8.000     224     224   0.00%   0.060   0.131   0.772   0.080   0.107   0.195   0.239
      10   7.100  11.000     426     426   0.00%   0.059   0.216   1.347   0.083   0.171   0.381   0.501
      15   9.833  15.000     590     590   0.00%   0.059   0.375   1.659   0.120   0.314   0.711   0.956
      20  10.917  16.000     655     655   0.00%   0.060   0.631   1.732   0.241   0.577   1.120   1.268
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.750   2.000      45      45   0.00%   0.079   0.101   0.234   0.080   0.100   0.120   0.124
       2   1.483   3.000      89      89   0.00%   0.060   0.119   0.811   0.080   0.105   0.140   0.207
       3   2.267   4.000     136     136   0.00%   0.060   0.107   0.687   0.080   0.104   0.124   0.154
       5   3.733   8.000     224     224   0.00%   0.060   0.131   0.772   0.080   0.107   0.195   0.239
      10   7.100  11.000     426     426   0.00%   0.059   0.216   1.347   0.083   0.171   0.381   0.501
      15   9.833  15.000     590     590   0.00%   0.059   0.375   1.659   0.120   0.314   0.711   0.956
      20  10.917  16.000     655     655   0.00%   0.060   0.631   1.732   0.241   0.577   1.120   1.268
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **20** CUs:

* In page 002 get: /coreloadtests/news took **0.715s**
  `Get /coreloadtests/news`
* In page 004 get: /coreloadtests/folder_listing took **0.640s**
  `Get coreloadtests/folder_listing`
* In page 003 get: /coreloadtests/contact-info took **0.632s**
  `Get /coreloadtests/contact-info`
* In page 001 get: /coreloadtests took **0.620s**
  `Get /coreloadtests`
* In page 005 get: /coreloadtests/sitemap took **0.549s**
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
           1       9       9   0.00%   0.094   0.102   0.107   0.094   0.104   0.107   0.107
           2      17      17   0.00%   0.094   0.108   0.148   0.094   0.105   0.131   0.148
           3      26      26   0.00%   0.075   0.111   0.256   0.094   0.105   0.115   0.199
           5      42      42   0.00%   0.074   0.138   0.765   0.093   0.104   0.180   0.286
          10      82      82   0.00%   0.075   0.240   0.877   0.103   0.185   0.450   0.600
          15     115     115   0.00%   0.074   0.416   1.659   0.112   0.320   0.856   1.002
          20     128     128   0.00%   0.075   0.620   1.534   0.185   0.582   1.133   1.249
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/news
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/news

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.113   0.130   0.234   0.113   0.115   0.234   0.234
           2      18      18   0.00%   0.107   0.126   0.235   0.110   0.117   0.148   0.235
           3      29      29   0.00%   0.109   0.121   0.154   0.114   0.119   0.128   0.130
           5      45      45   0.00%   0.084   0.164   0.772   0.094   0.124   0.256   0.303
          10      88      88   0.00%   0.084   0.218   0.815   0.113   0.201   0.370   0.444
          15     119     119   0.00%   0.084   0.385   1.617   0.137   0.350   0.697   0.970
          20     133     133   0.00%   0.136   0.715   1.624   0.352   0.688   1.195   1.272
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Get /coreloadtests/contact-info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/contact-info

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.080   0.084   0.111   0.080   0.080   0.111   0.111
           2      18      18   0.00%   0.061   0.120   0.811   0.080   0.081   0.082   0.811
           3      29      29   0.00%   0.060   0.082   0.127   0.064   0.081   0.096   0.096
           5      47      47   0.00%   0.061   0.105   0.406   0.071   0.082   0.181   0.186
          10      87      87   0.00%   0.061   0.189   0.795   0.080   0.140   0.405   0.463
          15     117     117   0.00%   0.061   0.366   1.258   0.089   0.284   0.864   0.992
          20     134     134   0.00%   0.062   0.632   1.732   0.252   0.572   1.170   1.384
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get coreloadtests/folder_listing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/folder_listing

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.095   0.105   0.122   0.095   0.107   0.122   0.122
           2      18      18   0.00%   0.096   0.143   0.782   0.097   0.107   0.111   0.782
           3      26      26   0.00%   0.077   0.113   0.192   0.097   0.107   0.168   0.175
           5      46      46   0.00%   0.077   0.130   0.239   0.096   0.109   0.214   0.237
          10      85      85   0.00%   0.076   0.240   1.006   0.097   0.178   0.385   0.645
          15     120     120   0.00%   0.077   0.384   1.317   0.118   0.333   0.709   0.994
          20     130     130   0.00%   0.102   0.640   1.455   0.265   0.579   1.125   1.309
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get coreloadtests/sitemap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/sitemap

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.079   0.084   0.120   0.079   0.080   0.120   0.120
           2      18      18   0.00%   0.060   0.099   0.225   0.079   0.081   0.207   0.225
           3      26      26   0.00%   0.074   0.107   0.687   0.079   0.080   0.113   0.115
           5      44      44   0.00%   0.060   0.117   0.699   0.079   0.081   0.184   0.215
          10      84      84   0.00%   0.059   0.194   1.347   0.080   0.154   0.297   0.431
          15     119     119   0.00%   0.059   0.325   1.241   0.126   0.278   0.557   0.808
          20     130     130   0.00%   0.060   0.549   1.268   0.222   0.520   0.941   1.056
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