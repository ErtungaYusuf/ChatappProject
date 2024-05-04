import socket
import threading


port =9080
#gerçek internette kullanımda bu ip cihazın public ip'sine eşitlenmeli
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

def handle_send_message(conn,addr):
    while True:
        message = input("Mesajınız:")
        message_encoded = message.encode("utf-8")
        message_length = len(message_encoded)
        send_length = str(message_length).encode("utf-8")
        send_length += b' ' * (header - len(send_length))
        conn.send(send_length)
        conn.send(message_encoded)


def start():
    print(f"{server_ip} ip'li cihaz gelen bağlantıları dinliyor...")
    server.listen()
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_contact, args=(conn,addr))
        thread2 = threading.Thread(target=handle_send_message, args = (conn,addr))
        thread.start()
        thread2.start()


start()