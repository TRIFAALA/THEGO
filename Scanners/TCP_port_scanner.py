from socket import *
from Probes.TCP_Probes import HTTP_Probe
from Probes.TCP_Probes import SSH_probe
from Probes.TCP_Probes import FTP_Probe
from Probes.TCP_Probes import TELNET_Probe
from Probes.TCP_Probes import IMAP_Probe
from Probes.TCP_Probes import NNTP_Probe
from Probes.TCP_Probes import SMTP_Probe
from Probes.TCP_Probes import POP3_Probe
from Probes.TCP_Probes import MySQL_Probe
from Probes.TCP_Probes import HTTPS_Probe
from Probes.TCP_Probes import POSTGRESQL_Probe
from Probes.TCP_Probes import REDIS_Probe
import time

def TCP_Scanner(SubDomain):

    Sec_Time = time.time()
    Current_Time = time.ctime(Sec_Time)
    
    IP_ADDR = gethostbyname(SubDomain)

    print(f"Starting to scan ports for IP ADDRESS {IP_ADDR} at {Current_Time}")
    
    TCP_Ports = [21,22,23,25,80,110,143,443,445,465,587,993,995,1433,3306,3389,5432,5900,6379,8080,8443]

   # Server_Speak_First = [21,22,23,25,110,143,3306,5432,5900]

   # Client_Speak_First = [80,8080,6379,445,3389,1433,443,465,993,995,8443]



    for port in TCP_Ports:

        s = socket(AF_INET,SOCK_STREAM)
        s.settimeout(1)
        Connect = s.connect_ex((IP_ADDR,port))
        
        if Connect == 0:
                        
            FTP_Probe.FTP_Probe(IP_ADDR,port)
            SSH_probe.SSH_probe(IP_ADDR,port)
            HTTP_Probe.HTTP_Probe(IP_ADDR,port,SubDomain)
            HTTPS_Probe.HTTPS_Probe(IP_ADDR,port)
            TELNET_Probe.TELNET_Probe(IP_ADDR,port)
            SMTP_Probe.SMTP_Probe(IP_ADDR,port)
            IMAP_Probe.IMAP_Probe(IP_ADDR,port)
            NNTP_Probe.NNTP_Probe(IP_ADDR,port)
            POP3_Probe.POP3_Probe(IP_ADDR,port)
            MySQL_Probe.MySQL_Probe(IP_ADDR,port)
            POSTGRESQL_Probe.POSTGRESQL_Probe(IP_ADDR,port)
            REDIS_Probe.REDIS_Probe(IP_ADDR,port)
        s.close() 
        
                
            
        

            
                


        


        
    
     


 



