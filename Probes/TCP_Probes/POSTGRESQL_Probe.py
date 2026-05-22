from socket import *



def POSTGRESQL_Probe(IP_ADDR,port):

    s = socket(AF_INET,SOCK_STREAM)
    try:
        s.connect((IP_ADDR,port))
        try:
            packet =  b'\x00\x00\x00\x08\x04\xd2\x16\x2f'
            s.send((packet))
            response = s.recv(1024)
            
            
            if len(response) > 0:
                
                if response.decode().startswith("HTTP") or response.decode().startswith("220") or "SMTP" in response.decode() or "FTP" in response.decode() or 'SSH' in response.decode() or '+OK' in response.decode():
                     pass
                elif 'S' in response.decode() or 'N' in response.decode() or 'K' in response.decode() or 'N' in response.decode() or 'Z' in response.decode():
 
                        print("-----------------------------------------------------------------------------------------------------------------------------------")
                        print(f"Open Port {port} \nPOSTGRESQL detected")
                        print("-----------------------------------------------------------------------------------------------------------------------------------")
        except Exception:
            pass
    
    except Exception:
        pass
    s.close()

