author: ObliVion
date: 2013-10-07 20:18
tags: backup, iPhone, SMS
title: Extracting SMS messages from an iPhone
type: post
template: post


A friend of mine had an iPhone 3 that was getting really flaky, it was
still running IOS 3.1.2 as she was afraid to update, things could go
wrong, she could lose all her texts. What she wanted was essentially a
PDF with her messages.

I went searching and found some tools ranging in price from $$5 to $$20,
but I was stubborn and cheap, and wanted another solution. There are
some free services where you upload a file from an iTunes backup to some
web application and it'll extract the texts for you. Neither I, nor my
friend wanted all her texts uploaded to a service on the net.

From there I found out the file, that the web app uses, is actually an
SQL database file. If you ask iTunes to **make an unencrypted backup to
your local drive**, most of the backup files are actually in easily
understandable formats like SQL and jpeg. The location of these files
are:

-   Windows XP: \\Documents and Settings\\USERNAME\\Application
    Data\\Apple Computer\\MobileSyncBackup\\
-   Windows Vista, 7 or 8: \\Users\\USERNAME\\AppData\\Roaming\\Apple
    Computer\\MobileSync\\Backup\\
-   MacOS X: \~/Library/Application Support/MobileSync/Backup/

It turns out the file named
3d0d7e5fb2ce288813306e4d4636395e047a3d28.mddata is in fact an SQL
database file with all text messages in the backup. After eyeballing the
file with [SQLite Database
Browser](http://sqlitebrowser.sourceforge.net/), exporting it to a CSV
file, importing it in [LibreOffice](http://libreoffice.org) Calc, I
found it hard to manage the more than 30,000 messages that way.

In the end I made a python script that saves the messages to text files,
each having the address (phone nr.) of the person you were conversing
with. I am unsure how it handles MMS messages, I know that the
multimedia content is lost, and I think the text is lost aswell, but I
don't know. The result is here:

[GitHub link](https://github.com/deadbok/iphone-sms-dump.git)
