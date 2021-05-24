from tkinter import *
def mifuncion():
    print("ejecutando el programa")

ventana=Tk()
ventana.title("hola mundo ")
ventana.geometry("400x200")


lbl=Label(ventana,fg="gray",bg="blue",text="Este es un label")
lbl.pack()

boton=Button(ventana,text="Presionar",command=mifuncion)
boton.config(fg="white",bg="black")
boton.pack()


ventana.mainloop()  