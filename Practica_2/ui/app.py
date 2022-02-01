import tkinter as tk
from personas.administrador import Administrador
from personas.barista import Barista
from personas.domiciliario import Domiciliario
class App:
    window =  tk.Tk()
    window.geometry('900x650')
    window.title('Inicio')
    
    admin = Administrador(0,"Admin",0, "Admin", "0000");
    bar1 = Barista(100988877,"Julio Cárdenas");
    bar2 = Barista(100844433,"Stephanie Peréz");
    bar3 = Barista(100344521,"Camilo Montaner");
    dom1 = Domiciliario("Santiago Monsalve");
    dom2 = Domiciliario("Hernán Cortéz");
    dom3 = Domiciliario("Juan Goméz");
    
    def __init__(self, evento):
        pass
    
    @staticmethod
    def getWindow():
        App.window.mainloop