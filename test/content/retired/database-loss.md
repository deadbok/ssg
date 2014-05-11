author: ObliVion
date: 2010-05-13 20:19
slug: database-loss
status: hidden
tags: MySQL Administrator, MySQL backup, MySQL Workbench
title: Database loss


I have lost the last 3 blog entries, about the Nelson Pass designed
First Watt F2 amplifier I am building. A mixture of a wanting to upgrade
Wordpress, to get rid of the "please update" message, trying to figure
out how to use MySQL Workbench, which has replaced MySQL Administrator,
that I used to do backups with, and last end really important, the level
of stress I was under, when I stupidly decided to do this, ended up this
way.

Somehow it seems that MySQL Workbench, wrote back the changes to the
server, even though I thought I asked it not to do so,  and BAM the
wordpress database was gone. Luckily I take backups fairly often, with
MySQL Administaror, and most of the post a still here.

I have reverted to using MySQL Administrator, for as long as it works,
and installed
[AutoMySQLBackup](http://sourceforge.net/projects/automysqlbackup/)on
the server according to this
[guide](http://www.debianhelp.co.uk/mysqlscript.htm).
