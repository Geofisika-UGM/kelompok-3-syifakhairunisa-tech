import math

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
    posisi_balok = x0 + v0x*t + (1/2)*ax*t**2
    return posisi_balok

print("Mencari posisi balok saat t")
m = float (input("Masukkan massa benda = "))
g = float (input("Masukkan percepatan gravitasi = "))
sudut = float (input("Masukkan sudut = "))
μs = float(input('Masukkan koefisien gaya gesek = '))
t = float (input("masukkan waktu = "))

x = posisi_balok(m,g,sudut,μs,t)
print(x)

y=x/5
import turtle
tt = turtle.Turtle()
tt.forward(150)  
tt.left(90)
tt.forward(100)
tt.left(124)
tt.forward(y)
tt.right(90)
tt.forward(50)
tt.left(90)
tt.forward(50)
tt.left(90)
tt.forward(50)
tt.left(90)
tt.forward(50)
tt.backward(178-y)
tt.penup()
tt.goto(120,100)
tt.write(x,"cm")
turtle.done()
turtle.mainloop()