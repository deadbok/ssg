Site
****
*The site is everything.* The site is where all the files it takes to build the 
final static site. 


Steps when building a site
==========================

 - Convert markdown files from the `content` directory to HTML.
 - Generate additional meta data.
 - Apply Jinja2 templates from `template` directory to the generated HTML and
   meta data


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


.. automodule:: ssg.settings