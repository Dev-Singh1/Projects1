import socket
def main():
    sniff=socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    sniff.bind(("wlo1", 0)) #wlo1 is the wifi interface name on my device, it may need to be changed to work on other devices.
    while True:
        print(sniff.recv(65565))
if __name__ == "__main__":
    main()
