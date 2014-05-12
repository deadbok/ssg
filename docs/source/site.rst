Site
****
*The site is everything.* The site is where all the files it takes to build the 
final static site, reside. 


Steps when building a site
==========================

 - Create context
 - Convert Markdown files from the `content` directory to HTML.
 - Generate additional meta data.
 - Run any enabled meta extensions.
 - Run any enabled content filters.
 - Run any enabled generators.
 - Apply Jinja2 templates from `template` directory to the context.
 - Write the generated HTML files
 - Copy anything else from the content directory
 - Delete anything else that is not in the content directory, from the output
   directory


Directories
===========

These are the directories used in the default configuration

content
   Everything in this directory is either processed or copied directly to the
   output directory.
output
   Where the generated site lives.
templates
   Jinja2 templates.

.. _configuration:

Configuration
=============

.. automodule:: ssg.settings
