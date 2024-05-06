import client_with_frontend
import server_with_frontend
import tkinter as tk
import threading

def client():
    threading.Thread(target=client_with_frontend.client_main).start()

def server():
    threading.Thread(target=server_with_frontend.server_main).start()

root = tk.Tk()
root.geometry("300x100")
frame = tk.Frame(root, height=60, width=20, bg="lightblue")
frame.pack(fill="both", expand="true")
label = tk.Label(frame, text="Server mı ya da client mı olmak istersin", bg="lightblue")
label.pack()
button1 = tk.Button(frame, text="Server", command=server)
button1.pack(side="right", padx=30)
button2 = tk.Button(frame, text="Client", command=client)
button2.pack(side="left", padx=30)
root.mainloop()
