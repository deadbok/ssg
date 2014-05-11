author: ObliVion
date: 2008-09-02 20:13
slug: firmware-ready
tags: Firmware, input selector, PIC16F628A, PICMicro, relay control
title: Firmware ready
type: post


The firmware for the DAC input selector has been debugged extensively,
and now seems ready for real life testing. The source is here: 
[SPDIF input selector source]($LOCALURL/SPDIF-input-selector.tar.gz).
The firmware has a manual, and an automatic selection mode.

-   If the button is pushed for less than about 2 seconds, the selector
    enters manual mode, and skip to the next input.
-   If the button is held for longer that 2 seconds, the firmware scans
    each input for one second and selects the first input that has data
    (audio).

The firmware works by sniffing the I2S data line to the DAC, to see if
anything is going on there. To prevent the DAC from playing anything,
before an input is selected, a relay has been added to the DAC board, to
only enable the I2S data line to the DAC, when a signal has been
selected.

When the project is finished the compiled firmware will be made
available along with the rest of the design files.
