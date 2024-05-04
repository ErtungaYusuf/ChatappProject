import socket

leght_header = 20
base_ip = "192.168.1.36"
base_port = 5050
tower = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tower.connect((base_ip,base_port))

def send_message(message):
    prepared_message = message.encode('utf-8')
    leght_for_header = len(prepared_message)
    prepared_lenght_header = str(leght_for_header).encode('utf-8')
    prepared_lenght_header += b' '*(leght_header-len(prepared_lenght_header))
    tower.send(prepared_lenght_header)
    tower.send(prepared_message)

while True:
    message = input("what is your message: ")
    send_message(message)
    if message == "end":
        break