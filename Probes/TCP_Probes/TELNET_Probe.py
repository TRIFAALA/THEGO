from socket import *

def TELNET_Probe(IP_ADDR,Port):

    s = socket(AF_INET,SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((IP_ADDR,Port))
        try:
            Response = s.recv(1024)
            if len(Response) > 0:
                if b"\xff" in Response:
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
                    print(f"Open Port {Port}/TCP")
                    print(f"TELNET Detected")
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
        except timeout:
            pass
    except ConnectionRefusedError:
        pass
    except timeout:
        pass
    s.close()        

