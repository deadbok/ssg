author: ObliVion
date: 2008-06-16 20:55
slug: shunt-regulator-and-new-dac-pcb
tags: NONOS, shunt regulator, TDA1545, TL431
title: Shunt regulator and new DAC PCB
type: post
 

I have just assembled and tested the prototype shunt regulator for the
DAC. Inpsite of long wires and veroboard it performs a little better
than the LM317+CSS+diode shunt I've been using so far. When they arrive
I will try replacing the transistors with some low noise BC560 types, to
see if they perform better.

!{Spectrum with the LM317 and CSS diode shunt}($LOCALURL/15_06_08.jpg)
!{Spectrum with the TL431 shunt}($LOCALURL/16_06_08.jpg)
<br style="clear: both;" /> 

The peaks at 50Hz, 100Hz and so forth comes from the SPDIF -\> I2S
converter board, where the PSU has not yet been optimized.

!{The schematic}($LOCALURL/TDA1545DIL8_NONOS_DAC_II_sch.png)
!{The PCB}($LOCALURL/TDA1545DIL8_NONOS_DAC_II_pcb.png)
<br style="clear: both;" /> 
 

[TDA1545 NONOS DAC II Cadsoft eagle project
files]($LOCALURL/tda1545dil8-nonos-dac-ii.zip)
