import socket

header = 64
port = 9080
disconnect_message = "#quit"
contact_ip = "192.168.202.23"
ADDR = (contact_ip,port)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)