import client_with_frontend
import server_with_frontend
import tkinter as tk
import threading

def client():
    threading.Thread(target=client_with_frontend.client_main).start()

def server():
    threading.Thread(target=server_with_frontend.server_main).start()

def save_username():
    name=message_entry.get()
    message_entry.delete(0,tk.END)
def get_username():
    return name


root = tk.Tk()
root.geometry("300x100")
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
message_entry = tk.Entry(frame1,text="sa")
message_entry.pack(side="left", fill="x", padx=10, pady=10, expand=True)
button3 = tk.Button(frame1, text="kaydet", command=save_username)
button3.pack(side="right", padx=10)
root.mainloop()
