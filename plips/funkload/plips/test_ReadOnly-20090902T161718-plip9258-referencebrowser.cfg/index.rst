======================
FunkLoad_ bench report
======================


:date: 2009-09-02 16:17:18
:abstract: Read only load test scenario
           Bench result of ``Readonly.test_ReadOnly``: 
           Read only load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 16:17:18
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

* 416 tests
* 2159 pages
* 2159 requests


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.133       8       8   0.00%
       2   0.300      18      18   0.00%
       3   0.450      27      27   0.00%
       5   0.700      42      42   0.00%
      10   1.367      82      82   0.00%
      15   1.817     109     109   0.00%
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
       1   0.717   2.000      43      43   0.00%   0.080   0.102   0.234   0.081   0.097   0.122   0.125
       2   1.533   4.000      92      92   0.00%   0.074   0.108   0.674   0.080   0.105   0.123   0.164
       3   2.333   5.000     140     140   0.00%   0.060   0.118   0.816   0.081   0.106   0.160   0.194
       5   3.767   7.000     226     226   0.00%   0.060   0.128   0.827   0.080   0.107   0.197   0.215
      10   7.133  12.000     428     428   0.00%   0.060   0.224   1.248   0.082   0.174   0.398   0.564
      15   9.517  16.000     571     571   0.00%   0.060   0.362   1.358   0.108   0.301   0.706   0.959
      20  10.983  16.000     659     659   0.00%   0.061   0.640   1.812   0.244   0.603   1.079   1.244
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.717   2.000      43      43   0.00%   0.080   0.102   0.234   0.081   0.097   0.122   0.125
       2   1.533   4.000      92      92   0.00%   0.074   0.108   0.674   0.080   0.105   0.123   0.164
       3   2.333   5.000     140     140   0.00%   0.060   0.118   0.816   0.081   0.106   0.160   0.194
       5   3.767   7.000     226     226   0.00%   0.060   0.128   0.827   0.080   0.107   0.197   0.215
      10   7.133  12.000     428     428   0.00%   0.060   0.224   1.248   0.082   0.174   0.398   0.564
      15   9.517  16.000     571     571   0.00%   0.060   0.362   1.358   0.108   0.301   0.706   0.959
      20  10.983  16.000     659     659   0.00%   0.061   0.640   1.812   0.244   0.603   1.079   1.244
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **20** CUs:

* In page 002 get: /coreloadtests/news took **0.696s**
  `Get /coreloadtests/news`
* In page 004 get: /coreloadtests/folder_listing took **0.691s**
  `Get coreloadtests/folder_listing`
* In page 003 get: /coreloadtests/contact-info took **0.679s**
  `Get /coreloadtests/contact-info`
* In page 001 get: /coreloadtests took **0.571s**
  `Get /coreloadtests`
* In page 005 get: /coreloadtests/sitemap took **0.559s**
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
           1       8       8   0.00%   0.095   0.101   0.106   0.095   0.105   0.106   0.106
           2      18      18   0.00%   0.074   0.104   0.138   0.095   0.105   0.109   0.138
           3      27      27   0.00%   0.094   0.133   0.245   0.095   0.106   0.225   0.239
           5      42      42   0.00%   0.076   0.128   0.512   0.095   0.106   0.180   0.212
          10      82      82   0.00%   0.075   0.268   1.248   0.094   0.206   0.534   0.662
          15     111     111   0.00%   0.075   0.386   1.358   0.111   0.316   0.813   0.964
          20     129     129   0.00%   0.107   0.571   1.609   0.198   0.566   0.921   1.024
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/news
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/news

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.114   0.132   0.234   0.114   0.115   0.234   0.234
           2      19      19   0.00%   0.113   0.153   0.674   0.114   0.116   0.198   0.674
           3      29      29   0.00%   0.095   0.124   0.194   0.112   0.116   0.162   0.187
           5      47      47   0.00%   0.084   0.175   0.805   0.105   0.139   0.233   0.296
          10      86      86   0.00%   0.089   0.253   0.898   0.115   0.195   0.430   0.516
          15     115     115   0.00%   0.085   0.404   1.169   0.125   0.331   0.967   1.127
          20     133     133   0.00%   0.095   0.696   1.661   0.355   0.653   1.110   1.367
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Get /coreloadtests/contact-info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/contact-info

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.081   0.086   0.110   0.081   0.082   0.110   0.110
           2      19      19   0.00%   0.074   0.089   0.164   0.081   0.082   0.115   0.164
           3      29      29   0.00%   0.060   0.103   0.558   0.081   0.082   0.126   0.127
           5      46      46   0.00%   0.061   0.101   0.188   0.068   0.082   0.159   0.172
          10      88      88   0.00%   0.061   0.210   1.188   0.081   0.164   0.348   0.660
          15     119     119   0.00%   0.072   0.347   1.242   0.093   0.272   0.772   0.923
          20     134     134   0.00%   0.081   0.679   1.506   0.253   0.643   1.131   1.289
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get coreloadtests/folder_listing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/folder_listing

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.097   0.105   0.122   0.097   0.098   0.122   0.122
           2      18      18   0.00%   0.097   0.106   0.123   0.098   0.107   0.110   0.123
           3      28      28   0.00%   0.077   0.136   0.816   0.097   0.108   0.152   0.189
           5      46      46   0.00%   0.094   0.136   0.827   0.098   0.108   0.166   0.207
          10      88      88   0.00%   0.077   0.219   0.979   0.098   0.177   0.366   0.415
          15     115     115   0.00%   0.097   0.389   1.135   0.129   0.324   0.737   0.947
          20     133     133   0.00%   0.098   0.691   1.812   0.268   0.622   1.172   1.256
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get coreloadtests/sitemap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/sitemap

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.080   0.084   0.112   0.080   0.081   0.112   0.112
           2      18      18   0.00%   0.078   0.087   0.201   0.079   0.080   0.081   0.201
           3      27      27   0.00%   0.060   0.093   0.164   0.080   0.082   0.142   0.146
           5      45      45   0.00%   0.060   0.098   0.229   0.078   0.081   0.161   0.197
          10      84      84   0.00%   0.060   0.173   0.763   0.080   0.144   0.320   0.387
          15     111     111   0.00%   0.060   0.286   1.001   0.082   0.242   0.530   0.679
          20     130     130   0.00%   0.061   0.559   1.791   0.173   0.508   0.991   1.183
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