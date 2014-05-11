author: ObliVion
date: 2012-08-08 19:50
slug: configuring-simulavr-on-gentoo
tags: avr, Gentoo, Linux
title: Configuring simulavr on Gentoo


On Gentoo I needed to point the configure script at libbfd.so. On my
system it is in `/usr/lib/binutils/x86\_64-pc-linux-gnu/2.22/` hence:

    ./configure --prefix=/usr/local/ --with-bfd=/usr/lib/binutils/x86\_64-pc-linux-gnu/2.22/
