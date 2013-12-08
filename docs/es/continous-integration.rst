.. -*- coding: utf-8 -*-

Prácticas esenciales de Integración Continuas
=============================================

El sistema CI en jenkins.plone.org es un recurso compartido para desarrolladores
de núcleo Plone para notificarles de regresiones en el código de núcleo Plone. Construir roturas son una parte normal y esperada del proceso de desarrollo. Nuestro objetivo es encontrar los errores y eliminarlos lo antes posible, sin esperar la perfección y cero errores. Sin embargo, hay algunas reglas esenciales que hay que seguir para lograr una versión estable.


1) No hacer un Check In en una construcción Rota
------------------------------------------------

No haga las cosas más complicadas para el desarrollador que es responsable por romper la construcción. Si la construcción se rompe, el desarrollador tiene que identificar el
causa de la rotura, tan pronto como sea posible y debería arreglarlo.

Si adoptamos esta estrategia, siempre vamos a estar en la mejor posición para saber qué causó el error y solucionarlo de inmediato. Si uno de los desarrolladores ha
hecho un check-in y causo la rotura de la construcción, como resultado, tenemos la mejor oportunidad de corregir la construcción si tenemos una visión clara de este problema. Realizando check-in de cambios en un futuro y provocando nuevas construcciones sólo conducirá a más problemas.

Si la construcción se rompe en un período más largo de tiempo (más de un par de
hora) se debe ya sea notificar al desarrollador que es responsable de la
rotura, solucionar el problema por sí mismo, o simplemente revertir el ``commit`` con el fin de poder seguir trabajando.

.. note::

    Hay una excepción a esta regla. A veces hay cambios o pruebas
    que dependen de los cambios en otros paquetes. Si este es el caso, no hay
    manera alrededor de romper una sola construcción durante un cierto período de tiempo. En este caso, ejecutar todas las pruebas locales con todos los cambios y el ``commit`` dentro de un marco de tiempo de 10 minutos.


2) Siempre ejecutar todas pruebas Commit localmente antes de hacer Commit
-------------------------------------------------------------------------

Siguiendo esta práctica asegura la construcción permanece verde (según lo que indique la maquina de construcción de pruebas continuas) y otros desarrolladores pueden
seguir trabajando sin romper la primera regla.

Puede haber cambios que se han comprobado antes de su última actualización de
el control de versiones de que podría conducir a un error de generación en Jenkins en
combinación con los cambios. Por lo tanto es esencial que compruebe
(:command:`git pull`) y correr las pruebas otra vez antes de hacer ``push`` su cambios a github.

Por otra parte, una fuente común de errores en el check-in es olvidarse de añadir algunos
archivos en el repositorio. Si usted sigue esta regla y su construcción local pasa, usted puede estar seguro de esto debido a alguien más hizo un check en el ínterin, 
o porque usted se olvidó de agregar una nueva clase o archivo de configuración que usted ha estado trabajando en el sistema de control de versiones.


3) Esperar a que pasen las pruebas de Commit antes de moverse del sitio
-----------------------------------------------------------------------

Siempre supervisar el progreso de la construcción y solucionar el problema de inmediato si falla. Usted tiene muchas más posibilidades de corregir de la construcción, si sólo
introdujo una regresión que tarde. También otro desarrollador podría haber
hecho un commit en el ínterin (por infringir la regla 1) haciendo las cosas más complicadas
para usted.


4) Nunca irse a casa con una construcción Rota
----------------------------------------------

Teniendo en cuenta la primera regla de la IC ("No hacer check in cuando una construcción rota"),
rompiendo la construcción esencialmente detiene todos los demás desarrolladores de trabajar en él.
Por lo tanto, ir a casa tiendo en una construcción rota (o incluso a una construcción que no ha terminado aún) no es aceptable, porque va a evitar todos los demás
desarrolladores a dejar de trabajar en la construcción o la corrección de los errores que ha
introducido.


5) Esté siempre preparado para volver a la revisión previa
----------------------------------------------------------

A fin de que los otros desarrolladores puedan trabajar en la construcción, usted debiera
siempre estar preparado para volver a la revisión anterior (pasada).


6) Caja de tiempo para la corrección antes de revertir cambios
--------------------------------------------------------------

Cuando la construcción se rompe en el check-in, trate de arreglarlo por diez minutos. Si, después de
diez minutos, que no se allá con la solución, volver a la anterior
versión de su sistema de control de versiones. De esta manera se permitirá a otros
desarrolladores seguir trabajando.


7) No comentar código si las pruebas fallan
-------------------------------------------

Una vez que comience a aplicar la regla anterior, el resultado suele ser que
los desarrolladores empiecen a hacer comentarios de código a la pruebas fallidas en orden de obtener la construcción
que pase las pruebas de nuevo lo más rápido posible. Si bien este impulso es comprensible, es un error. Las pruebas han estado pasando por un tiempo y luego empiezan a fallar.
Esto significa que, o bien producir una regresión, hicimos suposiciones que no son
deja de ser válida, o la aplicación ha cambiado la funcionalidad se está probando por una razón válida.

Usted siempre debe corregir bien el código (si tiene una regresión
ha sido encontrada), modificar la prueba (si es una de las hipótesis ha cambiado), o
borrarlo (si la funcionalidad está probando ya no existe).


8) Asumir la responsabilidad de todas las roturas que se derivan de sus Cambios
-------------------------------------------------------------------------------

Si usted hace un ``commit`` a un cambio y todas las pruebas que escribiste pasan, pero otros se rompe, la
construcción todavía está roto. Esto también se aplica a las pruebas que fallan en
``buildout.coredev`` y no pertenecen directamente al paquete que ha trabajado.
Por lo general, esto significa que usted ha introducido un error de regresión en la
aplicación. Es su responsabilidad - porque usted realizó el cambio - la corrección de todas las pruebas que no están pasando como consecuencia de los cambios.

Hay algunas pruebas de Plone que fallan al azar, siempre estamos trabajando en la corrección de esos. Si usted piensa que usted afecta una prueba de este tipo, trate de solucionarlo (mejorarlo) o volver a ejecutar el trabajo de Jenkins para ver si pasa de nuevo las pruebas. En cualquier caso, el desarrollador que
hace el commit es responsable de hacer que pase.


*) Romper la construcción y la compre Caipiriñas para todo el mundo
-------------------------------------------------------------------

Si se rompe la construcción que tiene que comprar Caipiriñas para todo el mundo (después usted
debe corregir la construcción por supuesto).

.. note::

    Esta regla se aplica sólo durante los sprints en Brasil. ;-)


Lectura adicional
-----------------

Esas reglas fueron tomadas del excelente libro "Continuous Delivery" por Jez Humble y David Farley (Addison Wesley) y han sido adoptadas y reescritas para la comunidad Plone. Si usted desea aprender más acerca de la Integración Continua y Entrega Continua (Continuous Delivery), yo recomiendo que compre este libro.
