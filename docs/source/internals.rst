Internals
*********

This is were internals are documented.

Context
=======

A context is created for each processed file in the content directory. The
context contains all data about an output file.

Keys in the context
-------------------

settings
   All settings used to generate the site
   
contents
   A list of all content.

   metadata
       The meta data for the page.
   
   html_content
       The HTML rendered from the input file.
   
   html
       The final HTML from the content rendered through a template

Writer
======

.. automodule:: ssg.writer
   :members: