#! /usr/bin/env python3

from socket import *
import sys


def send_udp(add, msg):
	SERVER_IP = ""
	SERVER_PORT = 55555

	s = socket(AF_INET, SOCK_DGRAM)  # IPv4 + UDP
	s.bind((SERVER_IP, SERVER_PORT))  # bind process to port and ip
	s.sendto(msg.encode(), add)  # send systemtime as byte object
	s.settimeout(5)
	try:
		data, address = s.recvfrom(1024)
		return data.decode()
	except timeout as t:
		print(t,str(add))
		pass

def main(argv):
	if len(argv) > 1: # arguments provided
		ADDRESS=(argv[1],int(argv[2]))
	else:
		ADDRESS=('192.168.137.176',8888)
	print("Send msg to: " + str(ADDRESS))
	print(send_udp(ADDRESS, "Hello World"))
 
if __name__ == '__main__':
	main(sys.argv)
