Cómo actualizar estas documentaciones
=====================================

Estos documentos actualmente son almacenados con el directorio /docs del buildout de coredev en github. Para actualizarles, por favor, hacer un checkout desde el buildout coredev y actualizar allá. Para generar sus cambios localmente, inicie de nuevo el buildout y entonces::

  > cd docs/build
  > make html

Sphinx colocara en un directorio que tu puedes consultar en tu navegador web para validar la documentacion generada. Por favor asegurese en validar todos los avisos y los errores antes de generar una revision para estar seguro que los documentos queden válido.
