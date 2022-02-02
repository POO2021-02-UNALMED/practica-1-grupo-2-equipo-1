from turtle import width
from noPersonas.bebida import Bebida
from noPersonas.cafe import Cafe
import tkinter as tk
from ui.fieldFrame import FieldFrame

class ReportarIncidente:
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
                        text='Reportar Incidente',
                        font = 'helvetica',
                        bg = 'royalblue1',
                        fg='white',
                        width=15,
                        height=1)
        
        nombre.place(x=385, y = 10)
        descripcion = tk.Label(cls.frame,
                            text = '''Debido a que la empresa maneja sus domicilios
con un tercero que brinda el servicio, esta 
funcionalidad permite reportar si alguna orden 
tuvo un incidente en su entrega, reportando ante
el sistema al domiciliario.''',
                            font='helvetica',
                            bg = 'royalblue1',
                            fg='white',
                            width = '40',
                            height='5')
        
        descripcion.place(x=270, y = 50)
        ff = FieldFrame(f = cls.frame, tituloCriterios="criterios", criterios=["Número de orden"], tituloValores="valores", valores=[0], habilitado=None)
        fframe = ff.getFrame()
        fframe.place(x=300, y=200)
        return cls.frame