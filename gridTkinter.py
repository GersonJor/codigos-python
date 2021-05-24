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

txt1=Entry(ventana,bg="pink")


lbl2=Label(ventana,text="Segundo numero",bg="green",fg="white")

txt2=Entry(ventana,bg="pink")

btn1=Button(ventana,text="sumar",bg="blue",fg="white",command=fnsuma)


lbl3=Label(ventana,text="Resultado",bg="green",fg="white")

txt3=Entry(ventana,bg="pink")


lbl1.grid(row=0,column=0,padx=6,pady=6,sticky="w",ipady=6)
txt1.grid(row=0,column=1,padx=6,pady=6)
lbl2.grid(row=1,column=0,padx=6,pady=6,sticky="w",ipady=6)
txt2.grid(row=1,column=1,padx=6,pady=6)
btn1.grid(row=1,column=2,padx=6,pady=6,ipadx=10,ipady=5)
lbl3.grid(row=2,column=0,padx=6,pady=6,sticky="w",ipady=6)
txt3.grid(row=2,column=1,padx=6,pady=6)


ventana.mainloop()