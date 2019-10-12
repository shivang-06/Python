from tkinter import *

def printing():
    pass

screen = Tk()
screen.title('Window')
#screen.geometry('450x300')
label_1 = Label(screen, text="Hello there mateY !!!").grid(column=0,row=0)
button_1=Button(screen,text="Click",command=printing,width=15,height=2,bg='#ffffff',fg='red').grid()
screen.mainloop()