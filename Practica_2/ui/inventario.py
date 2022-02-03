from turtle import width
from noPersonas.bebida import Bebida
from noPersonas.cafe import Cafe
from noPersonas.jugo import Jugo
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
        
        frame = tk.Frame(cls.frame,
                        width = "1000",
                        height = "1200", 
                        bg = 'royalblue1')

        label = tk.Label(frame, text="En este momento hay:\n\n"+ str(Cafe.getInventarioCafe())+" Cafés\n"+ str(Jugo.getInventarioJugo()) +" Jugos\n",
                        bg='royalblue1', 
                        fg ='white',
                        width=30,
                        height=5)
        
        label.pack()
                
        frame.place(x=350, y=200)   
        return cls.frame