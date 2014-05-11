author: ObliVion
date: 2010-06-29 21:29
slug: current-limiting-circuits-tested
tags: Current limit, Electronics, power supply, prototype
title: Current limiting circuits tested
type: post


This is the final schematic, everything is now tested, and working. Had
a little trouble, until I realized I had put a PNP transistor in place
of Q6.
!{Prototype power supply schematic}($LOCALURL/tested-sch.png)
<br style="clear: both;" />

Refering to the figure in [LAB Power Supply taking
shape]($LOCALURL/projects/LAB-PSU/lab-power-supply-taking-shape.html) 
here is the rundown on the last parts.

5
:   is the current limiting circuit on the positive rail. When the
    voltage across the current sense resistor R1 rises above 0.65V the
    transistor, Q3, will begin to conduct, stealing base current from
    the pass transistor. This will make the output voltage fall, until
    the voltage loss in R1 is back at 0.65V. The value of resistor R1
    sets the current limit, using Ohms law it is easy to calculate
    resistor value for a 1A current limit, (R=U/I), R1=0.65V/1=0.65Ω.
    The closest value is 0.56Ω, which gives a current of
    0.65V/0.56Ω=1.16A.

9
:   is the negative current limiting circuit. Q10 and R14, is the mirror
    circuits of Q3 and R1. Since the negative rail tracks the positive
    one, the negative voltage will drop, when the positive current limit
    kicks in. The positive rail, is not tracking the negative, and the
    positive voltage, will not drop, when the negative current limiter
    kicks in. Arguably, there will be no over-current problem, on the
    positive rail, if the positive current limit is not activated. For
    completeness, Q6 will turn down the voltage of the positive rail,
    when the difference between the positive and negative rail becomes
    large enough to make the voltage at the junction R9, R13 more than
    0.65V

Well it seems the power supply is working, I have made a PCB design,
that I will perfect, and publish when done.
<br style="clear: both;" />

!{Prototype}($LOCALURL/prototype.jpg)


