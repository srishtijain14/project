#!/usr/bin/python

import os,sys,time,socket,commands,cgitb,cgi

cgitb.enable()
print "Content-type:text/html\r\n\r\n"

data=cgi.FieldStorage()
osname=data.getvalue('os')
osram=data.getvalue('ram')
oscore=data.getvalue('core')
oshdd=data.getvalue('hdd')

print osname
print osram
print oscore
print oshdd

install_os='sudo virt-install  --cdrom /Redhat.iso --ram '+osram+' --vcpu '+oscore+' --nodisk '+' --name '+osname

x=os.system(install_os)

if x!=0:
	print "error"
