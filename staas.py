#!/usr/bin/python

import os,sys,time,commands,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#server's ip and port number where to connect
server_ip="192.168.122.223"
server_port=4444

x='''
press 1 for new drive
press 2 to extend the size
'''
print x
#choice from above options
ch=raw_input()
#drive name
drive_name=raw_input("enter drive name : ")
#drive size
drive_size=raw_input("enter drive size (10K or 20M or 30G : ")
#sending data to server
s.sendto(drive_name,(server_ip,server_port))
s.sendto(drive_size,(server_ip,server_port))
s.sendto(ch,(server_ip,server_port))
#recieving data from server
result=s.recvfrom(13)
if result[0]=="creationdone":
	os.system('mkdir /media/'+drive_name)
	os.system('mount '+server_ip+':/mnt/'+drive_name+' /media/'+drive_name)
	print "creation done"
elif result[0]=="extensiondone":
	print "extension done"
else:
	print "no response from cloud side"

