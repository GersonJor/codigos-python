from tkinter import Tk,Button,Frame

ventana=Tk()
ventana.title("Frame pruebas")
ventana.geometry("200x70")

frame1=Frame(ventana,bg="blue")
frame1.pack(expand=True,fill='both')

frame2=Frame(ventana,bg="yellow")
frame2.pack(expand=True,fill="both")
frame2.config(cursor="pirate")

redbutton=Button(frame1,text="RED",bg="red",fg="white")
yellowbutton=Button(frame1,text="YELLOW",bg="yellow",fg="white")
bluebutton=Button(frame1,text="BLUE",bg="blue",fg="white")

# redbutton.place(relx=0.05,rely=0.05,relwidth=0.25,relheight=0.9)
# yellowbutton.place(relx=0.35,rely=0.05,relwidth=0.25,relheight=0.9)
# bluebutton.place(relx=0.65,rely=0.05,relwidth=0.25,relheight=0.9)

redbutton.grid(row=0,column=0,padx=10,pady=1)
yellowbutton.grid(row=0,column=1,padx=10,pady=1)
bluebutton.grid(row=0,column=2,padx=10,pady=1)

blackbutton=Button(frame2,text="Black",bg="black",fg="white")
blackbutton.pack()





if __name__=='__main__':
    ventana.mainloop()