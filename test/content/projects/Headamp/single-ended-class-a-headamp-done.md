author: ObliVion
date: 2008-10-07 09:53
slug: single-ended-class-a-headamp-done
tags: Class A, Final design, Headamp, single ended
title: Single ended class A headamp done.
type: post

!{Finished Single ended class A headamp}($LOCALURL/final.jpg)
<br style="clear: both;" />

The beast has been tamed. It sounds good too, although my headphones are
cheap Sennheisers. The headamp is enclosed in a Hammond enclosure, using
the aluminium casing as heat sink, it gets hot. It makes for a nice way
to keep the coffee warm by placing the cup on top of the amplifier.
!{Schematic}($LOCALURL/schematic.png)
<br style="clear: both;" />

Q6, Q8, Q15, and Q17 are the output transistors, and **needs** heat
sinks, I have not calculated the exact size needed, but the bigger the
better. I use the aluminium chassis of a [Hammond
1455N2202](http://www.hammondmfg.com/pdf/1455N2202.pdf) with the
transistors mounted on the bottom, and it gets warmer than I like. Never
test the amp without proper heat sinking in place, as the output section
will most certainly release the precious blue smoke.

**Power supply**I have used a 2X12V toroid, a rectifier bridge, and
4700uf on each supply rail. Each channel draws about 200mA. 

**Grounding**Some attention is advised when wiring the ground, my first
ground layout resulted in a nasty saw-ish 50Hz hum from the amplifier. I
now connect the separate grounds from the input RCA connectors to their
respective ground pads, next to the input pads. The power ground are
connected to a star ground between the 4700uf power supply capacitors,
as well as the ground wire from the headphone jack.

**Files:**
[SE Class A headamp schematic and PCB]($LOCALURL/se-class-a-headamp.pdf)
[SE Class A headamp schematic and PCB (Cadsoft Eagle)]($LOCALURL/se-class-a-headamp.zip)
