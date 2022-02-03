from turtle import width
from noPersonas.bebida import Bebida
from noPersonas.cafe import Cafe
import tkinter as tk
from ui.fieldFrame import FieldFrame

class RegistroVenta:
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
                        text='Registro venta',
                        font = 'helvetica',
                        bg = 'royalblue1',
                        fg='white',
                        width=15,
                        height=1)
        
        nombre.place(x=385, y = 10)
        descripcion = tk.Label(cls.frame,
                            text = '''Esta funcionalidad le permite al administrador el 
registro y generación de una factura al momento de 
realizar una venta presencial o virtual''',
                            font='helvetica',
                            bg = 'royalblue1',
                            fg='white',
                            width = '40',
                            height='5')
        
        descripcion.place(x=270, y = 50)
        ff = FieldFrame('registro', f = cls.frame, 
                        tituloCriterios="criterios", 
                        criterios=["Número de barista", "Nombre cliente", "Número de cafes", "Número de jugos"], 
                        tituloValores="valores", 
                        valores=[0, "Juan",0,0], 
                        habilitado=None)
        
        ff.place(x=300, y=200)
        return cls.frame