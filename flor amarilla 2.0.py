from turtle import *
import colorsys
import math
import tkinter as tk

speed(0.25)
bgcolor("black")


goto(0, -40)
h = 0

for i in range(16):
    for j in range(18):
        c= colorsys.hsv_to_rgb(0.125 , 1, 1)
        color(c)
        rt(90)
        circle(150-j*6, 90)
        lt(90)
        circle(150-j*6, 90)
        rt(180)
    circle(40, 24)


color("black") 
shape("turtle")
fillcolor("brown")
phi = 137.508 * (math.pi/ 180.0)

for i in range (200):
    r = 4 * math.sqrt(i)
    theta = i*phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    penup()
    goto(x, y)
    setheading(i * 137.508)
    pendown()
    stamp()

def mostrar_te_amo():
    root = tk.Tk()
    root.geometry("200x100")
    label = tk.Label(root, text="Te amo", font=("Helvetica", 26))
    label.pack()
    root.mainloop()

mostrar_te_amo()
