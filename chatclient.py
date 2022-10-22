import socket
message=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Enter 9 for help")
while True:
    command = int(input("What would you like to do?:"))
    if(command == 1):
        target = input("To whom would you like to send this message?:")
        data= input("Enter the message to send:")
        packet="Recvier"+":"+target+"Data"+":"+data # puts message into format that the reciver program can easily decode.
        message.sendto(packet.encode(), (target, 5555))
    elif(command == 2):
        history=open("/home/$USERNAME/history.txt")#$USERNAME is a place holder
        conversation = history.readlines()
        history.close()
        print(conversation)
    elif(command == 3):
        print(data)
    else:
        print("Enter 1 to send a message")
        print("Enter 2 to read conversation history")
        print("Enter 3 to see unread messages")
        print("Enter 9 for this help menu")
