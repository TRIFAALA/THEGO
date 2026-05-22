from socket import *


def SSH_probe(IP_ADDR,port):

    s = socket(AF_INET,SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((IP_ADDR,port))
        try:
            Response = s.recv(1024).decode(errors="ignore")
            if len(Response) > 0:
                if Response.startswith("SSH-"):
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
                    print(f"Open Port {port}/TCP")
                    print(f"SSH detected \n{Response}")
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
        except Exception:
            pass
    except Exception:
        pass
    s.close()





