from socket import *



def SMTP_Probe(IP_ADDR,Port):

    s = socket(AF_INET,SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((IP_ADDR,Port))

        try:
            Response = s.recv(1024).decode(errors="ignore")
            if len(Response) > 0:
                if "smtp" in Response.lower() and Response.startswith("220"):
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
                    print(f"Open Port {Port}/TCP")
                    print(f"SMTP Detected \n{Response}")
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
        except Exception:
            pass
    except Exception:
        pass
    s.close()

