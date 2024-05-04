import socket
import threading

header = 64
port = 9080
disconnect_message = "#quit"
contact_ip = "192.168.202.23"
ADDR = (contact_ip,port)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send():
    while True:
        message = input("Mesajınız:")
        message_encoded = message.encode("utf-8")
        message_length = len(message_encoded)
        send_length = str(message_length).encode("utf-8")
        send_length += b' ' * (header - len(send_length))
        client.send(send_length)
        client.send(message_encoded)
        print(client.recv(2048).decode("utf-8"))#burası 64 bytle olacak şekilde düzenlenmeli

def receive():
    while True:
        message_length = client.recv(header).decode("utf-8")
        if message_length:
            message_length = int(message_length)
            message = client.recv(message_length).decode("utf-8")
            print(f"Server'dan mesaj: {message}")


receive_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)
receive_thread.start()
send_thread.start()