.. -*- coding: utf-8 -*-

Mr. Roboto
==========

Push en Github
--------------

Cuando sucede un push en Github, ``mr.roboto`` es disparado para iniciar el análisis del ``push``. 

* Si está en ``buildout-coredev`` se inicia el trabajo de la rama que ha hecho ``push``. En este caso nosotros enviamos a la lista plone-cvs el commit para cuidar el track de los commits en esa lista.
* Si está en un paquete que está en el archivo :file:`sources.cfg` de un ``buildout-coredev`` inicia los trabajos ``coredev`` que están vinculados a ese paquete y una tarea de trabajo *known good set - kgs* con ese paquete. Este trabajo kgs es una instantánea de la última versión de trabajo del ``buildout.coredev`` con la versión más reciente del paquete que está involucrado en el ``push``. Estos tareas de trabajo son muy rápido, ya que sólo probamos si el paquete ha aplicado al con el conjunto de versiones de paquetes bien conocidas (kgs) de plone / python de la configuración buildout del ``coredev``.
* Si está en una especificación plip que ejecuta el trabajo que está configurado A través de la Web en la interfaz de ``mr.roboto``. (http://jenkins.plone.org/roboto/plips)

Tareas acabadas
---------------

Cuando jenkins terminar un trabajo que hace una devolución a ``mr.roboto`` con el fin de:

* Si se trata de una tarea de trabajo ``coredev`` de toda las tareas del ``coredev`` relacionados con ese ``push`` que ha acabado, escribe un comentario sobre el commit github con toda la información (una vez y con toda la información así que no hay correos más vacías de sistema de notificación de GitHub)
* Si se trata de una tarea de trabajo kgs y se acaban todas las tareas de trabajos kgs (que puede tomar un máximo 10 minutos) y algunos ha fallado nosotros enviamos un correo electrónico a la lista de correo testbot diciendo que un commit fallo en una tarea de trabajo kgs. También nosotros enviamos un correo electrónico a la lista `plone-cvs <https://lists.sourceforge.net/lists/listinfo/plone-cvs>`_ con la información para realizar un seguimiento de todos los commits.
* Si se trata de una tarea de trabajo kgs y todos los trabajos kgs ha finalizado y todos están trabajando nosotros enviamos un correo electrónico a la lista `plone-cvs <https://lists.sourceforge.net/lists/listinfo/plone-cvs>`_ con la información para realizar un seguimiento de todos los commits.

Para todos los trabajos de construcción kgs de jenkins envía un correo al autor con los resultados cuando se termina.

Todas las notificaciones tiene una dirección URL como :
http://jenkins.plone.org/roboto/get_info?push=9a183de85b3f48abb363fa8286928a10

en esta dirección url existe el commit, quien, el diff, los archivos y el resultado de cada trabajo de Jenkins.

Entonces ...

* La lista de correo electrónico `plone-testbot <http://lists.plone.org/mailman/listinfo/plone-testbot>`_ está recibiendo sólo cuándo una prueba falla en entorno de kgs y puede tomar máximo de 10 minutos del push. 
* La lista de correo electrónico `plone-cvs <https://lists.sourceforge.net/lists/listinfo/plone-cvs>`_ siempre tiene el commit allí con el diff y de la información y puede tomar 10 minutos para llegar allí después del push.
* el autor recibe los resultados de las pruebas que fallan contra KGS en 10 minutos

.. note::
    En caso de errores de integración con otros paquetes que puede fallar debido a los push del kgs no será consciente de ello, por lo que es importante que al final (y después de los 50 que se lleva a los trabajos ``coredev`` que también compruebe la última versión de ``coredev`` con su push)
