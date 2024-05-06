import client_with_frontend
import server_with_frontend
import tkinter as tk
import threading

def client():
    threading.Thread(target=client_with_frontend.client_main).start()
    client_with_frontend.set_username(name)

def server():
    threading.Thread(target=server_with_frontend.server_main).start()
    server_with_frontend.set_username(name)

def save_username():
    global name
    name = message_entry.get()

def save_ip():
    ip = ip_entry.get() # IP adresini al
    server_with_frontend.server_ip = ip
    client_with_frontend.server_ip = ip

root = tk.Tk()
root.geometry("300x150")
frame = tk.Frame(root, height=60, width=20, bg="lightblue")
frame.pack(side="bottom",fill="both", expand="true")
frame1 = tk.Frame(root, height=60, width=20, bg="lightblue")
frame1.pack(side="top",fill="both", expand="true")
label = tk.Label(frame, text="Server mı ya da client mı olmak istersin", bg="lightblue")
label.pack()
button1 = tk.Button(frame, text="Server", command=server)
button1.pack(side="right", padx=30)
button2 = tk.Button(frame, text="Client", command=client)
button2.pack(side="left", padx=30)

label1 = tk.Label(frame1, text="Kullanıcı Adı", bg="lightblue")
label1.pack(side="left",padx=10)
message_entry = tk.Entry(frame1) # text parametresi kaldırıldı
message_entry.pack(side="left", fill="x", padx=10, pady=10, expand=True)
button3 = tk.Button(frame1, text="kaydet", command=save_username)
button3.pack(side="right", padx=10)

label2 = tk.Label(frame1, text="Server ip adresi:", bg="lightblue")
label2.pack(side="left",padx=10)
ip_entry = tk.Entry(frame1) # IP adresi için bir Entry alanı oluştur
ip_entry.pack(side="left", fill="x", padx=10, pady=10, expand=True)
button4 = tk.Button(frame1, text="kaydet", command=save_ip)
button4.pack(side="right", padx=10)

root.mainloop()

