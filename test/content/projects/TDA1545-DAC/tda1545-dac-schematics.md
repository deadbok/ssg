author: ObliVion
date: 2010-05-20 21:40
slug: 319
tags: DAC, diy audio, Final design, Microcontroller, NONOS, PIC16F628A, PICMicro, shunt regulator, TDA1545, TL431
title: TDA1545 DAC schematics
type: post


I have gathered together the schematics for the non oversampling TDA1545
DAC. Mind that I am only responsible for the shunt regulators, the
microcontroller, and the input selector. The digital input circuitry was
developed after reading [some post from Jocko Homo on the diyhifi.org
forum](http://www.diyhifi.org/forums/viewtopic.php?p=5707#p5707). The
TDA1545 circuit is mostly from the Philips [data
sheet](http://groenholdt.net/wp-content/uploads/file/TDA1545AT.pdf). The
I/V stage is [from rbroer on
DIYAudio](http://www.diyaudio.com/forums/digital-line-level/28144-single-rail-active-i-v-tda1543-tda1545a.html?perpage=50&pagenumber=1).

At some point in time I have made the following block diagram, and from
memory it seems correct.
!{TDA1545 NONOS DAC block diagram}($LOCALURL/TDA1545-NONOS-DAC-block.png)
<br style="clear: both;" />

From the top here is the input selector board, the micro controller for
the relays are on a second board, as per the block diagram.
!{Digital input selector]($LOCALURL/Digital-input-selector-cs8412.png)
<br style="clear: both;" />

After the relays, comes the SPDIF buffer/amplifier circuit based on
Jocko Homo's. The CS8412 converts the SPDIF signal into the correct I2S
format, I2S data goes both to the DAC board, and the micro controller
board. The micro controller signal is buffered by one of the 7404
inverters, in the hopes that any noise from the micro controller, will
be isolated.

The shunt regulators, are duplicates of the similar valued ones in the
shunt regulator schematic, you do not need to build these twice!

Here is the DAC circuit.

!{TDA1545 NONOS DAC schematic}($LOCALURL/TDA1545DIL8-NONOS-DAC-II.png)
<br style="clear: both;" />

Everything is in the puzzling Philips data sheet. The relay shuts off
the data, while the micro controller scan through the inputs.

Here comes the shunt regulators
!{Shunt Regulators}($LOCALURL/shuntreg.png)


The one at the bottom is the one for the DAC, and the one that is not
duplicated on the input selector board.
<br style="clear: both;" />

Here comes the I/V from rbroer, which is fed from the unregulated DC
supply.

!{rbroer I-V}($LOCALURL/rbroer-i-V.png)
<br style="clear: both;" />

And the micro controller schematic.

!{Digital input selector microcontroller board}($LOCALURL/Digital-input-selector-ucD-board.png)
<br style="clear: both;" />

I have redesigned the PCB layout's without saving the ones I used in the
working DAC. Therefore they have not been tested, and I would rather not
publish them, and have them blow up in some poor persons face.
