import socket
import threading
from cryptography.fernet import Fernet
import tkinter as tk

port = 5050
server_ip = socket.gethostbyname(socket.gethostname())
ADDR = (server_ip, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
header = 64
disconnect_message = "#quit"

sended_messages = []
received_messages = []

key = b'7a1vOxwC8XviL6IFcsCEo0xrQM_7_6A_kBz2e3qLmII='
fernet = Fernet(key)

def handle_contact(conn, addr):
    print(f"{addr} ip'li cihaz bağlandı")
    connected = True
    while connected:
        message_length = conn.recv(header).decode("utf-8")
        if message_length:
            message_length = int(message_length)
            message = conn.recv(message_length).decode("utf-8")
            decMessage = fernet.decrypt(message.encode()).decode()
            if decMessage == disconnect_message:
                connected = False
                print(f"{addr} ip'li cihazla bağlantı sonlandırıldı")
            else:
                received_messages.append(f"[{addr} ip'li cihaz]: {decMessage}")
                print(f"[{addr} ip'li cihaz]: {decMessage}")

    conn.close()

def handle_send_message(conn, addr):
    def send_message(event=None):
        message = message_entry.get()
        if message:
            sended_messages.append(message)
            message_encoded = message.encode("utf-8")
            encMessage = fernet.encrypt(message_encoded)
            message_length = len(encMessage)
            send_length = str(message_length).encode("utf-8")
            send_length += b' ' * (header - len(send_length))
            conn.send(send_length)
            conn.send(encMessage)
            message_entry.delete(0, tk.END)

    root = tk.Tk()
    root.title("Message Sender")
    root.geometry("300x100")

    message_entry = tk.Entry(root, width=30)
    message_entry.pack(pady=5)

    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack(pady=5)

    root.bind("<Return>", send_message)

    root.mainloop()

def update_messages(text_widget):
    while True:
        if received_messages:
            message = received_messages.pop(0)
            text_widget.insert(tk.END, f"{message}\n")
            text_widget.see(tk.END)  # Scroll to the end
        root.update()

def start():
    print(f"{server_ip} ip'li cihaz gelen bağlantıları dinliyor...")
    server.listen()
    while True:
        conn, addr = server.accept()
        text_widget = tk.Text(root)
        text_widget.pack()
        thread = threading.Thread(target=handle_contact, args=(conn, addr))
        thread2 = threading.Thread(target=handle_send_message, args=(conn, addr))
        thread.start()
        thread2.start()
        update_thread = threading.Thread(target=update_messages, args=(text_widget,))
        update_thread.start()

root = tk.Tk()
start()
root.mainloop()

