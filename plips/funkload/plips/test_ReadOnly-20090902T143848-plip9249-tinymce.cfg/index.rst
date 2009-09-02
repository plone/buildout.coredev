======================
FunkLoad_ bench report
======================


:date: 2009-09-02 14:38:48
:abstract: Read only load test scenario
           Bench result of ``Readonly.test_ReadOnly``: 
           Read only load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 14:38:48
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

* 430 tests
* 2210 pages
* 2210 requests


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.150       9       9   0.00%
       2   0.300      18      18   0.00%
       3   0.433      26      26   0.00%
       5   0.700      42      42   0.00%
      10   1.433      86      86   0.00%
      15   1.933     116     116   0.00%
      20   2.217     133     133   0.00%
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
       1   0.783   3.000      47      47   0.00%   0.059   0.107   0.495   0.079   0.096   0.123   0.124
       2   1.533   4.000      92      92   0.00%   0.060   0.098   0.181   0.079   0.104   0.117   0.124
       3   2.250   5.000     135     135   0.00%   0.060   0.112   0.547   0.079   0.096   0.159   0.190
       5   3.750   8.000     225     225   0.00%   0.058   0.124   0.591   0.079   0.105   0.203   0.227
      10   7.367  11.000     442     442   0.00%   0.058   0.190   0.939   0.080   0.161   0.312   0.407
      15   9.833  14.000     590     590   0.00%   0.058   0.344   1.171   0.115   0.301   0.662   0.778
      20  11.317  18.000     679     679   0.00%   0.059   0.544   1.337   0.237   0.518   0.897   0.997
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.783   3.000      47      47   0.00%   0.059   0.107   0.495   0.079   0.096   0.123   0.124
       2   1.533   4.000      92      92   0.00%   0.060   0.098   0.181   0.079   0.104   0.117   0.124
       3   2.250   5.000     135     135   0.00%   0.060   0.112   0.547   0.079   0.096   0.159   0.190
       5   3.750   8.000     225     225   0.00%   0.058   0.124   0.591   0.079   0.105   0.203   0.227
      10   7.367  11.000     442     442   0.00%   0.058   0.190   0.939   0.080   0.161   0.312   0.407
      15   9.833  14.000     590     590   0.00%   0.058   0.344   1.171   0.115   0.301   0.662   0.778
      20  11.317  18.000     679     679   0.00%   0.059   0.544   1.337   0.237   0.518   0.897   0.997
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **20** CUs:

* In page 001 get: /coreloadtests took **0.594s**
  `Get /coreloadtests`
* In page 004 get: /coreloadtests/folder_listing took **0.567s**
  `Get coreloadtests/folder_listing`
* In page 002 get: /coreloadtests/news took **0.559s**
  `Get /coreloadtests/news`
* In page 005 get: /coreloadtests/sitemap took **0.514s**
  `Get coreloadtests/sitemap`
* In page 003 get: /coreloadtests/contact-info took **0.487s**
  `Get /coreloadtests/contact-info`

Page detail stats
-----------------


PAGE 001: Get /coreloadtests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests

     .. image:: request_001.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.094   0.101   0.107   0.094   0.104   0.107   0.107
           2      18      18   0.00%   0.074   0.104   0.135   0.094   0.104   0.110   0.135
           3      26      26   0.00%   0.074   0.141   0.547   0.093   0.104   0.262   0.533
           5      42      42   0.00%   0.073   0.146   0.482   0.093   0.105   0.262   0.271
          10      84      84   0.00%   0.073   0.200   0.707   0.093   0.163   0.348   0.536
          15     116     116   0.00%   0.075   0.371   1.117   0.122   0.329   0.692   0.821
          20     132     132   0.00%   0.121   0.594   1.337   0.248   0.588   0.956   1.062
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/news
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/news

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      10      10   0.00%   0.113   0.130   0.237   0.113   0.123   0.237   0.237
           2      19      19   0.00%   0.093   0.117   0.129   0.113   0.116   0.126   0.129
           3      28      28   0.00%   0.083   0.125   0.190   0.103   0.123   0.159   0.182
           5      47      47   0.00%   0.083   0.140   0.534   0.104   0.123   0.203   0.215
          10      89      89   0.00%   0.083   0.206   0.939   0.105   0.175   0.311   0.423
          15     118     118   0.00%   0.106   0.411   1.171   0.131   0.345   0.834   0.961
          20     133     133   0.00%   0.113   0.559   1.304   0.276   0.525   0.923   1.002
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Get /coreloadtests/contact-info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/contact-info

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      10      10   0.00%   0.079   0.081   0.084   0.080   0.081   0.084   0.084
           2      19      19   0.00%   0.060   0.079   0.083   0.080   0.080   0.081   0.083
           3      29      29   0.00%   0.060   0.090   0.180   0.080   0.080   0.167   0.169
           5      47      47   0.00%   0.060   0.089   0.184   0.080   0.081   0.113   0.123
          10      90      90   0.00%   0.060   0.162   0.615   0.079   0.143   0.287   0.376
          15     118     118   0.00%   0.060   0.291   0.769   0.081   0.251   0.568   0.657
          20     136     136   0.00%   0.071   0.487   1.138   0.258   0.465   0.771   0.859
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get coreloadtests/folder_listing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/folder_listing

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.079   0.098   0.109   0.079   0.097   0.109   0.109
           2      18      18   0.00%   0.096   0.104   0.119   0.096   0.106   0.112   0.119
           3      26      26   0.00%   0.076   0.120   0.330   0.089   0.104   0.192   0.206
           5      46      46   0.00%   0.075   0.141   0.591   0.096   0.108   0.213   0.235
          10      90      90   0.00%   0.076   0.230   0.934   0.096   0.198   0.389   0.598
          15     119     119   0.00%   0.076   0.361   0.880   0.119   0.342   0.683   0.783
          20     140     140   0.00%   0.097   0.567   1.191   0.243   0.547   0.981   1.072
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get coreloadtests/sitemap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/sitemap

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.059   0.127   0.495   0.059   0.079   0.495   0.495
           2      18      18   0.00%   0.073   0.085   0.181   0.078   0.079   0.096   0.181
           3      26      26   0.00%   0.068   0.084   0.177   0.078   0.079   0.082   0.123
           5      43      43   0.00%   0.058   0.106   0.498   0.076   0.080   0.175   0.186
          10      89      89   0.00%   0.058   0.151   0.479   0.078   0.134   0.264   0.306
          15     119     119   0.00%   0.058   0.287   0.802   0.093   0.244   0.540   0.641
          20     138     138   0.00%   0.059   0.514   1.176   0.189   0.512   0.862   0.997
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