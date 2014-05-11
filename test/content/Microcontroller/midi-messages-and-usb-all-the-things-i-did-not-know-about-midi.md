author: ObliVion
date: 2013-05-20 11:06
slug: midi-messages-and-usb-all-the-things-i-did-not-know-about-midi
tags: MIDI, USB
title: MIDI messages and USB (All the things I did not know about MIDI)
type: post

I am in the process of building a MIDI USB device, using a PIC18F4550. I
have trimmed the [Microchip USB
framework](http://www.microchip.com/stellent/idcplg?IdcService=SS_GET_PAGE&nodeId=2680&dDocName=en537044)
MIDI example, and is using this code as my base. It is a blessing to not
have to code the entire USB stack with descriptors, from scratch, but it
is a pain using someone elses code, and learning to use this framework
as a sort of black box.

The goal is a combined MIDI to USB converter and knob box.

MIDI
====

MIDI is an interface for sending musical notations and messages through
a wire. I will only brush up on the protocol of MIDI in this text.

A MIDI message consists of a status byte and up to 2 data bytes, the
protocol is serial, and runs at 31250 baud. A table with all messages
can be found [here](http://www.midi.org/techspecs/midimessages.php). On
thing that was not obvious to me was that only the bytes needed are
send, no zeroes. As an example an "active sense" message only sends the
status byte. This may seem obvious, but starting from the USB side of
this stuff made it seem otherwise.

Another thing that I wasted a fair amount of time discovering, is
"running status". When you sent the same voice or mode command multiply
times you can omit the status byte from all but the first message.  An
example, you want to sent "note on" on channel 1, key number 60, and a
velocity of 128, when a key is pressed. Then "note on" on channel 1, key
number 60, and a velocity of 0, when a key is depressed. For the second
package you only send the data, e.g. key number 60, velocity 0, the
receiver assumes the status and channel are the same as the first
message.

USB MIDI
========

MIDI packages on the USB cable are 4-byte fixed length packages, unused
bytes are zeroed. The first byte is the cable number (16 virtual cables)
and the Code Index Number, which acts sort of the same as the first 4
bits of a MIDI status. The following 3 bytes are an ordinary midi
message. The standard is
[here](http://www.usb.org/developers/devclass_docs/midi10.pdf).

MIDI to USB MIDI
================

For a long time, a note on page 17 of the USB MIDI standard eluded me. I
thought that since the  Code Index Number almost mirrors the ordinary
status of a MIDI message, I would have to parse and classify every
message coming from the MIDI port. It turns out that you can send each
byte received along without out classifying it, and set the Code Index
Number to 0xF. Using this Code Index Number every byte received on the
MIDI port is simply packaged in a 4 byte package, first 4 bits, the
cable number, then 0xF, then the byte from the MIDI port, and in the end
padded with 2 zero bytes.
