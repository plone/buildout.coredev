======================
FunkLoad_ bench report
======================


:date: 2009-09-02 17:23:27
:abstract: Read only load test scenario
           Bench result of ``Readonly.test_ReadOnly``: 
           Read only load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 17:23:27
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

* 415 tests
* 2138 pages
* 2138 requests


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.150       9       9   0.00%
       2   0.300      18      18   0.00%
       3   0.417      25      25   0.00%
       5   0.733      44      44   0.00%
      10   1.317      79      79   0.00%
      15   1.867     112     112   0.00%
      20   2.133     128     128   0.00%
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
       1   0.800   2.000      48      48   0.00%   0.072   0.116   0.908   0.080   0.098   0.125   0.125
       2   1.500   3.000      90      90   0.00%   0.060   0.114   0.729   0.080   0.105   0.126   0.192
       3   2.183   6.000     131     131   0.00%   0.060   0.113   0.748   0.081   0.104   0.151   0.193
       5   3.717   7.000     223     223   0.00%   0.060   0.139   0.984   0.080   0.111   0.205   0.241
      10   6.950  11.000     417     417   0.00%   0.060   0.227   1.303   0.081   0.152   0.421   0.866
      15   9.467  16.000     568     568   0.00%   0.061   0.394   1.602   0.119   0.320   0.777   1.081
      20  11.017  17.000     661     661   0.00%   0.071   0.612   1.723   0.239   0.541   1.103   1.296
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.800   2.000      48      48   0.00%   0.072   0.116   0.908   0.080   0.098   0.125   0.125
       2   1.500   3.000      90      90   0.00%   0.060   0.114   0.729   0.080   0.105   0.126   0.192
       3   2.183   6.000     131     131   0.00%   0.060   0.113   0.748   0.081   0.104   0.151   0.193
       5   3.717   7.000     223     223   0.00%   0.060   0.139   0.984   0.080   0.111   0.205   0.241
      10   6.950  11.000     417     417   0.00%   0.060   0.227   1.303   0.081   0.152   0.421   0.866
      15   9.467  16.000     568     568   0.00%   0.061   0.394   1.602   0.119   0.320   0.777   1.081
      20  11.017  17.000     661     661   0.00%   0.071   0.612   1.723   0.239   0.541   1.103   1.296
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **20** CUs:

* In page 001 get: /coreloadtests took **0.689s**
  `Get /coreloadtests`
* In page 002 get: /coreloadtests/news took **0.659s**
  `Get /coreloadtests/news`
* In page 004 get: /coreloadtests/folder_listing took **0.604s**
  `Get coreloadtests/folder_listing`
* In page 003 get: /coreloadtests/contact-info took **0.595s**
  `Get /coreloadtests/contact-info`
* In page 005 get: /coreloadtests/sitemap took **0.513s**
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
           1       9       9   0.00%   0.095   0.101   0.108   0.095   0.104   0.108   0.108
           2      17      17   0.00%   0.094   0.112   0.224   0.095   0.105   0.118   0.224
           3      25      25   0.00%   0.074   0.110   0.235   0.094   0.104   0.123   0.189
           5      43      43   0.00%   0.074   0.133   0.281   0.094   0.109   0.195   0.223
          10      80      80   0.00%   0.074   0.291   1.303   0.095   0.188   0.981   1.140
          15     110     110   0.00%   0.074   0.403   1.492   0.128   0.324   0.774   1.109
          20     128     128   0.00%   0.169   0.689   1.580   0.290   0.635   1.217   1.371
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/news
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/news

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      10      10   0.00%   0.084   0.195   0.908   0.115   0.124   0.908   0.908
           2      19      19   0.00%   0.087   0.137   0.452   0.114   0.116   0.141   0.452
           3      27      27   0.00%   0.084   0.128   0.230   0.089   0.120   0.175   0.202
           5      45      45   0.00%   0.084   0.157   0.936   0.113   0.125   0.209   0.214
          10      84      84   0.00%   0.099   0.297   1.140   0.117   0.227   0.570   0.828
          15     113     113   0.00%   0.092   0.455   1.579   0.131   0.366   0.901   1.186
          20     135     135   0.00%   0.118   0.659   1.723   0.255   0.589   1.118   1.361
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Get /coreloadtests/contact-info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/contact-info

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      10      10   0.00%   0.080   0.086   0.123   0.080   0.081   0.123   0.123
           2      18      18   0.00%   0.075   0.118   0.729   0.080   0.082   0.093   0.729
           3      27      27   0.00%   0.061   0.086   0.133   0.080   0.081   0.107   0.112
           5      45      45   0.00%   0.061   0.112   0.419   0.080   0.082   0.185   0.198
          10      86      86   0.00%   0.061   0.183   1.082   0.071   0.112   0.305   0.866
          15     114     114   0.00%   0.071   0.354   1.407   0.109   0.303   0.601   1.094
          20     135     135   0.00%   0.076   0.595   1.556   0.244   0.505   1.090   1.234
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get coreloadtests/folder_listing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/folder_listing

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      10      10   0.00%   0.096   0.107   0.132   0.097   0.107   0.132   0.132
           2      18      18   0.00%   0.078   0.120   0.269   0.097   0.108   0.192   0.269
           3      26      26   0.00%   0.076   0.113   0.214   0.097   0.107   0.137   0.176
           5      45      45   0.00%   0.080   0.151   0.791   0.097   0.111   0.216   0.255
          10      85      85   0.00%   0.077   0.209   0.985   0.098   0.171   0.307   0.427
          15     117     117   0.00%   0.077   0.439   1.602   0.122   0.332   0.940   1.229
          20     134     134   0.00%   0.103   0.604   1.688   0.272   0.549   1.018   1.263
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get coreloadtests/sitemap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/sitemap

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.072   0.085   0.121   0.072   0.081   0.121   0.121
           2      18      18   0.00%   0.060   0.081   0.105   0.076   0.080   0.085   0.105
           3      26      26   0.00%   0.060   0.130   0.748   0.080   0.083   0.193   0.361
           5      45      45   0.00%   0.060   0.141   0.984   0.080   0.081   0.222   0.281
          10      82      82   0.00%   0.060   0.160   0.980   0.070   0.102   0.274   0.334
          15     114     114   0.00%   0.061   0.319   0.987   0.105   0.278   0.538   0.710
          20     129     129   0.00%   0.071   0.513   1.583   0.157   0.435   1.016   1.255
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