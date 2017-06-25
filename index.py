#!/usr/bin/python

import os,sys,time,socket,commands,cgitb,cgi

cgitb.enable()
print "Content-type:text/html\r\n\r\n"

data=cgi.FieldStorage()
email=data.getvalue('email')
pwd=data.getvalue('pwd')
if email=="abc@gmail.com" and pwd=="123":
	print "<head> <meta HTTP_EQUIV='refresh' width=device-width initial-scale=1.0 content='0;url='services.html' /> </head>"
else:
	print "invalid login"
