import imp
from turtle import width
from noPersonas.bebida import Bebida
from noPersonas.cafe import Cafe
import tkinter as tk
from noPersonas.orden import Orden
from personas.barista import Barista

class HistoricoVentas:
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
                        text='Historico Ventas',
                        font = 'helvetica',
                        bg = 'royalblue1',
                        fg='white',
                        width=15,
                        height=1)
        
        nombre.place(x=385, y = 10)
        descripcion = tk.Label(cls.frame,
                            text = '''Esta funcionalidad le permite al administrador
observar todas las ventas que han tenido lugar, y 
llevar a si mismo un control de los ingresos del local''',
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

        label = tk.Label(frame, text='Hasta el momento las ventas han sido',
                        bg='royalblue1', 
                        fg ='white',
                        width=30,
                        height=5)
        
        label.pack()
        
        for barista in Barista.getBaristas():
            for orden in barista.getOrdenes():
                tk.Label(frame,text = orden.__str__(), bg = 'royalblue1', fg='white').pack()
        
        frame.place(x=250, y=200)   
        return cls.frame