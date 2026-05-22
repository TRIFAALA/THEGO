from socket import *



def REDIS_Probe(IP_ADDR,port):

    s = socket(AF_INET,SOCK_STREAM)

    try:
        s.connect((IP_ADDR,port))
        try:
            Query = "PING\r\n"
            s.send(Query.encode())
            Response = s.recv(1024).decode(errors="ignore")
            if len(Response) > 0:
                if "pong" in Response.lower() or Response.startswith("PONG"):
                     print("-----------------------------------------------------------------------------------------------------------------------------------")
                     print(f"Open Port {port}")
                     print("REDIS DETECTED")
                     print("-----------------------------------------------------------------------------------------------------------------------------------")
        except Exception:
            pass
    except Exception:
        pass


