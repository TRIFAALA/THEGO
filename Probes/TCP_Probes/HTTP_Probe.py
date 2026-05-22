from socket import *



def HTTP_Probe(IP_Addr,Port,Host):

    s = socket(AF_INET,SOCK_STREAM)
    try:
        s.connect((IP_Addr,Port))
        s.settimeout(3)
        Request = (
        "HEAD / HTTP/1.1\r\n"
        f"Host: {Host}\r\n"
        "Connection: close\r\n"
        "\r\n"
        )
        try:
            s.send(Request.encode())
            Data_Recv = s.recv(4096).decode(errors="ignore")
            if len(Data_Recv) > 0:
                if Data_Recv.startswith("HTTP"):
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
                    print(f"Open Port : {Port}")
                    print("HTTP DETECTED")
                    print(Data_Recv)
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
                s.close()
        except Exception as e:
            pass
    except Exception as e:
        pass
    s.close()    
    



