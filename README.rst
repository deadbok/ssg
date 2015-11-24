Static Site Generator
=====================

.. image:: https://codeclimate.com/github/thoughtbot/paperclip/badges/gpa.svg
   :target: https://codeclimate.com/github/thoughtbot/paperclip
   :alt: Code Climate

Introduction
============

Static site generator is a toy of mine, since many python static blog 
generators are pretty large, and intimidating. This is an exercise to make a
simple framework for static site generation. On top of this a blog engine has
been written.

Static Site Generator basics
----------------------------

In its most basic form Static Site Generator (hereafter ssg), takes a bunch of
files written in `Markdown`_ and converts them into HTML files.

There is more to it though. After converting the `Markdown`_ into HTML, the whole
thing is processed by the `Jinja2`_ template engine.
A lot can be done solely in the `Jinja2`_ templates, but some steps in the
conversion can be hooked into, by extending ssg. I test ssg
on my blog, the engine is made by extensions to ssg, and `Jinja2`_
templates.

ssg
===
The main Static Site generator executable is called ```ssg```. This is a Python
command line program.

Command line options
--------------------

-d, --debug			Print debug information.
-s, --site_url		Set the site URL.
--write-all			Write all files, instead of updating.
-r, --root			Set the root directory of the site. Default is current 
                  directory.
-c, --create-site	Create a directory skeleton and config file for a new site. 
                  Defaults to current directory.

.. _Markdown: http://daringfireball.net/projects/markdown
.. _Jinja2: http://jinja.pocoo.org/
