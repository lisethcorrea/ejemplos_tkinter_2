from tkinter import Tk, Canvas, mainloop

ancho = 400
alto = 200
intervalo = 50

root = Tk()
root.resizable(False, False)

canvas = Canvas(width=ancho, height=alto)

for x in range(0, ancho, intervalo):
    canvas.create_line(x,0, x, alto)
for y in range(0, alto, intervalo):
    canvas.create_line(0,y, ancho, y)

canvas.pack()
mainloop()