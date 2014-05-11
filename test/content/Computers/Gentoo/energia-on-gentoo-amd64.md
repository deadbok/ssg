author: ObliVion
date: 2013-04-15 15:47
slug: energia-on-gentoo-amd64
tags: arduino, Energia, Gentoo, Microcontroller, MSP430 Launchpad, Stellaris Launchpad
title: Energia on Gentoo amd64


Energia IDE
===========

I never really caught on to the Arduino craze, not because of any
dislikes as such, but because I was familiar with Microchips PICMICRO
range. I had the parts, the programmer, and the knowledge to program
them in both asm and C, so I guess I have had no need for the Arduino
platform.

It turns out that the Arduino IDE has been ported to both the [Stellaris
Launchpad](http://www.ti.com/tool/ek-lm4f120xl), and the [MSP430
Launchpad](http://www.ti.com/ww/en/launchpad/msp430_head.html) from
Texas Instruments. and is called [Energia](http://energia.nu/). This is
nice, since it is then quite easy to port the vast amount of sketches
and libraries from the Arduino IDE to Energia IDE and the Texas
Instruments Launchpads.

Getting it going on Gentoo Linux
================================

First to run Energia, 32-bit java support is needed, so

    app-emulation/emul-linux-x86-java

needs to be emerged. When running Energia you must make sure

    emul-linux-x86-java-1.6

is selected as user VM with eselect. Create a file called
/etc/udev/rules.d/62-stellarpad.rules with these contents:

    ATTRS{idVendor}=="1cbe", ATTRS{idProduct}=="00fd", MODE="0660", GROUP="plugdev"

Reload udev and add yourself to the "plugdev" group, plug-in in the
Launchpad and you should be good to go!
