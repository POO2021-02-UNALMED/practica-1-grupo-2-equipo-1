import tkinter as tk
from tkinter import Frame

class FieldFrame(Frame):
    def __init__(self, f, tituloCriterios, criterios, tituloValores, valores, habilitado):
        super().__init__(master = f,
                        width = "1000",
                        height = "1200", 
                        bg = 'royalblue1')
        
        self.tituloCriterios = tk.Label(master = self, 
                        text = tituloCriterios,
                        font = 'helvetica',
                        bg = 'royalblue1',
                        fg = "white",
                        width = 15,
                        height = 2)
        
        self.tituloCriterios.grid(column=0, row=0)
        
        self.criterios = []
        
        for i in range(len(criterios)):
            self.criterios.append(tk.Label(self, 
                text=criterios[i],
                bg = 'royalblue1',
                fg = "white",
                width=15,
                height=2))
    
            self.criterios[i].grid(column=0,row=i + 1)
        
        self.tituloValores = tk.Label(self,
                            text=tituloValores,
                            font = 'helvetica',
                            bg = 'royalblue1',
                            fg = "white",
                            width=15,
                            height=2)
        
        self.tituloValores.grid(column=1, row=0)
        
        self.valores = []
        
        for i in range(len(valores)):
            self.valores.append(tk.Entry(self))
            self.valores[i].insert(tk.END, valores[i])
            
            self.valores[i].grid(column=1,row=i + 1)
        
        aceptar = tk.Button(self, 
                            width = 6, 
                            height=1, 
                            bg='light sky blue',
                            text='Aceptar',
                            font = 'helvetica',
                            command=self.aceptar)
        
        aceptar.grid(column=0,row=len(valores)+1)
        
        borrar = tk.Button(self, 
                        width="6", 
                        height="1", 
                        bg='light sky blue',
                        text='Borrar',
                        font = 'helvetica',
                        command=self.borrar)
        
        borrar.grid(column=1,row=len(valores)+1)
        
        self.diccionario = {}

    def aceptar(self):
        for i in range(len(self.valores)):
            self.diccionario[self.criterios[i]["text"]] = self.valores[i].get()
        
        tk.messagebox.showinfo('Aceptar', 'Información guardada')
        self.borrar()
    
    def borrar(self):
        for valor in self.valores:
            valor.delete(0, "end")
            
    def getValue(self, criterio):
        return self.diccionario[criterio]