import socket
import threading

leght_header = 20
base_ip = socket.gethostbyname(socket.gethostname())
base_port = 5050
tower = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connetion_address = base_ip, base_port
tower.bind(connetion_address)

def handle_with_connection(conn, addr):
    while True:
        message_length = conn.recv(leght_header).decode('utf-8')
        if message_length:
            message = conn.recv(int(message_length)).decode('utf-8')
            print(f"[{addr}]: {message}")
            #tower.send("message recieved".encode('utf-8'))
            if message == "end":
                print(f"{addr} ended connection ")
                break

    conn.close()
#def connect():
    #while True:
        #message = input("what is your message: ")
        #send_message(message)




tower.listen()
print(f"{base_ip} is listening... ")
while True:
    conn, addr = tower.accept()
    thread = threading.Thread(target=handle_with_connection, args=(conn, addr))
    print(f"{addr} is connected ")
    print(f"active connection number is {threading.active_count()}")
    thread.start()