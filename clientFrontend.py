import tkinter as tk
import client
import threading

def send_message(username):
    pass

def check_server():
    # Sunucu durumunu kontrol et
    pass

def on_send_button_click():
    send_message("username")  # Kullanıcı adını buraya ekleyin

def start_chat_app():
    # Sunucu thread'ini başlat
    server_thread = threading.Thread(target=client.start)
    server_thread.start()

    # Tkinter uygulamasını başlat
    root.mainloop()

root = tk.Tk()

frame_top = tk.Frame(root, height=60, width=20, bg="lightblue")
frame_top.pack(side="top")

frame_bottom = tk.Frame(root, height=400, width=400, bg="lightblue")
frame_bottom.pack(side="bottom", fill="x")

chat_history = tk.Listbox(frame_top, width=60, height=20)
chat_history.pack(padx=10, pady=10, side="top")

text_entry = tk.Entry(frame_bottom)
text_entry.pack(side="left", fill="x", padx=10, pady=10, expand=True)

send_button = tk.Button(frame_bottom, text="Gönder", command=on_send_button_click)
send_button.pack(side="right", padx=10)

# Sunucu durumunu düzenli olarak kontrol etmek için bir after() çağrısı yapın
root.after(1000, check_server)

# Tkinter uygulamasını başlatan fonksiyonu başlat
start_chat_app()

