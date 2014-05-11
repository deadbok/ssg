author: ObliVion
date: 2013-09-24 19:45
slug: nrf24l01-and-the-ti-msp430-and-stellaris-launchpads
tags: Microcontroller, MSP430 Launchpad, NRF24L01, Stellaris Launchpad
title: NRF24L01 and the TI MSP430 and Stellaris Launchpads
type: post


When using the Enrf24 library with Enegia these are the connections for
the NRF24L01 module.

!{NRF24L01 Module pin-out}($LOCALURL/nrf24l01_pinout.jpg)
<br style="clear: both;" />

 NRF24L01 | MSP430 | Stellaris
 ---------|--------|----------
 GND      | GND    | GND
 VCC      | VCC    | VCC
 CE       | P2.0   | PE1
 CSN      | P2.1   | PE2
 SCK      | P1.5   | PD0
 MOSI     | P1.7   | PD3
 MISO     | P1.6   | PD2
 IRQ      | P2.2   | PE3
 
