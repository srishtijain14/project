#!/usr/bin/python

import os,sys,time,commands,socket


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#server's ip and port number where to connect
server_ip="192.168.122.223"
server_port=4444

x='''
press 1 for SAAS
press 2 for STAAS
press 3 for IAAS
'''

print x

ch=raw_input()

if ch=='1':
	execfile('/root/Documents/cloudclient/saas/saas.py')
elif ch=='2':
	s.sendto(ch,(server_ip,server_port))
	execfile('/root/Documents/cloudclient/staas/staas.py')
elif ch=='3':
	#s.sendto(ch,(server_ip,server_port))
	excefile()
else:
	print "wrong choice"
	exit()


