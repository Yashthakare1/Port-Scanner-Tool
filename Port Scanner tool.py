#this is a simpal Port Scanner tool

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Enter the IP You Want To Scan")
port = int(input("Enter The Port You Want To Scan"))


def portScanner(port):
    if s.connect_ex((host,port)):
        print(f"The {port} port is Close")
    else:
        print(f"The {port} port is Open")


portScanner(port)
