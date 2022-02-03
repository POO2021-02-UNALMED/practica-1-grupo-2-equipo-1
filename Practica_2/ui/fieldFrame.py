import tkinter as tk
from tkinter import Frame
from excepciones.excepcionCampoNegativo import ExcepcionCampoNegativo
from excepciones.excepcionNegativos import ExcepcionNegativos
from excepciones.excepcionSinInfo import ExcepcionSinInfo
from excepciones.excepcionCampoVacio import ExcepcionCampoVacio

class FieldFrame(Frame):
    def __init__(self, f, tituloCriterios, criterios, tituloValores, valores, habilitado):
        self.aceptado = False
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

    def llenarDiccionario(self):
        excepcion = False
        for i in range(len(self.valores)):
            self.diccionario[self.criterios[i]["text"]] = self.valores[i].get()
            
            if self.valores[i].get().lstrip('-').isdigit():
                if int(self.valores[i].get()) < 0:
                    try:
                        raise ExcepcionCampoNegativo(self.valores[i].get())
                    except ExcepcionNegativos as f:
                        f.mostrarMensaje()
                        excepcion = True
                        
            elif self.valores[i].get() == '':
                try:
                    raise ExcepcionCampoVacio(self.criterios[i]["text"])
                except ExcepcionCampoVacio as f:
                    f.mostrarMensaje()
                    excepcion = True
        
        if not excepcion:
            tk.messagebox.showinfo('Aceptar', 'Información guardada')
            
    def aceptar(self):
        self.llenarDiccionario()
        self.aceptado = True
        
        self.borrar()
    
    def borrar(self):
        for valor in self.valores:
            valor.delete(0, "end")
            
    def getValue(self, criterio):
        if criterio in self.diccionario:
            return self.diccionario[criterio]
