from tkinter import Tk, Label, Button, Frame ,Entry
from tkinter.font import Font
from tkinter.ttk import Combobox

class Miventana(Frame):

    def __init__(self,master=None):
        super().__init__(master,width=500,height=350,bg="#BCBEB4")
        
        self.master=master
        self.pack(expand=True,fill='both')
        self.crear_widgets()

    def fregistrar(self):
        dni=self.txt1_DNI.get()
        apell=self.txt2_Apellidos.get()
        nom=self.txt3_Nombres.get()
        direc=self.txt4_Direccion.get()
        telf=self.txt5_Telf.get()
        
        
        print("DNI: ",int(dni),"\nAPELLIDOS: "+apell)

    def Productos(self,event):
        if (self.txt6_Cod1.get()) == '0':
             self.etiqueta_prod1["text"]="0"
             self.etiqueta_Unid1["text"]="0"
             self.a1=0
             self.etiqueta_precio1["text"]="S/",self.a1 
            
        elif (self.txt6_Cod1.get()) == '1':
            self.etiqueta_prod1["text"]="Linterna de baterías"
            self.etiqueta_Unid1["text"]="S/8.00"
        elif self.txt6_Cod1.get() == '2':
            self.etiqueta_prod1["text"]="    Taladro"
            self.etiqueta_Unid1["text"]="S/40.00"
        elif self.txt6_Cod1.get() == '3':
            self.etiqueta_prod1["text"]="    Escalera"
            self.etiqueta_Unid1["text"]="S/80.00"
        elif self.txt6_Cod1.get() == '4':
            self.etiqueta_prod1["text"]="    Alicate"
            self.etiqueta_Unid1["text"]="S/12.00"
        elif self.txt6_Cod1.get() == '5':
            self.etiqueta_prod1["text"]="    Martillo"
            self.etiqueta_Unid1["text"]="S/15.00"
        elif self.txt6_Cod1.get() == '6':
            self.etiqueta_prod1["text"]="    Cinta métrica"
            self.etiqueta_Unid1["text"]="S/5.00"
        
        if(self.txt7_Cod2.get())=='0':
            self.etiqueta_prod2["text"]="0"
            self.etiqueta_Unid2["text"]="0"
            self.a2=0
            self.etiqueta_precio2["text"]="S/",self.a2 
        elif(self.txt7_Cod2.get())=='1':
            self.etiqueta_prod2["text"]="Linterna de baterías"
            self.etiqueta_Unid2["text"]="S/8.00"
        elif self.txt7_Cod2.get() == '2':
            self.etiqueta_prod2["text"]="    Taladro"
            self.etiqueta_Unid2["text"]="S/40.00"
        elif self.txt7_Cod2.get() == '3':
            self.etiqueta_prod2["text"]="    Escalera"
            self.etiqueta_Unid2["text"]="S/80.00"
        elif self.txt7_Cod2.get() == '4':
            self.etiqueta_prod2["text"]="    Alicate"
            self.etiqueta_Unid2["text"]="S/12.00"
        elif self.txt7_Cod2.get() == '5':
            self.etiqueta_prod2["text"]="    Martillo"
            self.etiqueta_Unid2["text"]="S/15.00"
        elif self.txt7_Cod2.get() == '6':
            self.etiqueta_prod2["text"]="    Cinta métrica"
            self.etiqueta_Unid2["text"]="S/5.00"

        if(self.txt8_Cod3.get())=='0':
            self.etiqueta_prod3["text"]="0"
            self.etiqueta_Unid3["text"]="0"
            self.a3=0
            self.etiqueta_precio3["text"]="S/",self.a3
        if(self.txt8_Cod3.get())=='1':
            self.etiqueta_prod3["text"]="Linterna de baterías"
            self.etiqueta_Unid3["text"]="S/8.00"
        elif self.txt8_Cod3.get() == '2':
            self.etiqueta_prod3["text"]="    Taladro"
            self.etiqueta_Unid3["text"]="S/40.00"
        elif self.txt8_Cod3.get() == '3':
            self.etiqueta_prod3["text"]="    Escalera"
            self.etiqueta_Unid3["text"]="S/80.00"
        elif self.txt8_Cod3.get() == '4':
            self.etiqueta_prod3["text"]="    Alicate"
            self.etiqueta_Unid3["text"]="S/12.00"
        elif self.txt8_Cod3.get() == '5':
            self.etiqueta_prod3["text"]="    Martillo"
            self.etiqueta_Unid3["text"]="S/15.00"
        elif self.txt8_Cod3.get() == '6':
            self.etiqueta_prod3["text"]="    Cinta métrica"
            self.etiqueta_Unid3["text"]="S/5.00"
        


    def fprecios(self,evento):
        cont=0
        a=int(self.txt9_Cant1.get())
        for i in range (1,a+1):
            cont+=1
        if self.txt6_Cod1.get()=='0':
            self.a1=cont*0
            self.etiqueta_precio1["text"]="S/",self.a1 
        elif self.txt6_Cod1.get()=='1':
            self.a1=cont*8
            self.etiqueta_precio1["text"]="S/",self.a1       
        elif self.txt6_Cod1.get()=='2':
            self.a1=cont*40
            self.etiqueta_precio1["text"]="S/",self.a1
        elif self.txt6_Cod1.get()=='3':
            self.a1=cont*80
            self.etiqueta_precio1["text"]="S/",self.a1
        elif self.txt6_Cod1.get()=='4':
            self.a1=cont*12
            self.etiqueta_precio1["text"]="S/",self.a1
        elif self.txt6_Cod1.get()=='5':
            self.a1=cont*15
            self.etiqueta_precio1["text"]="S/",self.a1
        elif self.txt6_Cod1.get()=='6':
            self.a1=cont*5
            self.etiqueta_precio1["text"]="S/",self.a1

    def fprecios2(self,evento):    
        cont1=0
        cont=0
        b=int(self.txt10_Cant2.get())
        for i in range (1,b+1):
            cont1+=1
        # a= int(self.txt7_Cod2.get())
        # for i in range (1,a+1):
        #     cont+=1           
        if self.txt7_Cod2.get()=='0':
            self.a2=cont1*0
            self.etiqueta_precio2["text"]="S/",self.a2 
        elif self.txt7_Cod2.get()=='1':
            self.a2=cont1*8
            self.etiqueta_precio2["text"]="S/",self.a2         
        elif self.txt7_Cod2.get()=='2':
            self.a2=cont1*40
            self.etiqueta_precio2["text"]="S/",self.a2
        elif self.txt7_Cod2.get()=='3':
            self.a2=cont1*80
            self.etiqueta_precio2["text"]="S/",self.a2
        elif self.txt7_Cod2.get()=='4':
            self.a2=cont1*12
            self.etiqueta_precio2["text"]="S/",self.a2
        elif self.txt7_Cod2.get()=='5':
            self.a2=cont1*15
            self.etiqueta_precio2["text"]="S/",self.a2
        elif self.txt7_Cod2.get()=='6':
            self.a2=cont1*5
            self.etiqueta_precio2["text"]="S/",self.a2
            
    def fprecios3(self,evento):  
        cont1=0
        b=int(self.txt11_Cant3.get())
        for i in range (1,b+1):
            cont1+=1 
        if self.txt8_Cod3.get()=='0':
            self.a3=cont1*0
            self.etiqueta_precio3["text"]="S/",self.a3
        elif self.txt8_Cod3.get()=='1':
            self.a3=cont1*8
            self.etiqueta_precio3["text"]="S/",self.a3
        if self.txt8_Cod3.get()=='1':
            self.a3=cont1*8
            self.etiqueta_precio3["text"]="S/",self.a3      
        elif self.txt8_Cod3.get()=='2':
            self.a3=cont1*40
            self.etiqueta_precio3["text"]="S/",self.a3
        elif self.txt8_Cod3.get()=='3':
            self.a3=cont1*80
            self.etiqueta_precio3["text"]="S/",self.a3
        elif self.txt8_Cod3.get()=='4':
            self.a3=cont1*12
            self.etiqueta_precio3["text"]="S/",self.a3
        elif self.txt8_Cod3.get()=='5':
            self.a3=cont1*15
            self.etiqueta_precio3["text"]="S/",self.a3
        elif self.txt8_Cod3.get()=='6':
            self.a3=cont1*5
            self.etiqueta_precio3["text"]="S/",self.a3 

        # if self.txt9_Cant1.get() == '2':
        #     self.etiqueta_precio1["text"]="S/16.00"
    def total(self):
        
            
        suma=self.a1+self.a2+self.a3
        self.etiqueta_total["text"]="S/",suma
        
        

        
    def crear_widgets(self):

        # self.seframe1=Frame(ventana,bg="#BCBEB4")
        # frame1.pack(expand=True,fill='both')

        frame2=Frame(self,bg="#C4E4D5")
        frame2.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.54)

        frame3=Frame(self,bg="#E6EFB8")
        frame3.place(relx=0.02,rely=0.58,relwidth=0.96,relheight=0.40)

        my_font=Font(family="Time New Roman",size=14,weight="bold",slant="italic")
        my_font2=Font(family="Time New Roman",size=9,weight="bold",slant="roman")

        Label(frame2,text="Ferretería el Tornillo Feliz",font=my_font,fg="black",bg="#C4E4D5").pack()

        Label(frame2,text="DNI",font=my_font2,bg="#C4E4D5").place(relx=0.08,rely=0.16)

        self.txt1_DNI=Entry(frame2,width=8,borderwidth=3)
        self.txt1_DNI.place(relx=0.18,rely=0.15)

        Label(frame2,text="Apellidos",font=my_font2, bg="#C4E4D5").place(relx=0.04,rely=0.32)

        self.txt2_Apellidos=Entry(frame2,width=14,borderwidth=3)
        self.txt2_Apellidos.place(relx=0.18,rely=0.31)

        Label(frame2,text="Nombres",font=my_font2, bg="#C4E4D5").place(relx=0.5,rely=0.32)
        
        self.txt3_Nombres=Entry(frame2,width=14,borderwidth=3)
        self.txt3_Nombres.place(relx=0.65,rely=0.31)

        Label(frame2,text="Dirección",font=my_font2, bg="#C4E4D5").place(relx=0.04,rely=0.49)
        self.txt4_Direccion=Entry(frame2,width=50,borderwidth=3)
        self.txt4_Direccion.place(relx=0.18,rely=0.48)

        Label(frame2,text="Teléfono",font=my_font2, bg="#C4E4D5").place(relx=0.04,rely=0.66)
        self. txt5_Telf=Entry(frame2,width=50,borderwidth=3)
        # txt5_Telf.insert(0,"Escriba aqui su numero de teléfono....")
        self.txt5_Telf.place(relx=0.18,rely=0.65)

        Label(frame3,text="Cod_Prod",font=my_font2, bg="#E6EFB8").place(relx=0)
       
        self.opciones=["0","1","2","3","4","5","6"]

        self.txt6_Cod1=Combobox(frame3,width=4,values=self.opciones,state="readonly")
        self.txt6_Cod1.place(relx=0.02,rely=0.18) 
        self.txt6_Cod1.bind("<<ComboboxSelected>>", self.Productos,self.fprecios)
        self.txt6_Cod1.current(0)

        self.txt7_Cod2=Combobox(frame3,width=4,values=self.opciones,state="readonly")
        self.txt7_Cod2.place(relx=0.02,rely=0.38)
        self.txt7_Cod2.bind("<<ComboboxSelected>>", self.Productos,self.fprecios2)
        self.txt7_Cod2.current(0)

        self.txt8_Cod3=Combobox(frame3,width=4,values=self.opciones,state="readonly")
        self.txt8_Cod3.place(relx=0.02,rely=0.58)
        self.txt8_Cod3.bind("<<ComboboxSelected>>", self.Productos,self.fprecios3)
        self.txt8_Cod3.current(0)

        
        

        Label(frame3,text="Descripción",font=my_font2, bg="#E6EFB8").place(relx=0.21)
        self.etiqueta_prod1=Label(frame3,bg="#E6EFB8")
        self.etiqueta_prod1.place(relx=0.18,rely=0.18)
        self.etiqueta_prod2=Label(frame3,bg="#E6EFB8")
        self.etiqueta_prod2.place(relx=0.18,rely=0.38)
        self.etiqueta_prod3=Label(frame3,bg="#E6EFB8")
        self.etiqueta_prod3.place(relx=0.18,rely=0.58)

        Label(frame3,text="Unidad",font=my_font2, bg="#E6EFB8").place(relx=0.42)
        self.etiqueta_Unid1=Label(frame3,bg="#E6EFB8")
        self.etiqueta_Unid1.place(relx=0.42,rely=0.18)
        self.etiqueta_Unid2=Label(frame3,bg="#E6EFB8")
        self.etiqueta_Unid2.place(relx=0.42,rely=0.38)
        self.etiqueta_Unid3=Label(frame3,bg="#E6EFB8")
        self.etiqueta_Unid3.place(relx=0.42,rely=0.58)

        a=0
        self.opciones1=[]
        for i in range(1,101):
            a+=1
            self.opciones1+=[a]

        Label(frame3,text="Cantidad",font=my_font2, bg="#E6EFB8").place(relx=0.53)
        self.txt9_Cant1=Combobox(frame3,width=3,values=self.opciones1,state="readonly")
        self.txt9_Cant1.place(relx=0.55,rely=0.18)
        self.txt9_Cant1.bind("<<ComboboxSelected>>", self.fprecios)
        

        self.txt10_Cant2=Combobox(frame3,width=3,values=self.opciones1,state="readonly")
        self.txt10_Cant2.place(relx=0.55,rely=0.38)
        self.txt10_Cant2.bind("<<ComboboxSelected>>", self.fprecios2)

        self.txt11_Cant3=Combobox(frame3,width=3,values=self.opciones1,state="readonly")
        self.txt11_Cant3.place(relx=0.55,rely=0.58)
        self.txt11_Cant3.bind("<<ComboboxSelected>>", self.fprecios3)


        Label(frame3,text="Precio",font=my_font2, bg="#E6EFB8").place(relx=0.67)
        self.etiqueta_precio1=Label(frame3,bg="#E6EFB8")
        self.etiqueta_precio1.place(relx=0.73,rely=0.18)

        self.etiqueta_precio2=Label(frame3,bg="#E6EFB8")
        self.etiqueta_precio2.place(relx=0.73,rely=0.38)

        self.etiqueta_precio3=Label(frame3,bg="#E6EFB8")
        self.etiqueta_precio3.place(relx=0.73,rely=0.58)



        Label(frame3,text="Subtotal",font=my_font2, bg="#E6EFB8").place(relx=0.76)


        # Label(frame3,text="Total",font=my_font2, bg="#E6EFB8").place(relx=0.89,rely=0.80)
        self.etiqueta_total=Label(frame3,width=4,bg="white")
        self.etiqueta_total.place(relx=0.73,rely=0.80)
        
        self.btn1_Stotal=Button(frame3,text="Total",command=self.total)
        self.btn1_Stotal.place(relx=0.89,rely=0.8)

        self.btn1_Registro=Button(frame3,text="Registrar",command=self.fregistrar)
        self.btn1_Registro.place(relx=0.41,rely=0.8)




if __name__=='__main__':
        ventana=Tk()
        ventana.wm_title("Ferreteria el tornillo feliz")
        app=Miventana(ventana)
        app.mainloop()
 



