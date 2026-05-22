from socket import *



def MySQL_Probe(IP_ADDR,port):

    s = socket(AF_INET,SOCK_STREAM)
    try:
        s.connect((IP_ADDR,port))
        try:
        
            response = s.recv(1024)
            
            if len(response) > 0:
                if len(response) > 5:

                    if response[4] == 10:

                        version = response[5:].split(b'\x00')[0]
                        print("-----------------------------------------------------------------------------------------------------------------------------------")
                        print(f"Open Port {port}/TCP \nMySQL detected")
                        print(version.decode(errors="ignore"))
                        print("-----------------------------------------------------------------------------------------------------------------------------------")
        except Exception:
            pass
    
    except Exception:
        pass
    
    s.close()

