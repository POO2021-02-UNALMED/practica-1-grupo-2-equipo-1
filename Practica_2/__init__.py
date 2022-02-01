from cgitb import handler, text
import tkinter as tk
from turtle import dot

window =  tk.Tk()
window.geometry('900x650')
window.title('Inicio')

def hojaDeVida():
    pass

def cambioDesarrollador1(evento):
    desarrollador.config(text="Nicolas")
    desarrollador.bind("<Button-1>", cambioDesarrollador2)
    
    foto1 = tk.Label(p6, width=160, height=160, bg = 'royalblue1')
    foto1['image'] = fotoNicolas1
    foto1.grid(column=0, row= 0)

    foto2 = tk.Label(p6, width= 160, heigh=160, bg = 'royalblue1')
    foto2['image'] = fotoNicolas2
    foto2.grid(column=1, row= 0)

    foto3 = tk.Label(p6, width= 160, heigh=160, bg = 'royalblue1')
    foto3['image'] = fotoNicolas3
    foto3.grid(column=0, row= 1)

    foto4 = tk.Label(p6, width= 160, heigh=160, bg = 'royalblue1')
    foto4['image'] = fotoNicolas4
    foto4.grid(column=1, row= 1)

def cambioDesarrollador2(evento):
    desarrollador.config(text="Alejandro")
    desarrollador.bind("<Button-1>", cambioDesarrollador3)
    
    foto1 = tk.Label(p6, width=160, height=160, bg = 'royalblue1')
    foto1['image'] = fotoAlejandro1
    foto1.grid(column=0, row= 0)
    
    foto2 = tk.Label(p6, width= 160, heigh=160, bg = 'royalblue1')
    #foto2['image'] = fotoAlejandro2
    #foto2.grid(column=1, row= 0)

    foto3 = tk.Label(p6, width= 160, heigh=160, bg = 'royalblue1')
    #foto3['image'] = fotoAlejandro3
    #foto3.grid(column=0, row= 1)

    foto4 = tk.Label(p6, width= 160, heigh=160, bg = 'royalblue1')
    #foto4['image'] = fotoAlejandro4
    #foto4.grid(column=1, row= 1)

def cambioDesarrollador3(evento):
    desarrollador.config(text="Pablo")
    desarrollador.bind("<Button-1>", cambioDesarrollador1)

    foto1 = tk.Label(p6, width=160, height=160, bg = 'royalblue1')
    foto1['image'] = fotoPablo1
    foto1.grid(column=0, row= 0)

    foto2 = tk.Label(p6, width= 160, heigh=160, bg = 'royalblue1')
    foto2['image'] = fotoPablo2
    foto2.grid(column=1, row= 0)

    foto3 = tk.Label(p6, width= 160, heigh=160, bg = 'royalblue1')
    foto3['image'] = fotoPablo3
    foto3.grid(column=0, row= 1)

    foto4 = tk.Label(p6, width= 160, heigh=160, bg = 'royalblue1')
    foto4['image'] = fotoPablo4
    foto4.grid(column=1, row= 1)


p1 = tk.Frame(master=window, width="435", height="640", bg="light sky blue")
p1.place(x=9, y = 0)

p2 = tk.Frame(master=window, width="435", height="640", bg="light sky blue")
p2.place(x=455, y = 0)

# p3
p3 = tk.Frame(master = p1, width="420", height="220", bg='royalblue1')
p3.place(x = 7, y = 9)

bienvenida = tk.Label(master=p3, 
                    text="BIENVENIDO AL SISTEMA AUROS", 
                    width = "30", 
                    height = "5", 
                    bg = 'royalblue1', 
                    font = 'helvetica', 
                    fg = 'white')

bienvenida.place(x=65, y= 60)

#p4
p4 = tk.Frame(master = p1, width="420", height="400", bg='royalblue1')
p4.place(x = 7, y = 235)

#fotoSistema1 = tk.PhotoImage(file='FotoSistema1.png')
foto = tk.Label(p4, width = 57, height=18, bg = 'white')
#foto['image'] = fotoSistema1
foto.place(x=6, y=6)

boton = tk.Button(p4, 
                width=44, 
                height=5, 
                bg='light sky blue', 
                text='IR AL SISTEMA',
                font = 'helvetica')

boton.place(x=7, y = 290)

#p5
p5 = tk.Frame(master = p2, width="420", height="220", bg='royalblue1')
p5.place(x = 8, y = 9)

texto = 'Pablo'
desarrollador = tk.Label(master=p5, 
                    text="Pablo", 
                    width = "30", 
                    height = "5", 
                    bg = 'royalblue1', 
                    font = 'helvetica', 
                    fg = 'white')

desarrollador.place(x=65, y= 60)

desarrollador.bind("<Button-1>", cambioDesarrollador1)

#p6
fotoAlejandro1 = tk.PhotoImage(file='FotoAlejandro1.png')

fotoPablo1 = tk.PhotoImage(file='FotoPablo1.png')
fotoPablo2 = tk.PhotoImage(file='FotoPablo2.png')
fotoPablo3 = tk.PhotoImage(file='FotoPablo3.png')
fotoPablo4 = tk.PhotoImage(file='FotoPablo4.png')

fotoNicolas1 = tk.PhotoImage(file='FotoNicolas1.png')
fotoNicolas2 = tk.PhotoImage(file='FotoNicolas2.png')
fotoNicolas3 = tk.PhotoImage(file='FotoNicolas3.png')
fotoNicolas4 = tk.PhotoImage(file='FotoNicolas4.png')

p6 = tk.Frame(master = p2, width="420", height="400", bg='royalblue1')
p6.place(x = 7, y = 235)

foto1 = tk.Label(p6, width = 206, height=195, bg = 'royalblue1')
foto1['image'] = fotoPablo1
foto1.grid(column=0, row= 0)

foto2 = tk.Label(p6, width= 206, heigh=195, bg = 'royalblue1')
foto2['image'] = fotoPablo2
foto2.grid(column=1, row= 0)

foto3 = tk.Label(p6, width= 206, heigh=195, bg = 'royalblue1')
foto3['image'] = fotoPablo3
foto3.grid(column=0, row= 1)

foto4 = tk.Label(p6, width= 206, heigh=195, bg = 'royalblue1')
foto4['image'] = fotoPablo4
foto4.grid(column=1, row= 1)


window.mainloop()