author: ObliVion
date: 2010-06-27 18:21
slug: negative-tracking-regulator-tested
tags: Electronics, negative voltage regulator, power supply, prototype
title: Negative tracking regulator tested
type: post


I have tested the negative tracking regulator today, it differs from the
positive regulator, in that it it measures the voltage at the positive
output, and adjusts the negative rail accordingly.
!{Prototype power supply schematic}($LOCALURL/tested-II.png)
<br style="clear: both;" />

Referring to the block diagram in the last post, I will describe the new
blocks.

6
:  is a differential amplifier just like 2. The first input is taken
   from ground, the second from the voltage divider H, that samples the
   midway point between the positive and negative rail. The midway point
   is essentially 0V, as the positive and negative real should have
   equal opposite voltages. The difference amplifier will keep this
   midway point close to zero, by controlling, through the pass
   transistor 7, the voltage of the negative rail.

7
:  is a darlington pass transistor like 3.

8
:  is the voltage divider creating the midway voltage for 6.

Everything is working, and the next step is to test the current
limiters, which is hopefully going to happen at the beginning of next
week.


!{Negative tracking test III}($LOCALURL/DSC00238.jpg)
!{Negative tracking test II}($LOCALURL/DSC00237.jpg)
!{Negative tracking test I}($LOCALURL/DSC00236.jpg)

