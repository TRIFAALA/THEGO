from socket import *
import ssl


def HTTPS_Probe(host,port):


    s = socket(AF_INET,SOCK_STREAM)
    context = ssl.create_default_context()
    secure_sock = context.wrap_socket(s, server_hostname=host)

    try:
        secure_sock.connect((host, port))
        Request = (
            "HEAD / HTTP/1.1\r\n"
            f"Host: {host}\r\n"
            "Connection: close\r\n"
            "\r\n"
            )
        try:
            secure_sock.send(Request.encode())
            data = secure_sock.recv(1024).decode()
            if len(data) > 0:
                if "http" in data.lower():
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
                    print(f"Open Port {port}")
                    print("HTTPS DETECTED")
                    print(data)
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
        except Exception :
            pass
    except Exception:
        pass

    secure_sock.close()

