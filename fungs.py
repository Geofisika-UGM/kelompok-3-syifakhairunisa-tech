import tkinter as tk
import math
import turtle
import threading
def ramp_prob(m,g,sudut,μs,t):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=600)
    canvas.pack()
        
    def info(m,g,sudut,μs,t):
        if μs > 1:
            salah()
        else:
            posisi_balok(m,g,sudut,μs,t)
    def posisi_balok(m,g,sudut,μs,t):
        W = m*g
        sudutlintasan = math.radians(sudut)
        sina = math.sin(sudutlintasan)
        Wx = W*sina
        sudutlintasan = math.radians(sudut)
        cosa = math.cos(sudutlintasan)
        Wy = W*cosa
        N = Wy
        fs =  μs*N
        ΣFx = Wx - fs
        ax = ΣFx/m
        x0 = 0
        v0x = 0
        x = x0 + v0x*t + (1/2)*ax*t**2
        gambar(x)
    def salah():
        tt = turtle.RawTurtle(canvas)
        tt.write("Koefisien Gesek Terlalu Besar")
    def gambar(x):
        tt = turtle.RawTurtle(canvas)
        s=math.sqrt(150**2+100**2)
        y=x/5
        if y>s:
            tt.penup()
            tt.write(x)
            tt.goto(0,-20)            
            tt.write("melebihi batas")
        else:
            
            tt.forward(150)
            tt.left(90)
            tt.forward(100)
            tt.left(124)
            tt.forward(s)
            tt.left(180)
            tt.forward(s)
            tt.left(180)
            tt.forward(y)
            tt.right(90)
            tt.forward(20)
            tt.left(90)
            tt.forward(20)
            tt.left(90)
            tt.forward(20)
            tt.left(90)
            tt.forward(20)
        
            tt.penup()
            tt.goto(0,-20)            
            tt.write(x,"cm")
    info(m,g,sudut,μs,t)
    root.mainloop()