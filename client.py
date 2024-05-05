import socket
import threading
from cryptography.fernet import Fernet

header = 64
port = 5050
disconnect_message = "#quit"
contact_ip = "192.168.202.23"
ADDR = (contact_ip,port)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

senden_messages = []
recieved_messages = []

#şifreleme:
key = b'7a1vOxwC8XviL6IFcsCEo0xrQM_7_6A_kBz2e3qLmII='
fernet = Fernet(key)

def send(message):
<<<<<<< Updated upstream
    while True:
        senden_messages.append(message)
        message_encoded = message.encode("utf-8")
        encMessage = fernet.encrypt(message_encoded)
        message_length = len(encMessage)
        send_length = str(message_length).encode("utf-8")
        send_length += b' ' * (header - len(send_length))
        client.send(send_length)
        client.send(encMessage)
=======
    senden_messages.append(message)
    message_encoded = message.encode("utf-8")
    encMessage = fernet.encrypt(message_encoded)
    message_length = len(encMessage)
    send_length = str(message_length).encode("utf-8")
    send_length += b' ' * (header - len(send_length))
    client.send(send_length)
    client.send(encMessage)
>>>>>>> Stashed changes

def receive():
    while True:
        message_length = client.recv(header).decode("utf-8")
        if message_length:
            message_length = int(message_length)
            message = client.recv(message_length).decode("utf-8")
            decMessage = fernet.decrypt(message).decode()
            recieved_messages.append(decMessage)
            print(f"Server'dan mesaj: {decMessage}")
            return decMessage



def start():
    receive_thread = threading.Thread(target=receive)
    send_thread = threading.Thread(target=send)
    receive_thread.start()
    send_thread.start()

start()