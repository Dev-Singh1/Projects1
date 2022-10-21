
import socket
import sys
import os
sys.argv[2]
addr
targetport = 55555
connection1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
targethost = sys.argv[1]
connection1.connect((targethost, targetport))
connection1.settimeout(2)
connection1.send(b"helloworld")
try:
    connection1.recv(1024)
except socket.timeout:
    print(targethost + "is unreachable") 
except socket.error:
    print(targethost + " is reachable")
else:
    connection1.close()
    
