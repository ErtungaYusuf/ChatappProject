import socket
import threading

#bağlantı portu:
port = 9080

#karşıdakinin ip'si:
contacted_ip = input("Karşıdakinin ip adresi : ")

#kendi ip'miz:
user_ip = socket.gethostbyname(socket.gethostname())

#alınan ilk mesaj 64 bytlık bir header, bu değişken uzunluğu tutuyor:
header = 64
disconnect_message = "#quit"
#Her kullanıcı aynı zamanda bir server:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (contacted_ip,port)
server.bind(ADDR)

#gelen yeni bağlantıları kontrol eden fonksiyon:
def handle_contact(conn,addr):
    print(f"{addr} ip'li cihaz bağlandı")
    connected = True
    while connected:
        #karşı taraftan mesaj bekler:
        message_length = conn.recv(header).decode("utf-8")
        message_length = int(message_length)
        message = conn.recv(message_length).decode("utf-8")
        if message == disconnect_message:
            connected = False
            print(f"{addr} ip'li cihazla bağlantı sonlandırıldı")
        else:
            print(f"[{addr} ip'li cihaz]: {message}")

    conn.close()

def start():
    print(f"{user_ip} ip'li cihaz gelen bağlantıları dinliyor...")
    server.listen()
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_contact(), args=(conn,addr))
        thread.start()


start()