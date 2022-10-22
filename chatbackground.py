import socket
message=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
peerlist=["ip1", "ip2", "ip3"] # strings "ip1", ip2, ip3, are used as placeholders for actual ip adderesses since there are not enough participants in the network for actual peerlists.
while True:
    data , addr = message.recvfrom(4096)
    headers=[]
    headers=split(data, ",")
    name=split(headers[1], ":")
    if(name == "$USER"):#$User is a place holder for the username of the user.
        message=[]
        message=split(headers[2], ":")
        file1=open("history.txt", "a")
        file1.write(message[1].decode())
        file1.close()
    elif(name in peerlist):
        sendto(data, (target, 5555))
    else:
        peerlist.append(name)
        target = rand.choice(peerlist)
        while target == addr :
            target=rand.choice(peerlist)
        sendto(data, (target, 5555)) 
