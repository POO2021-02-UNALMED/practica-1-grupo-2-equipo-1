import tkinter as tk
from personas.barista import Barista

class ConsultarComision:
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
                        text='Consultar comision',
                        font = 'helvetica',
                        bg = 'royalblue1',
                        fg='white',
                        width=15,
                        height=1)
        
        nombre.place(x=385, y = 10)
        descripcion = tk.Label(cls.frame,
                            text = '''Como parte de un esfuerzo de la compañía
los baristas tienen derecho a comisionar sus ventas
a partir de ciertos requisitos, esta funcionalidad 
permite ver en todo momento como se han 
desempeñado los baristas en este ambito''',
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

        label = tk.Label(frame, text='En este momento los baristas tienen las\n siquientes comisiones',
                        bg='royalblue1', 
                        fg ='white',
                        width=30,
                        height=5)
        
        label.pack()
        
        for barista in Barista.getBaristas():
            tk.Label(frame,text = barista.getNombre() + " comisiona al " + str(barista.getComisionAcumulada()) +  "% y ha comisionado " + str(barista.getComisionVentas()), bg = 'royalblue1', fg='white').pack()
        
        frame.place(x=300, y=200)
        return cls.frame