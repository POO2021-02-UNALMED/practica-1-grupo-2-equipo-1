from json.tool import main
from logging import root
import tkinter as tk
from turtle import width
from ui.prepararCafe import PrepararCafe

class App:
    w = None
    window = None
    
    def __init__(self, nombre):
        self._nombre=nombre
    
    @classmethod
    def salir(cls):
        cls.w.destroy()

        
    @classmethod
    def iniciarSistema(cls, window):
        cls.window = window
        cls.w = tk.Tk()
        cls.w.geometry('900x650')
        cls.w.title('App')
        cls.w.option_add('*tearOff', False) 

        
        '''p1 = tk.Frame(master=cls.w, width="1000", height="100", bg="light sky blue")
        p1.place(x=0, y=10)'''
        
        menubar = tk.Menu(cls.w)
        menu1 = tk.Menu(menubar)
        menubar.add_cascade(menu=menu1, label='Archivo')
        menu1.add_command(label="Aplicación")
        menu1.add_command(label="Salir", command=cls.salir)
        
        menu2 = tk.Menu(menubar)
        menubar.add_cascade(menu=menu2, label='Procesos y consultas')
        #menu2.add_command(label="Aplicación")
        #menu2.add_command(label="Salir")

        menu3 = tk.Menu(menubar)
        menubar.add_cascade(menu=menu3, label='ayuda')
        menu3.add_command(label="Acerca de")
        cls.w['menu'] = menubar
        
        cafe = PrepararCafe('n')
        frame = PrepararCafe.start(cls.w)
        frame.place(x=0,y=0)
        return cls.w

        