author: ObliVion
date: 2010-06-26 23:29
slug: lab-power-supply-taking-shape
tags: discrete, Electronics, Linear Regulator, positive voltage regulator, power supply, prototype
title: LAB Power Supply taking shape
type: post


!{Prototype}($LOCALURL/DSC002241.jpg)
<br style="clear: both;" />

A have had an old untrustworthy 317/337 based power supply as my test
unit, since it was build in 1987. Over the years I have tried to improve
the poor thing, at first, without really knowing enough, to improve
anything. It has come to the point, where I blame this unit for a lot of
things, that might as well be faults, in the circuits I am testing.

I have been working from these specifications:

-   Easily adaptable to higher voltages (and currents)
-   Input voltage about +/- 22V
-   Variable output voltage between about  +/- 2- 20V
-   Output current limit at about 1A
-   Adjustable with a single multi-turn pot
-   Predictable performance
-   Readily available parts (what I had lying around)
-   The new PCB must fit in the place of the original, with only a
    modest level of violence.
    

I have been through some op-amp and/or 317/337 based designs, but they
all failed in different ways. In the end I am prototyping the following
circuit.
!{Prototype power supply schematic}($LOCALURL/tested-I.png)
<br style="clear: both;" />

The whole thing works in the perfect world of spice, and the coloured
parts has been tested as the prototype seen at the top of this post.
Since I have designed this from scratch, I will describe the circuit,
but first lets take a look at a functional block diagram of a standard
linear voltage regulator, from [National Semiconductor Application Note
1148](http://www.national.com/an/AN/AN-1148.pdf):
!{Standard 3-pin voltage regulator block diagram}($LOCALURL//standard-vreg-block-AN1148.png)


The positive side of my circuit is mostly a discrete implementation of
the above. VREF equals A in the schematic below, the error amp is
section B. The pass transistor is the darlington Q1, Q2, in block C,
these are connected a little different than the block diagram above,
mostly to save parts, and make life easier for myself in the current
limiting department. Voltage divider R1, R2 equals the voltage divider
R4, R7 in block D below.
<br style="clear: both;" />

1
:   is a twist on a standard zener reference. R2, D1, R5, and C4 is the
    standard circuit, only it is not connected to ground. R2 limits the
    current through D1, and could easily be increased, I would suggest
    3.9kΩ for a current of about 5mA through D1. R5 and C4 is there to
    filter out zener noise. D2 and R11, forms a negative counterpart, to
    D1 and R2, and I would suggest 3.9kΩ for R11. The junction between
    D2, and R11 is at -5.6V due to D2. Q9 is there to buffer the -5.6V
    from D2 and R11, due the 0,65V drop in Q9, the emitter voltage is
    about -5.6V+0.65V=-4.95V. C5 and R10 is a filter just like C4 and
    R5. D1 is referenced to the -4.95V, instead of the usual ground
    connection, this means that the junction between R2 and D1 should be
    at a stable -4.95V+5.6V=0.65V, which serves as a reference voltage,
    
2
:   is a simple differential amplifier in place of an op-amp. The
    transistor version was chosen, since most op-amps have a maximum
    supply rating of 36V. With the BJT version, scaling to a higher
    voltage, is a simple matter of choosing the right transistors for Q4
    and Q5. In my prototype I have used BC337 types. One of the inputs
    of the differential amplifier is connected to the reference voltage
    from R2, D1, through the filter R5 and C4. The other input is taken
    from the voltage divider R4, R7, which is a fraction of the output
    voltage. The output is taken between the collector of Q5, and R3.

3
:   is the pass transistor, the difference signal from block B, which is
    the difference between the reference voltage, and an adjustable
    fraction, of the output voltage, is used to control the voltage drop
    of Q1. Q2 makes this a darlington transistor with a current gain
    large enough, that the difference amplifier can drive it at maximum
    current load, on the power supply output.

4
:   is a simple voltage divider, the difference amplifier will adjust
    the output voltage, via Q2, Q1, to make the voltage at the
    connection between R4 and R7 equal to the reference voltage from A.
    R4 is the pot on the front panel, and R7 is a trimmer for initial
    fine tuning.

!{LAB Power Supply functional blocks}($LOCALURL/block-sch1.png)

This is as far as I have gotten until now. I will describe the rest of
the circuit as it is prototyped. For now this is a positive supply
adjustable from 0.70V to 6,6V running off a couple of 9V batteries.
