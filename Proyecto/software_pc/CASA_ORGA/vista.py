# Contiene toda la interfáz gráfica de usuario.

import tkinter as tk
from tkinter import ttk, font

class UI(ttk.Frame):

  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    # Configuraciones
    self.configure(padding=5)
    self.grid(row=0, column=0, sticky='nswe')
    self.grid_columnconfigure(0, weight=1)
    self.__estilos()

    # Widgets
    frm_arduino = ttk.Frame(self)
    frm_arduino.grid_columnconfigure(0, weight=1)
    lbl_enc_arduino = ttk.Label(frm_arduino, text='ARDUINO DESTINO', style='Encabezado.TLabel')
    lbl_puerto_con = ttk.Label(frm_arduino, text='Puerto de conexión')
    self.entry_puerto = ttk.Entry(frm_arduino, font=self.__FONT_DEFAULT)
    self.btn_conectar_puerto = ttk.Button(frm_arduino, text='Conectar')
    self.btn_prueba_puerto = ttk.Button(frm_arduino, text='Probar conexión')

    frm_archivo = ttk.Frame(self)
    frm_archivo.grid_columnconfigure(0, weight=1)
    lbl_enc_archivo = ttk.Label(frm_archivo, text='ARCHIVO DE CONFIGURACIÓN', style='Encabezado.TLabel')
    lbl_seleccion_archivo = ttk.Label(frm_archivo, text='Seleccione un archivo .org')
    self.entry_archivo = ttk.Entry(frm_archivo, font=self.__FONT_DEFAULT)
    self.btn_cargar_config = ttk.Button(frm_archivo, text='Cargar configuración')

    frm_ejecutar = ttk.Frame(self)
    frm_ejecutar.grid_columnconfigure(0, weight=1)
    self.btn_ejecutar = ttk.Button(frm_ejecutar, text='Ejecutar')
    self.progress_ejecutar = ttk.Progressbar(frm_ejecutar, mode='indeterminate', orient='horizontal')

    # Posicionamiento
    frm_arduino.grid(row=0, column=0, sticky='nswe', pady=10)
    lbl_enc_arduino.grid(row=0, column=0, sticky='we')
    lbl_puerto_con.grid(row=1, column=0, sticky='we')
    self.entry_puerto.grid(row=2, column=0, sticky='we')
    self.btn_conectar_puerto.grid(row=3, column=0, sticky='we')
    self.btn_prueba_puerto.grid(row=4, column=0, sticky='we')

    frm_archivo.grid(row=1, column=0, sticky='nswe', pady=10)
    lbl_enc_archivo.grid(row=0, column=0, sticky='we')
    lbl_seleccion_archivo.grid(row=1, column=0, sticky='we')
    self.entry_archivo.grid(row=2, column=0, sticky='we')
    self.btn_cargar_config.grid(row=3, column=0, sticky='we')

    frm_ejecutar.grid(row=2, column=0, sticky='nswe', pady=10)
    self.btn_ejecutar.grid(row=0, column=0, sticky='we')
    self.progress_ejecutar.grid(row=1, column=0, sticky='we')

  def __estilos(self):
    self.__FONT_ENCABEZADO = font.Font(self, size=15, weight='bold')
    self.__FONT_DEFAULT = font.Font(self, size=11)

    e = ttk.Style(self)
    e.configure('TLabel', font=self.__FONT_DEFAULT)
    e.configure('TButton', font=self.__FONT_DEFAULT)
    e.configure('Encabezado.TLabel', font=self.__FONT_ENCABEZADO)
    