import socket
import threading

header_lenght = 20
user_ip = socket.gethostbyname(socket.gethostname()) #kullanıcının kendi ip'si
contacted_ip = "192.168.1.36"
port = 5050
tower = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connetion_address = user_ip, port
tower.bind(connetion_address)
tower.connect((contacted_ip,port))


def handle_with_connection(conn, addr):
    while True:
        message_length = conn.recv(header_lenght).decode('utf-8')
        if message_length:
            message = conn.recv(int(message_length)).decode('utf-8')
            print(f"[{addr}]: {message}")
            #tower.send("message recieved".encode('utf-8'))
            if message == "end":
                print(f"{addr} ended connection ")
                break

    conn.close()
def send_message(message):
    prepared_message = message.encode('utf-8')
    leght_for_header = len(prepared_message)
    prepared_lenght_header = str(leght_for_header).encode('utf-8')
    prepared_lenght_header += b' '*(header_lenght-len(prepared_lenght_header))
    tower.send(prepared_lenght_header)
    tower.send(prepared_message)

tower.listen()
print(f"{user_ip} ip'li cihaz gelen bağlantıları dinliyor... ")
while True:
    conn, addr = tower.accept()
    thread = threading.Thread(target=handle_with_connection, args=(conn, addr))
    print(f"{addr} ip'li cihaz bağlandı ")
    print(f"active connection number is {threading.active_count()}")
    thread.start()
    while True:
        message = input("what is your message: ")
        send_message(message)
        if message == "end":
            break

