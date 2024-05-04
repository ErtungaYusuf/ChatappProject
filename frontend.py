import tkinter as tk
from tkinter import scrolledtext
# from client  import send_message
import server
import client


def send_message1(username):   #mesaj yollama
    message=text.get()
    if message:
       #send_message(message)
       chat_history.insert(tk.END,username+":"+message)
    text.delete(0,tk.END)


root=tk.Tk()
frametop=tk.Frame(root,height=60,width=20,bg="lightblue")
frametop.pack(side="top")

framebottom=tk.Frame(root,height=400,width=400,bg="lightblue")
framebottom.pack(side="bottom",fill="x")



chat_history=tk.Listbox(frametop,width=60,height=20)
chat_history.pack(padx=10,pady=10,side="top")




text=tk.Entry(framebottom)
text.pack(side="left",fill="x",padx=10,pady=10,expand=True)

buton = tk.Button(framebottom, text="gönder", command=lambda: send_message1("asd"))  #asd yerine normal kullanıcı ismi 
# kullanıcı ismi komutlarla geliyorsa asd yerine komut yazılır oyle bir komut yoksa fazladan pencere eklerim kullanıcı adı alan
buton.pack(side="right", padx=10)





root.mainloop()

