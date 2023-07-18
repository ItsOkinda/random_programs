import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try :
    print("insert the url without the https:// part \n")
    host = input('enetr ip or host name  : ')
    ip =socket.gethostbyname(host)
    print(ip)
except Exception as e:
    print("an error occured could not resolve host ",e)