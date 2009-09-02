======================
FunkLoad_ bench report
======================


:date: 2009-09-02 13:33:07
:abstract: Read only load test scenario
           Bench result of ``Readonly.test_ReadOnly``: 
           Read only load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 13:33:07
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

* 436 tests
* 2241 pages
* 2241 requests


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.150       9       9   0.00%
       2   0.300      18      18   0.00%
       3   0.450      27      27   0.00%
       5   0.717      43      43   0.00%
      10   1.417      85      85   0.00%
      15   1.983     119     119   0.00%
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
       1   0.783   2.000      47      47   0.00%   0.070   0.097   0.228   0.076   0.101   0.111   0.112
       2   1.483   3.000      89      89   0.00%   0.060   0.099   0.450   0.077   0.093   0.111   0.119
       3   2.367   5.000     142     142   0.00%   0.056   0.098   0.444   0.077   0.092   0.116   0.128
       5   3.667   6.000     220     220   0.00%   0.055   0.123   0.541   0.077   0.102   0.215   0.256
      10   7.133  13.000     428     428   0.00%   0.057   0.190   0.713   0.078   0.160   0.355   0.466
      15  10.067  15.000     604     604   0.00%   0.056   0.283   1.121   0.102   0.252   0.526   0.598
      20  11.850  20.000     711     711   0.00%   0.056   0.521   1.370   0.200   0.492   0.891   0.978
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.783   2.000      47      47   0.00%   0.070   0.097   0.228   0.076   0.101   0.111   0.112
       2   1.483   3.000      89      89   0.00%   0.060   0.099   0.450   0.077   0.093   0.111   0.119
       3   2.367   5.000     142     142   0.00%   0.056   0.098   0.444   0.077   0.092   0.116   0.128
       5   3.667   6.000     220     220   0.00%   0.055   0.123   0.541   0.077   0.102   0.215   0.256
      10   7.133  13.000     428     428   0.00%   0.057   0.190   0.713   0.078   0.160   0.355   0.466
      15  10.067  15.000     604     604   0.00%   0.056   0.283   1.121   0.102   0.252   0.526   0.598
      20  11.850  20.000     711     711   0.00%   0.056   0.521   1.370   0.200   0.492   0.891   0.978
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **20** CUs:

* In page 002 get: /coreloadtests/news took **0.607s**
  `Get /coreloadtests/news`
* In page 004 get: /coreloadtests/folder_listing took **0.534s**
  `Get coreloadtests/folder_listing`
* In page 003 get: /coreloadtests/contact-info took **0.521s**
  `Get /coreloadtests/contact-info`
* In page 001 get: /coreloadtests took **0.517s**
  `Get /coreloadtests`
* In page 005 get: /coreloadtests/sitemap took **0.427s**
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
           1       9       9   0.00%   0.088   0.096   0.102   0.088   0.101   0.102   0.102
           2      17      17   0.00%   0.073   0.095   0.105   0.080   0.101   0.102   0.105
           3      27      27   0.00%   0.070   0.094   0.112   0.090   0.091   0.104   0.104
           5      43      43   0.00%   0.070   0.146   0.541   0.090   0.101   0.232   0.334
          10      82      82   0.00%   0.070   0.178   0.713   0.090   0.162   0.280   0.378
          15     117     117   0.00%   0.071   0.309   0.722   0.108   0.298   0.560   0.598
          20     138     138   0.00%   0.100   0.517   1.092   0.165   0.485   0.884   0.960
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/news
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/news

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      10      10   0.00%   0.109   0.122   0.228   0.109   0.110   0.228   0.228
           2      18      18   0.00%   0.099   0.115   0.208   0.100   0.110   0.120   0.208
           3      30      30   0.00%   0.079   0.131   0.444   0.099   0.112   0.200   0.260
           5      46      46   0.00%   0.080   0.138   0.437   0.089   0.111   0.235   0.277
          10      84      84   0.00%   0.079   0.203   0.579   0.100   0.173   0.394   0.477
          15     121     121   0.00%   0.079   0.320   0.966   0.121   0.277   0.547   0.639
          20     138     138   0.00%   0.083   0.607   1.370   0.240   0.559   1.061   1.172
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Get /coreloadtests/contact-info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/contact-info

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      10      10   0.00%   0.074   0.080   0.107   0.077   0.077   0.107   0.107
           2      18      18   0.00%   0.060   0.078   0.091   0.076   0.078   0.081   0.091
           3      29      29   0.00%   0.057   0.080   0.116   0.076   0.077   0.088   0.097
           5      44      44   0.00%   0.067   0.099   0.231   0.077   0.078   0.180   0.203
          10      89      89   0.00%   0.057   0.167   0.594   0.077   0.135   0.320   0.373
          15     123     123   0.00%   0.057   0.242   0.743   0.078   0.218   0.457   0.609
          20     145     145   0.00%   0.079   0.521   1.069   0.232   0.508   0.794   0.942
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get coreloadtests/folder_listing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/folder_listing

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.092   0.102   0.118   0.092   0.103   0.118   0.118
           2      18      18   0.00%   0.092   0.119   0.450   0.093   0.103   0.111   0.450
           3      29      29   0.00%   0.083   0.101   0.172   0.092   0.102   0.110   0.117
           5      44      44   0.00%   0.073   0.134   0.272   0.092   0.104   0.238   0.269
          10      88      88   0.00%   0.072   0.224   0.670   0.101   0.174   0.480   0.606
          15     123     123   0.00%   0.084   0.296   1.121   0.115   0.260   0.558   0.595
          20     147     147   0.00%   0.095   0.534   1.062   0.212   0.517   0.843   0.960
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get coreloadtests/sitemap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/sitemap

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.070   0.082   0.106   0.070   0.077   0.106   0.106
           2      18      18   0.00%   0.076   0.087   0.228   0.076   0.077   0.108   0.228
           3      27      27   0.00%   0.056   0.081   0.189   0.076   0.077   0.082   0.093
           5      43      43   0.00%   0.055   0.098   0.221   0.067   0.077   0.163   0.175
          10      85      85   0.00%   0.067   0.178   0.506   0.077   0.151   0.357   0.461
          15     120     120   0.00%   0.056   0.248   0.806   0.078   0.213   0.505   0.521
          20     143     143   0.00%   0.056   0.427   1.151   0.144   0.399   0.780   0.903
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