======================
FunkLoad_ bench report
======================


:date: 2009-09-02 16:25:24
:abstract: Heavy write load test scenario
           Bench result of ``Writeheavy.test_WriteHeavy``: 
           Heavy write load test scenario

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents

Bench configuration
-------------------

* Launched: 2009-09-02 16:25:24
* Test: ``collective.coreloadtests.tests.test_Writeheavy.py Writeheavy.test_WriteHeavy``
* Server: http://localhost:8080
* Cycles of concurrent users: [1, 2, 3, 5, 10]
* Cycle duration: 120s
* Sleeptime between request: from 0.0s to 2.0s
* Sleeptime between test case: 1.0s
* Startup delay between thread: 0.2s
* FunkLoad_ version: 1.10.0


Bench content
-------------

The test ``Writeheavy.test_WriteHeavy`` contains: 

* 11 page(s)
* 3 redirect(s)
* 0 link(s)
* 0 image(s)
* 0 XML RPC call(s)

The bench contains:

* 118 tests, 20 error(s)
* 1324 pages, 20 error(s)
* 1636 requests, 20 error(s)


Test stats
----------

The number of Successful **Test** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ======= ======= ======= ======= =======
     CUs    STPS   TOTAL SUCCESS   ERROR
 ======= ======= ======= ======= =======
       1   0.067       8       8   0.00%
       2   0.125      17      15  11.76%
       3   0.183      24      22   8.33%
       5   0.233      31      28   9.68%
      10   0.208      38      25  34.21%
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
       1   0.817   3.000      98      98   0.00%   0.011   0.210   1.285   0.021   0.102   0.678   0.721
       2   1.525   5.000     185     183   1.08%   0.010   0.252   1.803   0.021   0.106   0.645   1.212
       3   2.125   5.000     257     255   0.78%   0.010   0.309   3.827   0.021   0.117   0.757   1.271
       5   2.917  10.000     353     350   0.85%   0.010   0.533  10.695   0.052   0.202   1.497   2.843
      10   3.483  11.000     431     418   3.02%   0.011   1.361  18.863   0.134   0.599   3.970   5.520
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Request stats
-------------

The number of **Request** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
     CUs     RPS  maxRPS   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
       1   1.042   3.000     125     125   0.00%   0.010   0.165   0.792   0.020   0.103   0.321   0.485
       2   1.925   5.000     231     229   0.87%   0.009   0.205   1.568   0.020   0.120   0.404   0.798
       3   2.692   6.000     323     321   0.62%   0.009   0.248   3.093   0.018   0.127   0.496   0.695
       5   3.675  10.000     441     438   0.68%   0.009   0.468  10.265   0.038   0.214   0.939   2.020
      10   4.300  12.000     516     503   2.52%   0.009   1.408  18.461   0.137   0.673   2.959   4.991
 ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

5 Slowest requests
------------------

Slowest average response time during the best cycle with **5** CUs:

* In page 008 post: /coreloadtests/Members/lateralis/folder-3/portal_factory/Document/document.2009-09-02.2304326600/edit took **2.765s**
  `Post /coreloadtests/Members/user...511052309/atct_edit`
* In page 007 post: /coreloadtests/Members/volans/portal_factory/Folder/folder.2009-09-02.2382755449/edit took **1.251s**
  `Post /coreloadtests/Members/user...280843853/atct_edit`
* In page 008 redirect: /coreloadtests/Members/lateralis/folder-3/nona-arctos-dorsum-novaehollandiae-rhytis took **0.411s**
  ``
* In page 007 redirect: /coreloadtests/Members/volans/folder-4/ took **0.389s**
  ``
* In page 006 get: /coreloadtests/Members/volans/view took **0.378s**
  `Get /coreloadtests/Members/user/view`

Page detail stats
-----------------


PAGE 001: Get /coreloadtests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests

     .. image:: request_001.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       8       8   0.00%   0.095   0.103   0.106   0.095   0.106   0.106   0.106
           2      16      16   0.00%   0.099   0.156   0.540   0.104   0.112   0.318   0.540
           3      23      23   0.00%   0.075   0.119   0.229   0.093   0.106   0.188   0.202
           5      31      31   0.00%   0.081   0.203   0.757   0.096   0.179   0.336   0.441
          10      38      38   0.00%   0.087   0.572   2.221   0.131   0.277   1.812   2.207
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 002: Get /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/join_form

     .. image:: request_002.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.076   0.080   0.099   0.076   0.077   0.099   0.099
           2      18      18   0.00%   0.057   0.095   0.390   0.076   0.077   0.100   0.390
           3      25      25   0.00%   0.066   0.124   0.451   0.076   0.078   0.260   0.318
           5      34      34   0.00%   0.067   0.124   0.321   0.077   0.086   0.228   0.242
          10      42      42   0.00%   0.066   0.441   2.975   0.107   0.247   0.760   1.504
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 003: Post /coreloadtests/join_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/join_form

     .. image:: request_003.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.080   0.095   0.162   0.080   0.091   0.162   0.162
           2      18      18   0.00%   0.070   0.090   0.159   0.077   0.082   0.106   0.159
           3      25      25   0.00%   0.063   0.155   1.207   0.080   0.082   0.224   0.297
           5      34      34   0.00%   0.062   0.162   0.828   0.081   0.106   0.303   0.376
          10      45      45   0.00%   0.083   0.577   3.244   0.100   0.245   1.746   2.954
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 004: Post /coreloadtests/login_form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/login_form

     .. image:: request_004.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.092   0.098   0.103   0.092   0.101   0.103   0.103
           2      18      18   0.00%   0.081   0.105   0.158   0.092   0.103   0.137   0.158
           3      25      25   0.00%   0.090   0.143   0.695   0.091   0.103   0.191   0.212
           5      34      34   0.00%   0.091   0.268   1.046   0.103   0.217   0.570   0.894
          10      45      45   0.00%   0.138   0.810   3.971   0.283   0.535   1.810   2.159
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 005: Get /coreloadtests/dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/dashboard

     .. image:: request_005.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.121   0.142   0.211   0.121   0.134   0.211   0.211
           2      18      18   0.00%   0.116   0.148   0.243   0.120   0.132   0.232   0.243
           3      25      25   0.00%   0.106   0.171   0.393   0.121   0.132   0.293   0.363
           5      34      34   0.00%   0.109   0.239   0.872   0.119   0.167   0.418   0.791
          10      44      44   0.00%   0.113   0.774   2.517   0.177   0.620   1.519   1.864
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 006: Get /coreloadtests/Members/user/view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/Members/nothos/view

     .. image:: request_006.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.237   0.258   0.307   0.237   0.248   0.307   0.307
           2      18      17   5.56%   0.194   0.254   0.404   0.231   0.248   0.312   0.404
           3      24      22   8.33%   0.212   0.339   0.789   0.237   0.259   0.562   0.619
           5      33      32   3.03%   0.205   0.378   1.105   0.235   0.317   0.622   0.678
          10      44      43   2.27%   0.282   0.975   3.457   0.399   0.949   1.603   2.213
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, get, url /coreloadtests/Members/nothos/createObject?type_name=Folder

     .. image:: request_006.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.011   0.018   0.022   0.011   0.021   0.022   0.022
           2      17      17   0.00%   0.010   0.067   0.516   0.010   0.021   0.179   0.516
           3      22      22   0.00%   0.010   0.065   0.568   0.010   0.021   0.120   0.208
           5      32      32   0.00%   0.010   0.066   0.248   0.011   0.039   0.169   0.245
          10      42      42   0.00%   0.011   0.657   2.959   0.054   0.340   1.484   2.703
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 007: Post /coreloadtests/Members/user...280843853/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/nothos/portal_factory/Folder/folder.2009-09-02.8378416426/edit

     .. image:: request_007.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.279   0.314   0.393   0.279   0.308   0.393   0.393
           2      17      16   5.88%   0.293   0.418   1.270   0.293   0.316   0.970   1.270
           3      22      22   0.00%   0.307   0.383   0.686   0.312   0.334   0.529   0.612
           5      32      32   0.00%   0.270   1.251   3.950   0.317   0.846   2.966   3.105
          10      39      35  10.26%   1.150   3.713  12.471   1.226   2.607   7.809  11.412
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/nothos/folder-5/

     .. image:: request_007.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.240   0.308   0.785   0.240   0.247   0.785   0.785
           2      16      16   0.00%   0.217   0.286   0.808   0.229   0.251   0.335   0.808
           3      22      22   0.00%   0.235   0.306   0.692   0.248   0.286   0.349   0.366
           5      32      32   0.00%   0.226   0.389   1.207   0.240   0.334   0.550   0.939
          10      35      35   0.00%   0.248   1.317   4.216   0.394   1.056   2.557   2.874
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 003, get, url /coreloadtests/Members/nothos/folder-5/createObject?type_name=Document

     .. image:: request_007.003.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.011   0.019   0.022   0.011   0.022   0.022   0.022
           2      15      15   0.00%   0.011   0.016   0.030   0.011   0.012   0.022   0.030
           3      22      22   0.00%   0.011   0.025   0.160   0.011   0.018   0.042   0.054
           5      31      31   0.00%   0.011   0.113   0.751   0.011   0.041   0.313   0.414
          10      34      34   0.00%   0.012   0.985   3.063   0.042   0.747   2.668   2.778
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 008: Post /coreloadtests/Members/user...511052309/atct_edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url /coreloadtests/Members/nothos/folder-5/portal_factory/Document/document.2009-09-02.8405246581/edit

     .. image:: request_008.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.460   0.487   0.504   0.460   0.485   0.504   0.504
           2      15      15   0.00%   0.449   0.853   1.568   0.458   0.929   1.232   1.568
           3      22      22   0.00%   0.492   1.269   3.093   0.494   1.056   2.403   2.463
           5      30      28   6.67%   0.450   2.765  10.265   0.618   2.072   8.680   9.112
          10      33      25  24.24%   1.051   6.844  18.461   1.959   4.897  13.935  18.168
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/Members/nothos/folder-5/brevis-zygos-occidentalis-stoma-morphos

     .. image:: request_008.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.212   0.289   0.792   0.212   0.231   0.792   0.792
           2      15      15   0.00%   0.213   0.295   0.731   0.219   0.248   0.363   0.731
           3      22      22   0.00%   0.190   0.267   0.734   0.202   0.228   0.315   0.449
           5      28      28   0.00%   0.193   0.411   1.852   0.207   0.320   0.770   0.882
          10      25      25   0.00%   0.284   1.526   3.849   0.472   1.432   2.494   3.558
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

PAGE 009: Get /coreloadtests/logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url /coreloadtests/logout

     .. image:: request_009.001.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.010   0.017   0.020   0.010   0.020   0.020   0.020
           2      15      15   0.00%   0.009   0.040   0.184   0.010   0.020   0.135   0.184
           3      22      22   0.00%   0.009   0.049   0.529   0.010   0.010   0.093   0.100
           5      28      28   0.00%   0.009   0.089   0.488   0.009   0.039   0.430   0.469
          10      25      25   0.00%   0.009   0.701   2.595   0.038   0.436   2.132   2.306
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
* Req: 002, redirect, url /coreloadtests/logged_out

     .. image:: request_009.002.png

     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
         CUs   TOTAL SUCCESS   ERROR     MIN     AVG     MAX     P10     MED     P90     P95
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======
           1       9       9   0.00%   0.064   0.073   0.084   0.064   0.074   0.084   0.084
           2      15      15   0.00%   0.065   0.103   0.269   0.074   0.087   0.130   0.269
           3      22      22   0.00%   0.064   0.115   0.254   0.078   0.086   0.212   0.248
           5      28      28   0.00%   0.074   0.202   0.809   0.084   0.149   0.400   0.429
          10      25      25   0.00%   0.091   0.537   3.388   0.137   0.208   1.708   2.044
     ======= ======= ======= ======= ======= ======= ======= ======= ======= ======= =======

Failures and Errors
-------------------


Failures
~~~~~~~~

* 7 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in Connection.py, line 594: See the server error log for details
* 6 time(s), code: 500, <class 'ZODB.POSException.ConflictError'>
  in FileStorage.py, line 514: See the server error log for details
* 7 time(s), code: 503::

    No traceback.


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