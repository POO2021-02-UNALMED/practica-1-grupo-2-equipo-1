from turtle import width
from noPersonas.bebida import Bebida
from noPersonas.cafe import Cafe
import tkinter as tk

class Inventario:
    frame = None
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    @classmethod
    def start(cls, window):
        cls.frame = tk.Frame(window, 
                            width="900", 
                            height="700", 
                            bg='light sky blue')
        
        nombre = tk.Label(cls.frame, 
                        text='Inventario',
                        font = 'helvetica',
                        bg = 'royalblue1',
                        fg='white',
                        width=15,
                        height=1)
        
        nombre.place(x=385, y = 10)
        descripcion = tk.Label(cls.frame,
                            text = '''Permite consultar el inventario actual
tanto de jugos como de cafés''',
                            font='helvetica',
                            bg = 'royalblue1',
                            fg='white',
                            width = '40',
                            height='5')
        
        descripcion.place(x=270, y = 50)
        #cafes = tk.Entry(cls.frame,width="50")
        #cafes.pack
        #label2 = tk.Label(cls.frame, text="Se prepararon " + "" + " cafés.")
        #label2.place(x=0,y=0)
        #boton = tk.Button(cls.frame)
        #boton.place(x=100,y=100)
        return cls.frame