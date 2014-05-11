author: ObliVion
date: 2009-01-28 19:30
slug: converting-a-virtualbox-disk-image-to-kvmqemu
tags: disk image, KVM, VirtualBox, Virtualization
title: Converting a VirtualBox disk Image to KVM/QEMU
type: post
template: post


I had an installation of [Lunar Linux](http://www.lunar-linux.org/),
that I wanted to move from [VirtualBox](http://www.virtualbox.org) to
[KVM](http://kvm.qumranet.com/kvmwiki), and therefore had to convert the
imagefile. I searched high and low, but found no up to date instructions
on how to do this. | In the old days there seem to have existed a tool
called "vditool", but now "VBoxManager" will do the trick of converting
a VirtualBox .vdi image into raw format. Here are the steps that I took:

* Find the UUID of the VirtualBox disk image:
  <pre>oblivion@mastermind ~/.VirtualBox/VDI $$ VBoxManage list hdds 
VirtualBox Command Line Management Interface Version 2.1.2
(C) 2005-2009 Sun Microsystems, Inc.
All rights reserved.
UUID:         e4e316cb-ad9f-46ae-b15c-164b893371cb
Format:       VDI
Location:     /home/oblivion/.VirtualBox/VDI/lunar.vdi
Accessible:   yes
Usage:        Lunar (UUID: d249a972-f112-4cbc-91ce-389ce75e4fac)</pre>

* Convert the .vdi file to raw format, using the UUID just found.
  Using VBoxManage's clonehd function the .vdi file is cloned into a raw
  image, in this case called lunar.img:
  <pre>oblivion@mastermind ~/.VirtualBox/VDI $$ VBoxManage clonehd e4e316cb-ad9f-46ae-b15c-164b893371cb lunar.img -format RAW
VirtualBox Command Line Management Interface Version 2.1.2
(C) 2005-2009 Sun Microsystems, Inc. All rights reserved.
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
Clone hard disk created in format 'RAW'. UUID: 5106c566-7188-4513-a416-73eb7a4e44a9</pre>

* On my Gentoo Linux system, the converted image was saved in
  ~/.VirtualBox/HardDisks.

* Convert the image to QEMU qcow2 format using qemu-img:
  <pre>oblivion@mastermind ~/.VirtualBox/HardDisks $$ qemu-img convert ~/.VirtualBox/HardDisks/lunar.img -O qcow2 lunar.qcow2</pre>


From the utter silence of this command springs lunar.qcow2, ready for KVM!
