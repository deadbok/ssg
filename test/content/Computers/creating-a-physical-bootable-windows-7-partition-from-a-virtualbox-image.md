author: ObliVion
date: 2013-02-08 04:22
slug: creating-a-physical-bootable-windows-7-partition-from-a-virtualbox-image
tags: Linux, Virtualbox, Windows
title: Creating a physical bootable Windows 7 partition from a VirtualBox image
type: post
template: post


I will walk through copying a bootable Windows 7 installation from a
VirtualBox VM to real iron.

-   Insert an external hard drive in the USB port and share it with your
    Windows 7 VM.
-   Ask windows to make a system image "Control Panel -\> Back up your
    computer -\> Create system image", and save it to the external hard
    drive.
-   Boot the Windows 7 install disk, click through, and select "Repair
    windows installation". The drives that you do not put on the exclude
    list, will be repartitioned and formatted, so make sure to exclude
    everything you want to keep.
-   Let it chew on your backup, and when done, boot Windows.
