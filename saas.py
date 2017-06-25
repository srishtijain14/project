#!/usr/bin/python

import os,sys,time,socket,commands,cgitb,cgi

cgitb.enable()
print "Content-type:text/html\r\n\r\n"

data=cgi.FieldStorage()
f=data.getvalue('firefox')
v=data.getvalue('vlc')
cal=data.getvalue('cal')
g=data.getvalue('gedit')
o=data.getvalue('office')
cam=data.getvalue('cam')
s=data.getvalue('screenshot')

if f=='firefox':
	execfile('/var/www/html/firefox.sh')
