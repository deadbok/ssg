Introduction
============

Static site generator is a toy of mine, since many python static blog 
generators are pretty large, and intimidating. This is an exercise to make a
simple framework for static site generation. On top of this a blog engine is
appearing.

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

.. _Markdown: http://daringfireball.net/projects/markdown
.. _Jinja2: http://jinja.pocoo.org/