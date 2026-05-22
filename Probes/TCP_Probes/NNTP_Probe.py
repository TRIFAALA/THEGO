from socket import *



def NNTP_Probe(IP_ADDR,Port):

    s = socket(AF_INET,SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((IP_ADDR,Port))
    
        try:
            Response = s.recv(1024).decode()
            if len(Response) > 0:  
                if "nntp" in Response.lower() or Response.startswith("200"):
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
                    print(f"Open Port {Port}/TCP")
                    print(f"NNTP Detected \n{Response}")
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
            
        except Exception:
            pass
    except Exception:
        pass
    s.close()

