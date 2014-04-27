Internals
*********

This is were internals are documented.

Context
=======

A context is created for each processed file in the content directory. The
context contains all data about an output file.

Keys in the context
-------------------

metadata
    The meta data for the context.

content
    The HTML rendered from the input file.

settings
   All settings used to generate the site

html
    The final HTML from the content rendered through a template

Writer
======

.. automodule:: ssg.writer
   :members: