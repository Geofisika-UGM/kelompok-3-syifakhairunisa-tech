from tkinter import*
import tkinter.font
import math
from fungs import ramp_prob
root = Tk()
root.geometry("300x600")

changefont = tkinter.font.Font(size=20)
Title = Label(root,text = "Core Ramp Problem", font = changefont)
Title.place(x=20, y=10)

m = Label(root,text = "Massa Benda")
g =Label(root,text = "Gravitasi")
sudut = Label(root,text = "Besar Sudut")
μs = Label(root,text = "Koefisien Gaya Gesek")
t = Label(root,text = "Durasi Waktu")


e1 = Entry(root,width=40)
e2 = Entry(root,width=40)
e3 = Entry(root)
e4 = Entry(root,width=40)
e5 = Entry(root,width=40)

m.place(x = 20, y = 50)
g.place(x = 20, y = 90)
sudut.place(x = 20, y = 130)
μs.place(x = 20, y = 170)
t.place(x = 20, y = 210)

e1.place(x = 20, y = 70)
e2.place(x = 20, y = 110)
e3.place(x = 20, y = 150)
e4.place(x = 20, y = 190)
e5.place(x = 20, y = 230)

def cetak():
    m = float(e1.get())
    g = float(e2.get())
    sudut = float(e3.get())
    μs = float(e4.get())
    t = float(e5.get())
    ramp_prob(m,g,sudut,μs,t)
            

btn = Button(root,text="submit", command=cetak).place(x=100, y=260)

root.mainloop()