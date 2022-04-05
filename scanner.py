#Port scan with Python
#Connection py to os
from socket import socket
#port list
ports = [21, 23, 80, 443, 8080]
for ports in ports:
#creating client object, going into socket module and creating a socket object and type socket, (connection IP and TCP/IP protocol)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#searching time (depends on the network)
    client.settimeout(0.1)
#client connect to the local and the port (answer 0 is correct), could be the domain or the IP
#bancocn.com is the Solyd course site for pentest
    cod = client.connect_ex(('sitename.com', ports))
    if cod == 0:
        print (ports, 'Open')
    else:
        print('Close')
#1024 bytes that I want to receive
answer = client.recv(1024)
print (answer)