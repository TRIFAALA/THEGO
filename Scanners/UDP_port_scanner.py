from socket import *
from Probes.UDP_Probes import DNS_Probe
from Probes.UDP_Probes import NTP_Probe

def UDP_Scanner(Subdomain):

    HOST = gethostbyname(Subdomain)

    UDP_Ports = [53,67,68,69,123,137,138,161,162,500,514,520,1900,5353]

    for port in UDP_Ports:

        DNS_Probe.DNS_Probe(HOST,port)
        NTP_Probe.NTP_Probe(HOST,port)

    
        

