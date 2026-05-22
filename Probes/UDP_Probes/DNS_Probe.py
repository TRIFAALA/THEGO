from socket import *


def DNS_Probe(IP_ADDR,port):

    # Subs_split = Subdomain.split(".")
    s = socket(AF_INET,SOCK_DGRAM)

    dns_server = (IP_ADDR,port)

    packet = b'\x12\x34\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00' + b'\x03www\x05google\x03com\x00\x00\x01\x00\x01'
    try:
        s.settimeout(2)
        s.sendto(packet,dns_server)
        data,addr = s.recvfrom(1024)
        if len(data) > 0:
            if packet.hex()[0:4] in data.hex()[0:4]:
                print("-----------------------------------------------------------------------------------------------------------------------------------")
                print(f"Open Port {port}/UDP")
                print("DNS DETECTED")
                print("-----------------------------------------------------------------------------------------------------------------------------------")
    except Exception:
        pass
    s.close()


