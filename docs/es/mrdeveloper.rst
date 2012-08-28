Mr. Developer
=============

Esta configuracion buildout usa mr.developer para administrar los paquetes de desarrollo. Ver 
http://pypi.python.org/pypi/mr.developer para mayor informacion o ejecutar 
el comando 'bin/develop help' para un lista de comando disponibles.

El mas comun flujo de trabajo para obtener todas la ultimas actualizciones es:

  $ git pull
  $ bin/develop rb

Esto te conseguirá la version masreciente de la configuración coredev, compruebe 
y actualice todos los paquetes vía Subversion en el directorio src y ejecute 
buildout para configurar el asunto.

De vez en cuando puedes comprobar si alguna cosas pendiente:

  $ bin/develop st

Si esto imprime algua líneas con un signo de interrogación delante, usted puede limpiarlo con:

  $ bin/develop purge

Esto sacará los paquetes del directorio src/ los cuáles ya no son necesarios, 
cuando estos han sido reemplazados por una apropiada liberacion en formato Egg 
de estos paquetes.
