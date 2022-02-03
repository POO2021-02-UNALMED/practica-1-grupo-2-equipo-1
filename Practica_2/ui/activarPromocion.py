from turtle import width
from noPersonas.bebida import Bebida
from noPersonas.cafe import Cafe
import tkinter as tk

class ActivarPromocion:
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
                        text='Activar promoción',
                        font = 'helvetica',
                        bg = 'royalblue1',
                        fg='white',
                        width=15,
                        height=1)
        
        nombre.place(x=385, y = 10)
        descripcion = tk.Label(cls.frame,
                            text = '''Esta funcionalidad le permite al administrador
activar las promociones a las que la empresa 
puede recurrir en caso de necesitar incrementar
las ventas''',
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

        label = tk.Label(frame, text='Activar promociones',
                        bg='royalblue1', 
                        fg ='white',
                        width=30,
                        height=5)
        
        label.pack()
        
        cls.activar = tk.IntVar()
        si = tk.Radiobutton(frame, text='si',
        variable=cls.activar, value=1, bg='lightskyblue1', command=cls.isPromos)
        no = tk.Radiobutton(frame, text='no', variable=cls.activar,
        value=0,bg='lightskyblue1', command=cls.isPromos)
        si.pack()
        no.pack()
        
        frame.place(x=340, y=200)
        return cls.frame
    
    @classmethod
    def isPromos(cls):
        if cls.activar.get() == 1:
            return True
        return False