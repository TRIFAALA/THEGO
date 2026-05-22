from socket import *



def IMAP_Probe(IP_ADDR,Port):

    s = socket(AF_INET,SOCK_STREAM)

    s.settimeout(3)
    try:
        s.connect((IP_ADDR,Port))
        try:
            Response = s.recv(1024).decode()
            if len(Response) > 0:
                if "imap" in Response.lower():
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
                    print(f"Open Port {Port}")
                    print(f"IMAP Detected {Response}")
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
            
        except Exception as e:
            pass
        # s.close()
    except Exception as e:
        pass
    s.close()
    

