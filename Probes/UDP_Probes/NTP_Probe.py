from socket import *

def NTP_Probe(IP_ADDR,port):

    
    s = socket(AF_INET, SOCK_DGRAM)
    query = b'\x1b' + 47 * b'\0'
    try:
        s.settimeout(2)
        s.sendto(query, (IP_ADDR, port))

        data, address = s.recvfrom(1024)
        if len(data) >= 48:
            print("-----------------------------------------------------------------------------------------------------------------------------------")
            print(f"Open Port {port}/UDP")
            print("NTP DETECTED")
            print("-----------------------------------------------------------------------------------------------------------------------------------")
    except Exception:
        pass
    s.close()
