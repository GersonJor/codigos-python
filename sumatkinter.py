from tkinter import Tk, Label, Button, Entry

ventana=Tk()
ventana.title("Ejemplo place(sumar)")
ventana.geometry("400x200")

def fnsuma():
    n1=txt1.get()
    n2=txt2.get()
    r=float(n1)+float(n2)
    txt3.delete(0,"end")
    txt3.insert(0,r)


lbl1=Label(ventana,text="Primer numero",bg ="green",fg="white")
lbl1.place(relx=0.03,rely=0.04,relwidth=0.23,relheight=0.1)
txt1=Entry(ventana,bg="pink")
txt1.place(relx=0.3,rely=0.04,relwidth=0.22,relheight=0.1)

lbl2=Label(ventana,text="Segundo numero",bg="green",fg="white")
lbl2.place(relx=0.03,rely=0.2,relwidth=0.23,relheight=0.1)
txt2=Entry(ventana,bg="pink")
txt2.place(relx=0.3,rely=0.2,relwidth=0.22,relheight=0.1)
btn1=Button(ventana,text="sumar",bg="blue",fg="white",command=fnsuma)
btn1.place(relx=0.6,rely=0.2,relwidth=0.20,relheight=0.1)

lbl3=Label(ventana,text="Resultado",bg="green",fg="white")
lbl3.place(relx=0.03,rely=0.36,relwidth=0.23,relheight=0.1)
txt3=Entry(ventana,bg="pink")
txt3.place(relx=0.3,rely=0.36,relwidth=0.22,relheight=0.1)

ventana.mainloop()