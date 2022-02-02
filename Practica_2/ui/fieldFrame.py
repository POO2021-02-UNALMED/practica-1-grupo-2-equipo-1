import tkinter as tk

class FieldFrame:
    def __init__(self, f, tituloCriterios, criterios, tituloValores, valores, habilitado):
        self.frame = tk.Frame(f,
                        width="800", 
                        height="600", 
                        bg='royalblue1')
        
        titulo = tk.Label(self.frame, 
                        text=tituloCriterios,
                        font = 'helvetica',
                        bg = 'royalblue1',
                        fg = "white",
                        width=15,
                        height=1)
        
        titulo.grid(column=0, row=0)
        
        for i in range(len(criterios)):
            fr = tk.Label(self.frame, 
                text=criterios[i],
                bg = 'royalblue1',
                fg = "white",
                width=15,
                height=1)
    
            fr.grid(column=0,row=i + 1)
        
        tvalores = tk.Label(self.frame,
                            text=tituloValores,
                            font = 'helvetica',
                            bg = 'royalblue1',
                            fg = "white")
        
        tvalores.grid(column=1, row=0)
        
        for i in range(len(valores)):
            en = tk.Entry(self.frame)
            en.insert(tk.END, valores[i])
            
            en.grid(column=1,row=i + 1)

    def getFrame(self):
        return self.frame