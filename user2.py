import socket
import threading


port =9080
server_ip = socket.gethostbyname(socket.gethostname())
ADDR = (server_ip ,port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
#alınan ilk mesaj 64 bytlık bir header, bu değişken uzunluğu tutuyor:
header = 64
disconnect_message = "#quit"
def handle_contact(conn,addr):
    print(f"{addr} ip'li cihaz bağlandı")
    connected = True
    while connected:
        #karşı taraftan mesaj bekler:
        message_length = conn.recv(header).decode("utf-8")
        if message_length:
            message_length = int(message_length)
            message = conn.recv(message_length).decode("utf-8")
            if message == disconnect_message:
                connected = False
                print(f"{addr} ip'li cihazla bağlantı sonlandırıldı")
            else:
                print(f"[{addr} ip'li cihaz]: {message}")

    conn.close()

def start():
    print(f"{server_ip} ip'li cihaz gelen bağlantıları dinliyor...")
    server.listen()
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_contact, args=(conn,addr))
        thread.start()


start()