MythTV and cifs trouble
#######################
:date: 2008-09-14 22:58
:author: ObliVion
:status: hidden
:tags: cifs, mount, Mythbuntu, samba
:slug: mythtv-and-cifs-trouble

Ever since I installed the `Mythbuntu`_ distribution I've had a hang
when samba tried to mount my remote music partition using cifs. It
seemed the network was not yet brought up, when the mount init script
tried to mount the share. After messing around with this for a very long
time, I decided to try and uninstall "NetworkManager", and mange the
network the "Debian" way. Adding the interface to
/etc/network/interfaces:

``auto lo eth0 iface lo inet loopback iface eth0 inet dhcp``

This finally did the trick, and I am no longer forced to watch the
bootscreen complaining about stupid network errors for the better half
of a minute.

.. _Mythbuntu: http://mythbuntu.org
