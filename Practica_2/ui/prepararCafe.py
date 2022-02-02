from turtle import width
from noPersonas.bebida import Bebida
from noPersonas.cafe import Cafe
import tkinter as tk

from ui.fieldFrame import FieldFrame

class PrepararCafe:
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
                        text='Preparar cafe',
                        font = 'helvetica',
                        bg = 'royalblue1',
                        fg='white',
                        width=15,
                        height=1)
        
        nombre.place(x=385, y = 10)
        descripcion = tk.Label(cls.frame,
                            text = '''Permite adicionar al inventario un determinado
número de cafés, mostrando que han sido 
previamente preparados por baristas''',
                            font='helvetica',
                            bg = 'royalblue1',
                            fg='white',
                            width = '40',
                            height='5')
        
        descripcion.place(x=270, y = 50)
        
        ff = FieldFrame(f = cls.frame, tituloCriterios="criterios", criterios=["cafes a preparar"], tituloValores="valores", valores=[0], habilitado=None)
        fframe = ff.getFrame()
        fframe.place(x=300, y=200)
        #cafes = tk.Entry(cls.frame,width="50")
        #cafes.pack
        Cafe.prepararCafes(0)
        #label2 = tk.Label(cls.frame, text="Se prepararon " + "" + " cafés.")
        #label2.place(x=0,y=0)
        #boton = tk.Button(cls.frame)
        #boton.place(x=100,y=100)
        return cls.frame