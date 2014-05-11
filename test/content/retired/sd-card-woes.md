author: ObliVion
date: 2008-05-12 21:41
slug: sd-card-woes
status: hidden
tags: 3.3V to 5V, PICMicro, SD card, USB
title: SD Card woes


 

I have been working on merging the code from ["USB Mass Storage Device
Using a
PIC"](http://www.microchip.com/stellent/idcplg?IdcService=SS_GET_PAGE&nodeId=1824&appnote=en024394),
from Microchip. As such things are working, the project board enumerates
as a Mass Storage Device, only there is no communication with the SD
card. The code communicating with the SD card, branches to an error
condition. I hope this is due to my resistor divider level converter, or
the fact that a 3.3V logical signal can only just drive the input pin of
the PIC. This would make sense as there are a lot of wires dangling,
introducing noise, where there is no headroom to start with. Gotta get
my hands on some 74LS125 chips.
