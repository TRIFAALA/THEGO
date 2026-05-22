from Scanners import TCP_port_scanner
from Scanners import UDP_port_scanner
import logo



logo.print_thumbs_up_logo()



Subdomain = input("Enter Subdomain you want to scan >> ")



    
    
TCP_port_scanner.TCP_Scanner(Subdomain)
UDP_port_scanner.UDP_Scanner(Subdomain)
    