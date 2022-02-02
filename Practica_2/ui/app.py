from json.tool import main
from logging import root
import tkinter as tk
from turtle import width
from ui.activarPromocion import ActivarPromocion
from ui.historicoVentas import HistoricoVentas
from ui.inventario import Inventario
from ui.prepararCafe import PrepararCafe
from ui.prepararJugo import PrepararJugo
from ui.registroVenta import RegistroVenta
from ui.reportarIncidente import ReportarIncidente
from ui.consultarComision import ConsultarComision

class App:
    w = None
    window = None
    
    def __init__(self, nombre):
        self._nombre=nombre
    
    @classmethod
    def salir(cls):
        cls.w.destroy()

    @classmethod
    def activarPromocion(cls):     
        cafe = ActivarPromocion('n')
        frame = ActivarPromocion.start(cls.w)
        frame.place(x=0,y=0)
    
    @classmethod
    def consultarComision(cls):     
        cafe = ConsultarComision('n')
        frame = ConsultarComision.start(cls.w)
        frame.place(x=0,y=0)

    @classmethod
    def historicoVentas(cls):     
        cafe = HistoricoVentas('n')
        frame = HistoricoVentas.start(cls.w)
        frame.place(x=0,y=0)

    @classmethod
    def inventario(cls):     
        cafe = Inventario('n')
        frame = Inventario.start(cls.w)
        frame.place(x=0,y=0)

    @classmethod
    def prepararCafe(cls):     
        cafe = PrepararCafe('n')
        frame = PrepararCafe.start(cls.w)
        frame.place(x=0,y=0)
        
    @classmethod
    def prepararJugo(cls):     
        cafe = PrepararJugo('n')
        frame = PrepararJugo.start(cls.w)
        frame.place(x=0,y=0)
    
    @classmethod
    def reportarIncidente(cls):     
        cafe = ReportarIncidente('n')
        frame = ReportarIncidente.start(cls.w)
        frame.place(x=0,y=0)
    
    @classmethod
    def registroVenta(cls):     
        cafe = RegistroVenta('n')
        frame = RegistroVenta.start(cls.w)
        frame.place(x=0,y=0)
        
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
        menu2.add_command(label="Activar promoción", command= cls.activarPromocion)
        menu2.add_command(label="Consultar comisión", command= cls.consultarComision)
        menu2.add_command(label="Historico ventas", command= cls.historicoVentas)
        menu2.add_command(label="Inventario", command= cls.inventario)
        menu2.add_command(label="Preparar cafe", command= cls.prepararCafe)
        menu2.add_command(label="Prepara Jugo", command= cls.prepararJugo)
        menu2.add_command(label="Registro incidente", command= cls.reportarIncidente)
        menu2.add_command(label="Registro venta", command= cls.registroVenta)

        menu3 = tk.Menu(menubar)
        menubar.add_cascade(menu=menu3, label='ayuda')
        menu3.add_command(label="Acerca de")
        cls.w['menu'] = menubar
        

        return cls.w

        