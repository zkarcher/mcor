import sys
import select
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 2084

MESSAGE = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto( MESSAGE, (UDP_IP, UDP_PORT) )
print "sent"