from socket import *



def FTP_Probe(IP_ADDR,Port):

    s = socket(AF_INET,SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((IP_ADDR,Port))

        try:
            Response = s.recv(1024).decode()
            if len(Response) > 0 :
                if "ftp" in Response.lower() or Response.startswith("220"):
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
                    print(f"Open Port {Port}/TCP")
                    print(f"FTP Detected \n{Response}")
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
            
        except timeout:
            pass
        except UnicodeEncodeError:
            pass
    except ConnectionRefusedError:
          pass
    except timeout:
        pass
    s.close()

