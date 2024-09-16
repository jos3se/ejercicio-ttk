import tkinter as tk
from tkinter import ttk ,Label,PhotoImage
contrasena = 110507
usuario = "pepe1234"
def enviar(entry1,entry2,imagen):
    
    user = str(entry1.get())
    contra = int(entry2.get())
    if user == usuario and contra == contrasena:
        imagen.configure(file="clipart-765_small.png")
    else:
        imagen.configure(file="R.png")

root = tk.Tk()
root.title("login")
root.geometry("400x400")
label1 = ttk.Label(root,text="usuario")
label1.pack()
entry1 = ttk.Entry()
entry1.pack()
label2 = ttk.Label(root,text="contraseña")
label2.pack()
entry2 = ttk.Entry()
entry2.pack()
boton = ttk.Button(text="comprobar",command= lambda:enviar(entry1,entry2,imagen))
boton.pack()
imagen = PhotoImage(file="")
label3 = Label(root, image=imagen)
label3.pack()
root.mainloop()