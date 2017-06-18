#!/usr/bin/python

import socket,getpass,os,time,sys

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#server's ip and port number where to connect
server_ip="192.168.122.223"
server_port=4444

x='''
following services can be availed :
press 1 for firefox :
press 2 for vlc :
press 3 for calculator :
press 4 for gedit : 
press 5 for openoffice :
press 6 for webcam :
press 7 for screenshot :
'''

print x

ch=raw_input()

if ch=='1':
	execfile('/root/Documents/cloudclient/saas/firefox.py')
elif ch=='2':
	execfile('/root/Documents/cloudclient/saas/vlc.py')
elif ch=='3':
	execfile('/root/Documents/cloudclient/saas/calc.py')
elif ch=='4':
	execfile('/root/Documents/cloudclient/saas/gedit.py')
elif ch=='5':
	execfile('/root/Documents/cloudclient/saas/openoffice.py')
elif ch=='6':
	execfile('/root/Documents/cloudclient/saas/webcam.py')
elif ch=='7':
	execfile('/root/Documents/cloudclient/saas/screenshot.py')
else:
	print "wrong choice"
	 
