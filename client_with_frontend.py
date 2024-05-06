import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from cryptography.fernet import Fernet

header = 64
port = 5050
disconnect_message = "#quit"
server_ip="178.240.201.228"

# Anahtar oluşturulması veya kullanılması
key = b'7a1vOxwC8XviL6IFcsCEo0xrQM_7_6A_kBz2e3qLmII='
fernet = Fernet(key)
username = "Ertunga Yusuf Ocak"
class ChatClient:
    def __init__(self, master):
        self.root = master
        self.frametop = tk.Frame(self.root, height=60, width=20, bg="lightblue")
        self.frametop.pack(side="top")

        self.framebottom = tk.Frame(self.root, height=400, width=400, bg="lightblue")
        self.framebottom.pack(side="bottom", fill="x")

        self.message_box = tk.Listbox(self.frametop,width=60,height=20)
        self.message_box.pack(padx=10,pady=10,side="top")

        self.message_entry = tk.Entry(self.framebottom)
        self.message_entry.pack(side="left",fill="x",padx=10,pady=10,expand=True)

        self.send_button = tk.Button(self.framebottom, text="Send", command=self.send_message)
        self.send_button.pack(side="right", padx=10)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect_to_server()

        self.receive_thread = threading.Thread(target=self.receive_message)
        self.receive_thread.start()

        self.update_messages()

    def connect_to_server(self):
        # Sunucuya bağlanma
        try:
            self.client.connect((server_ip, port))  # İletişim için hedef IP
        except Exception as e:
            print("Bağlantı hatası:", e)

    def send_message(self):
        # Mesaj gönderme
        message = self.message_entry.get()
        if message:
            message = username + ": " + message
            self.message_box.config(state=tk.NORMAL)
            self.message_box.insert(tk.END,message)
            self.message_box.config(state=tk.DISABLED)
            message_encoded = message.encode("utf-8")
            enc_message = fernet.encrypt(message_encoded)
            message_length = len(enc_message)
            send_length = str(message_length).encode("utf-8")
            send_length += b' ' * (header - len(send_length))
            self.client.send(send_length)
            self.client.send(enc_message)
            self.message_entry.delete(0, tk.END)

    def receive_message(self):
        # Mesaj alma
        while True:
            try:
                message_length = self.client.recv(header).decode("utf-8")
                if message_length:
                    message_length = int(message_length)
                    message = self.client.recv(message_length).decode("utf-8")
                    dec_message = fernet.decrypt(message.encode()).decode()
                    self.message_box.config(state=tk.NORMAL)
                    self.message_box.insert(tk.END, dec_message)
                    self.message_box.config(state=tk.DISABLED)
            except Exception as e:
                print("Alma hatası:", e)
                break

    def update_messages(self):
        # Arayüzü güncelleme
        self.message_box.config(state=tk.NORMAL)
        self.root.after(100, self.update_messages)

def client_main():
    root = tk.Tk()
    app = ChatClient(root)
    root.mainloop()
if __name__ == "__main__":
    client_main()


