How to Update these Docs
========================

These documents are currently stored with the coredev buildout in github in /docs. To update them, please checkout the coredev buildout and update there. To check your changes locally, rerun buildout and then::

  > cd docs/build
  > make html

Sphinx will poop out a file directory that you can put in your browser url to validate. Please make sure to validate all warnings and errors before committing to make sure the documents remain valid.
