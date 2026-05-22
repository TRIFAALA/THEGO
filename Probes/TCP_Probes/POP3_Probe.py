from socket import *



def POP3_Probe(IP_ADDR,Port):

    s = socket(AF_INET,SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((IP_ADDR,Port))

        try:
            Response = s.recv(1024).decode(errors="ignore")
            if len(Response) > 0:
                if "pop3" in Response.lower():
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
                    print(f"Open Port {Port}")
                    print("POP3 detected")
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
            
        except Exception as e:
            pass
    except Exception as e:
        pass
    s.close()


