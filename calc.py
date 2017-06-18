#!/usr/bin/python

import socket,getpass,os,sys,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_ip="192.168.122.223"
server_port=4444

os.system('sshpass -p 123 ssh -X test@'+ server_ip +' gnome-calculator')
