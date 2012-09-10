Como presentar corrección de fallos al núcleo de Plone
======================================================
Este documento supone que usted quiere corregir un fallo y detallará el proceso completo para hacerlo. Para más información en la escritura de PLIPS, por favor :doc:`valla aqui <plips>`.

Política sobre soporte a la Versión
-----------------------------------
Si usted está tratando de corregir fallos, tenga en cuenta que Plone tiene una `política sobre soporte a la versión <http://plone.org/support/version-support-policy>`_.

Dependencias
------------
* `Git <http://help.github.com/mac-set-up-git/>`_
* `Subversion <http://subversion.apache.org/>`_
* `Python <http://python.org/>`_ 2.6 or 2.7  incluyendo encabezados de desarrollo.
* Si usted esta usando un Mac OSX, necesitara instalar XCode. Usted puede hacer este a través de la app store o muchos otros métodos que venden. Usted probablemente querrá instalar su propio python 2.6 entonces necesita fuera todos los archivos encabezados cuál hace compilar algunas extensiones. Usted puede ignorar este consejo para empezar, pero tenga fe, volverás a él más tarde. Ellos siempre hacen...
* `Python Imaging Library (PIL) <http://www.pythonware.com/products/pil/>`_. Debe asegurarse instalar esto dentro de su apropiado entorno python.
* `VirtualEnv <http://www.virtualenv.org/en/latest/index.html>`_  en el apropiado entorno python.
* `GCC <http://gcc.gnu.org/>`_ para compilar ZODB, Zope y lxml.
* `libxml2 y libxslt <http://xmlsoft.org/XSLT/downloads.html>`_, incluyendo los encabezados de desarrollo.


Instalando su Entorno de Desarrollo
-----------------------------------
El primer paso en corregir un fallo está consiguiendo ejecutar este buildout correctamente. Le recomendamos corregir un fallo en la branch más reciente y entonces backporting tan como sea necesario. `Github <https://github.com/plone/buildout.coredev/>`_ por defecto siempre apunta a la rama actualmente activa. Más información en el cambio de ramas de liberación a continuación.

Para instalar un entorno de desarrollo plone 4.2::

  > cd ~/buildouts # o donde tu quieras colocar sus cosas
  > git clone -b 4.2  https://github.com/plone/buildout.coredev ./plone42devel
  > virtualenv --no-site-packages plone42devpy
  > cd plone42devel
  > ../plone42devpy/bin/python bootstrap.py # (donde "python" es su binario python 2.6). 
  > bin/buildout -v

Si se encuentra con problemas en este proceso, consulte la documentación :doc:`issues`.

Esto se ejecutará durante mucho tiempo, si es su primera ejecución de buildout (~ 20 minutos). Una vez que se hace ejecutado el buildout, usted puede comenzar su nueva instancia Zope con el siguiente comando::

  > ./bin/instance fg

El usuario y contraseña por defecto para una instancia Zope de desarrollo es admin/admin.

Cambiar Branches
^^^^^^^^^^^^^^^^
Si su fallo es especifico en una branch o usted piensa que debería hacer backport, usted puede cambiar fácilmente las branches. La primera ves usted tiene que obtener una branch, usted debe hacer::

  > git checkout -t origin/4.1

Esto debería crear una branch local de 4,1 rastrear el uno en github. A partir de entonces sólo se puede hacer::

  > git checkout 4.1

Para ver qué branch que se encuentra actualmente, acaba de hacer::

  > git branch

La línea con un * por él indicará qué rama actualmente estás trabajando.

.. important::
   Asegúrese de volver a ejecutar buildout si estuviera en una rama diferente antes para obtener las versiones correctas de los paquetes, de lo contrario obtendrá un comportamiento extraño! 

Para mas información sobre buildout, por favor ver la `documentación sobre buildout en el manual de desarrollador collective <http://collective-docs.plone.org/en/latest/tutorials/buildout/index.html>`_.


Comprobando Paquetes para corregir
----------------------------------
La mayoría de paquetes no están en el directorio src/ por defecto, así usted que puedes usar mr.developer para conseguir la versión mas reciente y asegurarse que usted siempre tiene la versión mas actualizada. Puede ser un poco intimidante al principio para averiguar qué paquetes están causando el fallo en cuestión, pero sólo pregunte en el IRC si necesitas algo de ayuda. Una vez que [cree] saben cuál es el paquete(s) que desea, tenemos que obtener de la fuente del mismo.

Usted puede conseguir la fuente del paquete con mr.developer y la orden checkout, o puedes ir directamente a editar checkouts.cfg. Nosotros recomendamos el último pero describirá ambos. Al final, checkouts.cfg tiene que ser configurado cualquier manera así que también podrías empezar allí.

En la base de su buildout, abra el archivo checkouts.cfg y añada su paquete si no es ya allí::

  auto-checkout =
          # mi paquetes modificados 
          plone.app.caching
          plone.caching
          # otros
          ...

Entonces ejecutar de nuevo buildout para conseguir los paquetes de sus repositorios fuente::

  > ./bin/buildout

Alternativamente, nosotros podemos administrar los checkouts desde la línea de comando, usando el comando de mr.developer ``bin/develop`` para conseguir la fuente de paquetes más reciente. Por ejemplo, si la incidencia es en los paquetes plone.app.caching y plone.caching::

  > ./bin/develop co plone.app.caching
  > ./bin/develop co plone.caching
  > ./bin/buildout

No olvide volver a ejecutar buildout! En ambos métodos, mr.developer descargará la fuente de github (o de donde se definió) y poner el paquete en el directorio src. Usted puede repetir este proceso con tan muchos o cuando pocos paquetes cuando necesite. Para algunos más consejos en la forma de trabajo con mr.developer, por favor :doc:`lea mas aquí <mrdeveloper>`.

Probando localmente
-------------------
En un mundo ideal, usted debería escribir un caso de prueba para su incidencia antes de tratar de corregirlo. En realidad esto rara ves sucede. Ningún asunto cómo  te lo acercas, usted tiene que SIEMPRE probar la ejecución de los test cases para ambos el módulo y plone.org antes de que generar una revisión con cualquiera de cambios. 

Si usted no comienza con un caso de prueba, se ahorrará problemas potenciales y validar el fallo antes de llegar demasiado profundo en la incidencia!

Para correr una prueba para el módulo específico ejecute el siguiente comando::

  > ./bin/test -m plone.app.caching

Estos deberían ejecutarse todo sin fallos. Por favor, no verifique ninguna cosa adicional! Si usted no lo ha escrito ya, este es un buen momento para escribir un caso de prueba para la falla que usted está reparando y asegúrese de que todo está funcionando como debería.

Después de las pruebas de nivel de módulo se ejecutan con su cambio realizado, por favor asegúrese de que los otros módulos no se ven afectados por su cambio realizado, para esto ejecute todas as pruebas con el siguiente comando::

  > ./bin/alltests

*Nota*: Las pruebas toman un tiempo en ejecutarse. Una ves se allá convertido en el maestro de corrección de fallas, usted tal ves le deje al servicio de jenkins hacer esta tarea por usted. Más sobre esto a continuación.

Actualizar el archivo CHANGES.rst y checkouts.cfg
-------------------------------------------------
Una ves todo las pruebas se ejecuten localmente en si maquina, usted debe estar CASI listo para generar una revisión de sus cambios. Un par de cosas hay que hacer antes de continuar. 

Primero, por favor edite el archivo CHANGES.rst (o CHANGES.txt) en cada archivo que usted modifico y agregue un resumen de sus cambios en base al formato que usa este archivo. Esta nota de cambio será cotejada para la próxima versión de Plone y es importante para los integradores y desarrolladores.

*Lo más importante*, si no lo hizo antes, edite el checkouts.cfg en el directorio de buildout y agregar el paquete al cual le hizo sus cambios a la lista de auto-checkout. Esto le permite al administrador de la versión saber que paquete ha sido actualizado para que cuando sea la próxima versión de Plone tendrá que fijar a la próxima versión del paquete al momento de generar un nuevo paquete Egg. LEER: esto es como su corrección viene en un paquete egg! 

Tenga en cuenta que hay una separador de sección llamada "# Test Fixes Only". Asegúrese que su paquete egg este por encima de esa línea o su paquete egg probablemente no se hizo muy rápidamente. Este dice al administrador de la versión que los paquetes Egg por debajo de esta línea tienen pruebas que están actualizadas, pero no hay cambios en el código.

Modifique el archivo checkouts.cfg también ejecute el buildbot, entonces el servicio jenkins, actualizara el paquete egg y ejecutara todas las pruebas contra las pruebas que usted realizo. No sea que alguna vez volvería a sáltate ejecutar todas las pruebas, por supuesto... Más sobre esto a continuación.

Si su fallo esta en mas de una publicación (ej. 4.1 y 4.2), por favor, aplicar sus cambios en ambas branches y añadir al archivo checkouts.cfg.

Generando una revisión y haciendo Pull Requests
-----------------------------------------------
¡Uf! Estamos en la recta final. Verifique su lista de actividades hechas en los últimos minutos:

 * ¿Usted corrigió el fallo original?
 * ¿Su código consiste con nuestro :doc:`style`?
 * ¿Usted removió lineas extras de código y PDB persistentes?
 * ¿Usted escribió un caso de prueba para su fallo?
 * ¿Todos sus casos de prueba para los módulos y para Plone se ejecutan sin ningún problema?
 * ¿Usted actualizo el archivo CHANGES.rst en cada paquete que usted modifico?
 * ¿Usted añadió sus paquetes cambiados al archivo checkouts.cfg?

Si usted respondió SI a todas estas preguntas, usted esta listo para presentar sus cambios! Un par de recordatorios rápidos:

 * Solamente generar una revisión directamente a la branch de desarrollo si usted esta seguro que su código no causa ninguna falla y los cambios son pequeños y triviales. De lo contrario, por favor, haga un fork del repositorio aplicando sus revisiones allí y luego haga un pull request (mas abajo se explica como).
 * Por favor, trate de hacer un cambio por cada revisión. Si usted esta corrigiendo tres fallas, haga tres revisiones. De esta forma, es fácil ver que fue cambiado y donde se realizo el cambio, además es mas fácil hacer un roll back de cualquier cambio si es necesario. Si usted quiere hacer muchos cambios sobre limpiar espacios en blanco o renombrar variables, es especialmente importante hacer una revisión separada por esta razón.
* Nosotros tenemos un grupo de ángeles que siguen los cambios y cada revisión aplicada para ver que ha sucedido de nuevo en el código fuente de nuestro favorito CMS! Si su revisión tiene algo REALMENTE sketchy, ellos le contactaran políticamente a usted, lo mas común que suceda es que inmediatamente revierten los cambios aplicados con sus revisiones. Hay personas no oficiales asignadas a esto si usted esta especialmente nervioso, entre en el canal IRC en freenode.net y pregunte por alguien que pueda ver sus cambios.

Generando revisiones al paquete Products.CMFPlone
-------------------------------------------------
Si usted esta trabajando un corregir un fallo en el paquete Products.CMFPlone,
hay un par de otras cosas que debe tomar en cuenta.
Primero y mas importante, 
puede ver que este paquete tiene varias branches.
Al momento de escribir este documento,
habían tres branches para 4.1, 4.2, y master, el cual es implícitamente 4.3.

Aun me sigue? Entonces usted tiene un corrección de falla para 4.x.
Si la corrección es solamente para una versión,
asegúrese de obtener la branch y aplicar sus cambios allí.
Sin embargo, si la corrección del fallo es en múltiples branches. 

Por ejemplo el fallo inicia en la versión 4.1. Obtenga la branch 4.1 y aplicar sus cambios allí con varias revisiones por cada cambio con sus respectivos tests.

Su su corrección involucra una simple revisión de cambios,
usted puede usar el comando git ``cherry-pick`` para aplicar la misma revisión
a un branch diferente.

Primero cambie a la branch::

  > git checkout 4.2

Y entonces con el comando git cherry-pick y el número de revisión (usted puede obtener el número SHA hash desde el git log).

  > git cherry-pick b6ff4309

Tal ves allá conflictos; entonces, resolverlos y seguir las instrucciones 
que la herramienta git le da a usted para completar el cherry-pick.

Si su corrección involucra múltiples revisiones, cherry-picking entonces uno a uno puede resultar tedioso.
En este caso las cosas son más fáciles si usted hizo su corrección en una branch con una característica separada.

En ese escenario, primero fusiones la branch característica a la branch 4.1::

  > git checkout 4.1
  > git merge my-awesome-feature

A continuación, regrese a la branch característica y haga una branch para `establecerlo` dentro de la branch 4.2::

  > git checkout my-awesome-feature
  > git checkout -b my-awesome-feature-4.2
  > git rebase ef978a --onto 4.2

(ef978a pasa a ser la ultima revisión en el histórico de la branch característica antes
de que sea bifurcaba de la versión 4.1. Usted puede mirar el histórico de su repositorio git para encontrar este.)

Al llegar a este punto, la historia de la branch característica ha sido actualizada, pero no ha sido de hecho 
fusionada con la versión 4.2 aún. Este le permite a usted resolver conflictos antes de que usted
lo fusione a la branch release 4.2. Hacerlo ahora así::

  > git checkout 4.2
  > git merge my-awesome-feature-4.2


Branches y Forks y Hacer revisiones directamente - ¡Por Dios!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Plone uso un repositorio svn, así que todo el mundo es familiar y acostumbrado a hacer revisiones directamente a las branches. Después de que la migración de los repositorios svn al servicio github, la comunidad decidió mantener este espíritu. Si usted ha firmado el contributor agreement, puedes cometer directamente a la branch (para plone esto sería la versión del branch ej. la branch 4.1, para más otros paquetes esto sería el branch llamado master).

NO OBSTANTE, hay unas cuantas situaciones donde una hacer un nuevo branch es apropiado. Si usted:
 * usted se esta iniciando, 
 * usted no esta seguro acerca de sus cambios
 * quiere revisión de comentario/código
 * están llevando a cabo un cambio no trivial

Entonces probablemente quieres crear una branch de cualquier paquete que está utilizando y entonces use la característica de pull request del servicio github para conseguir revisión. Todo acerca de este proceso sería el mismo, excepto que necesita para trabajar en una branch. Tome de ejemplo el paquete plone.app.caching. Después de comprobarlo con mr.developer, cree su propia branch con::

  > cd src/plone.app.caching
  > git checkout -b my_descriptive_branch_name

*Nota*: Hacer Branch o fork es su elección. Yo prefiero hacer branch, y yo estoy escribiendo la documentación en esto usando el método de branch. Si usted hace un branch, nos ayudo porque nosotros *sabemos* que tienes permisos para aplicar revisiones a este branch. De cualquier forma, es tu decisión.

Proceda como de costumbre. Cuándo usted este a punto para hacer push de la corrección de su fallo, debe hacer un push a una branch remota con el siguiente comando::

  > git push origin my_descriptive_branch_name

Esto hará un branch remoto en el servicio github. Vaya a esta branch de la interfaz de usuario github y en la parte superior derecha habrá un botón que dice "Pull Request". Este le permitirá hacer una solicitud dentro de un pull request en la branch principal. Hay personas que se ven una vez a la semana o más para revisar las solicitudes pull requests y confirmaran si es o no es una buena corrección y le dará una retroalimentación cuando sea necesario. Los revisores son informales y muy agradables, así que no se preocupe - que están ahí para ayudar! Si usted quieres retroalimentación inmediata, valla a la sala IRC con el enlace de pull request y pedida una revisión.

*Nota*: todavía necesitas actualizar el archivo *checkouts.cfg* en las branches correctas de proyecto buildout.coredev!

Jenkins
-------
Usted TODAVÍA no está listo! Por favor, compruebe que el servicio jenkins se asegure que sus cambios no hallan roto cosas. Se ejecuta cada media hora y tarda un rato para ejecutar la comprobación en una hora es una apuesta segura. Ten una cerveza y tu mirada sobre el `panel de control Jenkins <https://jenkins.plone.org/>`_.

Finalizando Tickets
-------------------
Si usted esta trabajando de un ticket asignado, por favor no olvide en volver a actualizar el ticket y agregar un enlace a sus revisión de cambios. Actualmente no tenemos una integración de nuestro sistema de ticket con el servicio github pero es una forma agradable de seguir sus cambios. Eso también le permite al reportero saber que usted preocupa. Si el fallo es realmente mala, considere en contactar al release manager y he invitarle a hacer un pronto lanzamiento.

FAQ
---
 * *¿Cómo puedo saber si se tomo mis cambios en mi paquete?* 
    Usted puede seguir el proyecto en github y mirar la linea del tiempo de cambios. Usted también puede descargar el CHANGES.txt de cada liberación de Plone para ver una lista comprensible de todos los cambios y validar que su contribuciones estén presente.

