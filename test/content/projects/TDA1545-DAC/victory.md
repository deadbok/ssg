author: ObliVion
date: 2008-04-17 14:24
slug: victory
tags: DAC, diy audio, NONOS, TDA1545
title: Victory!
type: post


Finally after a thousand cups of coffee (for me that is) it is actually
playing music again. This time through the last TDA1545 DAC chip that I
haven't destroyed. This is a clone of the
["Monica"](http://diyparadise.com/dacs.html) DAC. I can not comment that
much on the sound, since it has been a while since the TDA1543 DAC, was
playing, but it sounds nice, and definitely different. If you have some
spare chips and time, try it for yourself.

 

!{The schematic}($LOCALURL/TDA1545DIL8_NONOS_DAC_sch.jpg)

In the final version, R1 is 33k, and C7 has been omitted. C7 seemed to
be the part causing the 2 DAC chips to die, I'm not sure why, and I'm
not sure the final solution is to leave it out, but since I'm at my last
chip, It'll stay that way for a while. Also check the output from the
current source between R4 and D1, if above 6V, short out D1, D4, and D7.

 
!{PCB layout}($LOCALURL/TDA1545DIL8_NONOS_DAC_pcb.jpg)

[TDA1545 NONOS DAC Cadsoft eagle project files]($LOCALURL//TDA1545DIL8%20NONOS%20DAC.zip)

[TDA1545 Datasheet]($LOCALURL//TDA1545AT.pdf)
