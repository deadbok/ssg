author: ObliVion
date: 2008-05-13 03:11
slug: inverse-riaa-in-pspice
tags: Inverse RIAA, Phono preamplifier, simulation, Spice
title: Inverse RIAA in PSpice
type: post


I have been looking for a way to simulate an inverse RIAA network in
spice, After using a passive discrete simulation for a while, i found
this: [How to calculate RIAA
correctly?](http://www.diyaudio.com/forums/showthread.php?postid=849619#post849619)

Using the ELAPLACE part in OrCAD PSpice, changing the XFORM paramter to
this

   (1+3180u\*s)\*(1+75u\*s)/((1+318u\*s)\*(1+3.18u\*s))\*

And everything works like a charm.
