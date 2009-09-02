======================
FunkLoad_ bench report
======================


:date: 2009-09-02 12:00:34
:abstract: Read only load test scenario
           Bench result of ``Readonly.test_ReadOnly``: 
           Read only load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 12:00:34
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

* 433 tests
* 2215 pages
* 2215 requests


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.167      10      10   0.00%
       2   0.300      18      18   0.00%
       3   0.433      26      26   0.00%
       5   0.700      42      42   0.00%
      10   1.350      81      81   0.00%
      15   1.967     118     118   0.00%
      20   2.300     138     138   0.00%
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
       1   0.833   3.000      50      50   0.00%   0.066   0.096   0.236   0.076   0.094   0.111   0.118
       2   1.567   5.000      94      94   0.00%   0.056   0.102   0.528   0.076   0.093   0.111   0.120
       3   2.217   5.000     133     133   0.00%   0.057   0.100   0.457   0.077   0.094   0.118   0.132
       5   3.600   8.000     216     216   0.00%   0.056   0.125   0.432   0.076   0.103   0.211   0.231
      10   7.067  11.000     424     424   0.00%   0.056   0.181   0.876   0.077   0.139   0.328   0.423
      15   9.967  18.000     598     598   0.00%   0.057   0.308   1.024   0.100   0.263   0.577   0.693
      20  11.667  17.000     700     700   0.00%   0.055   0.495   1.333   0.182   0.468   0.824   0.913
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   0.833   3.000      50      50   0.00%   0.066   0.096   0.236   0.076   0.094   0.111   0.118
       2   1.567   5.000      94      94   0.00%   0.056   0.102   0.528   0.076   0.093   0.111   0.120
       3   2.217   5.000     133     133   0.00%   0.057   0.100   0.457   0.077   0.094   0.118   0.132
       5   3.600   8.000     216     216   0.00%   0.056   0.125   0.432   0.076   0.103   0.211   0.231
      10   7.067  11.000     424     424   0.00%   0.056   0.181   0.876   0.077   0.139   0.328   0.423
      15   9.967  18.000     598     598   0.00%   0.057   0.308   1.024   0.100   0.263   0.577   0.693
      20  11.667  17.000     700     700   0.00%   0.055   0.495   1.333   0.182   0.468   0.824   0.913
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **20** CUs:

* In page 004 get: /coreloadtests/folder_listing took **0.556s**
  `Get coreloadtests/folder_listing`
* In page 001 get: /coreloadtests took **0.516s**
  `Get /coreloadtests`
* In page 002 get: /coreloadtests/news took **0.510s**
  `Get /coreloadtests/news`
* In page 003 get: /coreloadtests/contact-info took **0.449s**
  `Get /coreloadtests/contact-info`
* In page 005 get: /coreloadtests/sitemap took **0.443s**
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
           1      10      10   0.00%   0.090   0.097   0.105   0.091   0.100   0.105   0.105
           2      18      18   0.00%   0.071   0.095   0.108   0.085   0.101   0.105   0.108
           3      26      26   0.00%   0.070   0.102   0.214   0.090   0.101   0.103   0.111
           5      41      41   0.00%   0.070   0.128   0.388   0.090   0.098   0.202   0.222
          10      81      81   0.00%   0.070   0.187   0.712   0.090   0.158   0.298   0.366
          15     118     118   0.00%   0.070   0.308   1.024   0.110   0.277   0.543   0.701
          20     136     136   0.00%   0.072   0.516   1.317   0.167   0.484   0.880   0.954
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/news
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/news

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      10      10   0.00%   0.098   0.123   0.236   0.108   0.110   0.236   0.236
           2      19      19   0.00%   0.100   0.115   0.163   0.100   0.110   0.124   0.163
           3      27      27   0.00%   0.079   0.133   0.457   0.100   0.111   0.219   0.249
           5      46      46   0.00%   0.079   0.142   0.294   0.100   0.123   0.218   0.229
          10      84      84   0.00%   0.079   0.220   0.876   0.109   0.166   0.422   0.644
          15     118     118   0.00%   0.080   0.354   1.022   0.141   0.328   0.636   0.760
          20     138     138   0.00%   0.101   0.510   1.333   0.254   0.485   0.793   0.913
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Get /coreloadtests/contact-info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/contact-info

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      10      10   0.00%   0.076   0.080   0.106   0.077   0.078   0.106   0.106
           2      19      19   0.00%   0.074   0.103   0.528   0.076   0.077   0.109   0.528
           3      27      27   0.00%   0.076   0.084   0.143   0.077   0.078   0.096   0.119
           5      45      45   0.00%   0.057   0.102   0.339   0.076   0.078   0.176   0.220
          10      88      88   0.00%   0.057   0.162   0.812   0.077   0.115   0.320   0.388
          15     118     118   0.00%   0.057   0.322   1.007   0.081   0.256   0.586   0.818
          20     142     142   0.00%   0.077   0.449   1.081   0.126   0.405   0.821   0.862
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Get coreloadtests/folder_listing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/folder_listing

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      10      10   0.00%   0.088   0.101   0.118   0.093   0.102   0.118   0.118
           2      19      19   0.00%   0.093   0.122   0.521   0.093   0.103   0.106   0.521
           3      27      27   0.00%   0.073   0.103   0.156   0.092   0.102   0.124   0.130
           5      42      42   0.00%   0.072   0.127   0.432   0.091   0.103   0.192   0.214
          10      87      87   0.00%   0.072   0.188   0.645   0.092   0.156   0.365   0.398
          15     122     122   0.00%   0.072   0.311   0.883   0.102   0.259   0.624   0.691
          20     144     144   0.00%   0.085   0.556   1.276   0.197   0.541   0.856   0.997
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get coreloadtests/sitemap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/sitemap

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1      10      10   0.00%   0.066   0.080   0.108   0.075   0.077   0.108   0.108
           2      19      19   0.00%   0.056   0.076   0.088   0.057   0.077   0.081   0.088
           3      26      26   0.00%   0.057   0.076   0.111   0.058   0.077   0.082   0.091
           5      42      42   0.00%   0.056   0.123   0.416   0.075   0.085   0.215   0.231
          10      84      84   0.00%   0.056   0.150   0.810   0.076   0.101   0.275   0.369
          15     122     122   0.00%   0.062   0.245   0.938   0.077   0.194   0.474   0.584
          20     140     140   0.00%   0.055   0.443   1.088   0.199   0.393   0.782   0.881
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