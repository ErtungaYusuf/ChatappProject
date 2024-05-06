import client_with_frontend
import server_with_frontend
import tkinter as tk
import threading

def client():
    save_username()
    threading.Thread(target=client_with_frontend.client_main).start()
    client_with_frontend.set_username(name)
    save_ip()

def server():
    save_username()
    threading.Thread(target=server_with_frontend.server_main).start()
    server_with_frontend.set_username(name)
    ip_entry.insert(0,server_with_frontend.get_server_ip())

def save_username():
    global name
    name = message_entry.get()
    message_entry.delete(0,tk.END)

def save_ip():
    ip = ip_entry.get()
    client_with_frontend.set_ip(ip)

root = tk.Tk()
root.geometry("400x180")
root.title("Chat Uygulaması")
frame1 = tk.Frame(root, height=60, width=20, bg="lightblue")
frame1.pack(side="top",fill="both", expand="true")
frame = tk.Frame(root, height=60, width=20, bg="lightblue")
frame.pack(fill="both", expand="true")
frame2 = tk.Frame(root, height=60, width=20, bg="lightblue")
frame2.pack(side="bottom",fill="both", expand="true")
label = tk.Label(frame, text="Server mı ya da client mı olmak istersin", bg="lightblue")
label.pack()
button1 = tk.Button(frame, text="Server", command=server)
button1.pack(side="right", padx=30)
button2 = tk.Button(frame, text="Client", command=client)
button2.pack(side="left", padx=30)

label1 = tk.Label(frame1, text="Kullanıcı Adı:", bg="lightblue")
label1.pack(side="left",padx=10)
message_entry = tk.Entry(frame1) # text parametresi kaldırıldı
message_entry.pack(side="left", fill="x", padx=10, pady=10, expand=True)




label2 = tk.Label(frame2, text="Serverın ip adresi:", bg="lightblue")
label2.pack(side="left",padx=10)
ip_entry = tk.Entry(frame2) # IP adresi için bir Entry alanı oluştur
ip_entry.pack(side="left", fill="x", padx=10, pady=10, expand=True)


root.mainloop()

