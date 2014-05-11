author: ObliVion
date: 2008-04-28 23:02
slug: timer1-and-real-time-clock
status: hidden
tags: Accelerometer, PICMicro, real time clock, RTC, Timer1
title: Timer1 and real time clock


 

After reading through all the timer options in the
[PIC18F2550](http://www.microchip.com/stellent/idcplg?IdcService=SS_GET_PAGE&nodeId=1335&dDocName=en010280),
I decided to go for an external watch crystal hooked up to Timer1. I
cracked open an old watch of mine, and got the crystal. I now have a
simple ISR toggling a LED every second. This way, I can have a the clock
counting even if the PICMicro is in low power mode. I will continue to
test this option, as it seems easier, and cheaper, than using and
external real time clock.
