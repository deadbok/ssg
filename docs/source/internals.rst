Internals
*********

This is were internals are documented.

Static Site Generator (main)
============================

.. automodule:: ssg

.. autofunction:: ssg.init

.. autofunction:: ssg.process_content

.. autofunction:: ssg.apply_templates

.. autofunction:: ssg.run

Meta data
=========

.. automodule:: ssg.metadata

.. autoclass:: ssg.metadata.MetaParserBase
   :members:
 
.. automodule:: ssg.metaext.categorymetaparser


Content filters
===============

.. automodule:: ssg.contentfilter

.. autoclass:: ssg.contentfilter.ContentFilterBase
   :members:

.. automodule:: ssg.contentfilters.localurl

Context
=======

.. automodule:: ssg.context


Generator
=========

.. automodule:: ssg.generator

.. autoclass:: ssg.generator.GeneratorBase
   :members:

.. automodule:: ssg.generators.blogindex

.. automodule:: ssg.generators.categoryindex

.. automodule:: ssg.generators.tagcloud


Writer
======

.. automodule:: ssg.writer
   :members: