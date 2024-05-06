import socket
import threading
from cryptography.fernet import Fernet
import tkinter as tk
#from main import get_username

port = 5050
server_ip = socket.gethostbyname(socket.gethostname())
ADDR = (server_ip, port)

def get_server_ip():
    return server_ip

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
header = 64
disconnect_message = "#quit"

sended_messages = []
received_messages = []
username = "default1"
key = b'7a1vOxwC8XviL6IFcsCEo0xrQM_7_6A_kBz2e3qLmII='
fernet = Fernet(key)
def set_username(name):
    global username
    username=name
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
                received_messages.append(decMessage)
                print(f"[{addr} ip'li cihaz]: {decMessage}")
    conn.close()

def handle_send_message(conn, addr):
    def send_message(event=None):
        message = message_entry.get()
        if message:
            message = username + ": " + message
            sended_messages.append(message)
            message_encoded = message.encode("utf-8")
            encMessage = fernet.encrypt(message_encoded)
            message_length = len(encMessage)
            send_length = str(message_length).encode("utf-8")
            send_length += b' ' * (header - len(send_length))
            conn.send(send_length)
            conn.send(encMessage)
            message_entry.delete(0, tk.END)
            chat_history.insert(tk.END,message)

    def create_gui():
        root = tk.Tk()
        frametop = tk.Frame(root, height=60, width=20, bg="lightblue")
        frametop.pack(side="top")

        framebottom = tk.Frame(root, height=400, width=400, bg="lightblue")
        framebottom.pack(side="bottom", fill="x")

        chat_history = tk.Listbox(frametop, width=60, height=20)
        chat_history.pack(padx=10, pady=10, side="top")

        message_entry = tk.Entry(framebottom)
        message_entry.pack(side="left", fill="x", padx=10, pady=10, expand=True)

        send_button = tk.Button(framebottom, text="Send", command=send_message)
        send_button.pack(side="right", padx=10)

        root.bind("<Return>", send_message)
        return root, chat_history, message_entry

    def update_messages(text_widget):
        while True:
            if received_messages:
                message = received_messages.pop(0)
                text_widget.insert(tk.END, message)
                text_widget.see(tk.END)  # Scroll to the end
                text_widget.update_idletasks()  # Güncellemeleri yap
            root.update()  # Ana pencereyi güncelle

    root, chat_history, message_entry = create_gui()
    update_thread = threading.Thread(target=update_messages, args=(chat_history,))
    update_thread.start()

    root.mainloop()

def start():
    print(f"{server_ip} ip'li cihaz gelen bağlantıları dinliyor...")
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_contact, args=(conn, addr))
        thread2 = threading.Thread(target=handle_send_message, args=(conn, addr))
        thread.start()
        thread2.start()
def server_main():
    root = tk.Tk()
    start()
    root.title("Chat Uygulaması")
    root.mainloop()

#server_main()

