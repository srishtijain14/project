#!/usr/bin/python

import socket,getpass,time,os,sys

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#server's ip and port number where to connect
server_ip="192.168.122.223"
server_port=4444
#input username and password
s_user=raw_input("enter username : ")
s_password=getpass.getpass("enter password : ")
#sending data to server
s.sendto(s_user,(server_ip,server_port))
s.sendto(s_password,(server_ip,server_port))

data=s.recvfrom(20)
print data[0]
time.sleep(1)
if data[0]=="authentication done":
	print "please wait for a while"
	time.sleep(2)
	execfile('start.py')
	time.sleep(1)
elif data[0]=="invalid credentials":
	exit()

