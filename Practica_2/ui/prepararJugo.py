from turtle import width
from noPersonas.bebida import Bebida
from noPersonas.jugo import Jugo
import tkinter as tk
from ui.fieldFrame import FieldFrame

class PrepararJugo:
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
                        text='Preparar Jugo',
                        font = 'helvetica',
                        bg = 'royalblue1',
                        fg='white',
                        width=15,
                        height=1)
        
        nombre.place(x=385, y = 10)
        descripcion = tk.Label(cls.frame,
                            text = '''Permite adicionar jugos al inventario,
llevando un registro digital de las preparaciones
de los baristas en el local''',
                            font='helvetica',
                            bg = 'royalblue1',
                            fg='white',
                            width = '40',
                            height='5')
        
        descripcion.place(x=270, y = 50)
        ff = FieldFrame('jugo', f = cls.frame, tituloCriterios="criterios", criterios=["jugos a preparar"], tituloValores="valores", valores=[0], habilitado=None)
        ff.place(x=300, y=200)
        
        return cls.frame