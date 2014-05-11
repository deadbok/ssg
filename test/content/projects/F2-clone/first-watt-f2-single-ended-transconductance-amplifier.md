author: ObliVion
date: 2010-05-13 15:36
slug: first-watt-f2-single-ended-transconductance-amplifier
tags: Final design, First Watt F2, Full range driver, MOSFET, Nelson Pass, Power Amplifier, transconductance
title: First Watt F2 single ended transconductance amplifier
type: post


Since I lost all my post on my transconductance amplifier projects, that
ended up in an all N-channel MOSFET version of [Nelson
Pass](http://en.wikipedia.org/wiki/Nelson_Pass) [First Watt
F2]($LOCALURL/prod_f2_man.pdf)
amplifier, I will summarize them here.

!{First Watt F2 single channel first prototype}($LOCALURL/f2-prototype-i.jpg)
<br style="clear: both;" />

The above mess is the first prototype of a transconductance amplifier
like the First Watt F2. It came to life after numerous SPICE simulations
and chewing through OTA datasheets, Pass papers, and forum posts on
DIYAudio.

!{SEAS fullrange}($LOCALURL/seas-fullrange.jpg)
It all started when I began experimenting with open baffle speakers, and
got hold of some vintage SEAS full range drivers. It turned out Nelson
Pass had been experimenting a with this kind of driver, and had written
a paper on the subject.

[Current Source Amplifiers and Sensitive / Full-Range
Drivers]($LOCALURL/cs-amps-speakers.pdf)

In short it seems that some full range drivers will benefit from being
driven by a
[transconductance](http://en.wikipedia.org/wiki/Transconductance)
amplifier. A transconductance amplifier is a voltage to current
converter with amplification. Our standard power amplifiers, are mostly
voltage amplifiers, and will vary the voltage to the load, according to
the input voltage. A transconductance amplifier will vary the current to
the load, according to the input voltage. For a purely resistive load,
this makes no difference as I=U/R, but a loudspeaker is not a purely
resistive load. It is actually the current through the voice coil, that
controls the force of the generated magnetic field, not the voltage.
Because of this, a variable current source seems the most sensible way
to drive a speaker. There is a catch though, since most amplifiers, are
voltage amplifiers, most n-way speakers have their crossover designed
for voltage drive, and will behave wrong, when driven by current. Nelson
Pass has written a paper on how to design filters for transconductance
amplifiers instead, I have not studied this very hard, since I am
building this for full range drivers.

[Current Source Crossover Filters]($LOCALURL/cs-xover-networks.pdf)
<br style="clear: both;" />

Nelson Pass had designed both his First Watt F1 & F2 as transconductance
amplifiers, since I have a bag of IRF640 N-channel MOSFET's. I ended up
modifying the F2 ([First Watt F2 schematic]($LOCALURL/f2-service-manual-sm.pdf)),
to use only N-channel MOSFET's and added a simple regulator, from Nelson
Pass ZEN series.

!{First Watt F2 final prototype}($LOCALURL/f2-final-i.jpg)

The resulting sound, was good. Despite the two fans needed to keep the
amp from burning a hole in the table, that it was lying on (class A,
silver, custom made mains cord, 300B, nuclear reactor in the kitchen,
mumble mumble). Despite the crude boxes the SEAS drivers had to put up
with. Despite the insane amount of distortion, compared to most
amplifiers. I have not tested this, but believe I can hear a change to
the better, when driven with this amplifier. I have not yet tried
correcting the speaker response as per Mr. Pass papers. I have simply
decided that it sounded so well I want to finish it, and play with it
some more along the way.

!{First Watt F2 schematic}($LOCALURL/firstwatt-f2-sch1.png)

!{First Watt F2 supply schematic}($LOCALURL/firstwatt-f2-supply-sch1.png)
