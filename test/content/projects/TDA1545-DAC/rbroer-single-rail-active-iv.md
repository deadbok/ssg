author: ObliVion
date: 2008-06-03 22:16
slug: rbroer-single-rail-active-iv
tags: DAC, I/V, NONOS, TDA1545
title: rbroer Single rail, active I/V
type: post

!{Testing}($LOCALURL/tda1545-dac-i-v.jpg)
Tonight I finished an active I/V stage for the TDA1545 DAC. Up until
now I have used a resistor I/V for both my TDA1543 and TDA1545 DAC, this
has some undesirable effects as the current output of the DAC should be
looking into a very low value resistor, and a fairly high valued one is
needed to get a deecent voltage output
([http://members.chello.nl/~m.heijligers/DAChtml/Analogue/IV.html](http://members.chello.nl/~m.heijligers/DAChtml/Analogue/IV.html)).
Besides presenting a better impedance to the current output of the
TDA1545, the active I/V stage also brings the output to about 2Vpp, in
it's current configuration. The I/V stage was designed by "rbroer" of
diyAudio, the original thread is here: [Single rail, active I/V for
TDA1543,
TDA1545A](http://www.diyaudio.com/forums/showthread.php?s=&threadid=28144&perpage=50&pagenumber=1).

The sound with the active I/V is definitely better. My test setup is a
long way away from my stereo, therefore the DAC has to drive a 20 meter
long cable, which has always led to a "muffled" sound. Since the active
I/V has better current and voltage driving capabilities, this is now
gone. This is a wonderful experiences, no magic, simple logic, that
manifests itself, in the way I would have expected. Everything is firm
and in control. As far as I can see this can only improve things, even
when the DAC is back in place, with a half meter of cabling.

I will post a the relevant layout files, when I have finished testing
and tweaking.
