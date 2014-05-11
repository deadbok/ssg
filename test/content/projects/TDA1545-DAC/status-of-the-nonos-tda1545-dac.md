author: ObliVion
date: 2008-06-03 22:57
slug: status-of-the-nonos-tda1545-dac
tags: NONOS, project, SPDIF, TDA1545
title: Status of the NONOS TDA1545 DAC
type: post
 

Here's a list of things to be done before the final product is posted:

**TDA1545 DAC:**

-   <del>New PCB layout</del>
-   <del>At least testing a better power supply, I'm thinking
    TL431 shunts</del>
-   Try some BC560's in the shunt regulator.
-   Testing some bypass tricks, around 22pf from supply to ground, and
    the same value from Iref to ground

**Active I/V:**

-   <del>Low noise BC550/BC560 transistors instead of BC547/BC557</del>

**SPDIF/I2S converter:**

-   <del>Testing a better power supply for the CS8412, again I'm
    thinking TL431 shunts</del>
-   <del>The SPDIF input circuit is bypassed, figure out why it
    does not work</del>
-   Possibly a new PCB layout

**uC input selector:**

-   Install some bilateral switches to avoid switching the actual signal
    to the DAC before we know there is a signal
-   Ponder on SPDIF signal detection, do I a need to program a PLL?

I know that nothing has been posted about the uC input selector yet.
Basically I'm not the least satisfied with the way I have solved the
problem up until now.

A PIC16F628 switches the input relays, until a signal shows up on the
DATA line of the CS8412. meaning that the actual sound is output from
the DAC as well. I have decided to try measuring at the SPDIF inputs
by using bilateral switches instead. I may have to lock on to the SPDIF
signal to detect audio data. the solution that I'm hoping will do, is to
establish the length of the pulses on the SPDIF line, if there is data,
some pulses should be half the length. I'm yet uncertain as to whether
the preambles will screw this up. If so I will have to detect these.

[Wikipedia on SPDIF](http://en.wikipedia.org/wiki/Spdif)
