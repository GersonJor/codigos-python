from tkinter import Tk, Label, Button, Entry, Frame


class Miventana(Frame):

    def __init__(self,master=None):
        super().__init__(master,width=320,height=170)
        self.master=master
        self.pack()
        self.create_widgets()

    def fnsuma(self):

        n1=self.txt1.get()
        n2=self.txt2.get()
        r=float(n1)+float(n2)
        self.txt3.delete(0,"end")
        self.txt3.insert(0,r)

    def create_widgets(self):


            self.lbl1=Label(self,text="Primer numero",bg ="green",fg="white")
            self.txt1=Entry(self,bg="pink")
            self.lbl2=Label(self,text="Segundo numero",bg="green",fg="white")
            self.txt2=Entry(self,bg="pink")
            self.btn1=Button(self,text="sumar",bg="blue",fg="white",command=self.fnsuma)
            self.lbl3=Label(self,text="Resultado",bg="green",fg="white")
            self.txt3=Entry(self,bg="pink")


            self.lbl1.grid(row=0,column=0,padx=6,pady=6,sticky="w",ipady=6)
            self.txt1.grid(row=0,column=1,padx=6,pady=6)
            self.lbl2.grid(row=1,column=0,padx=6,pady=6,sticky="w",ipady=6)
            self.txt2.grid(row=1,column=1,padx=6,pady=6)
            self.btn1.grid(row=1,column=2,padx=6,pady=6,ipadx=10,ipady=5)
            self.lbl3.grid(row=2,column=0,padx=6,pady=6,sticky="w",ipady=6)
            self.txt3.grid(row=2,column=1,padx=6,pady=6)



ventana=Tk()
ventana.wm_title("Suma de numeros")
app=Miventana(ventana)
app.mainloop()