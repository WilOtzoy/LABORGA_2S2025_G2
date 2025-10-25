# Controlador de la interfaz gráfica de usuario.

import sys
import os
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path

from vista import UI
import conexion

class App(tk.Tk):
  
  def __init__(self, **kw):
    super().__init__(**kw)
    self.arduino = None # Conexion con arduino

    if sys.platform == 'linux':
      ttk.Style(self).theme_use('clam')
    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(0, weight=1)
    self.title("Casa Orga 2025")
    self.resizable(0, 0)
    self.ui = UI(self)

    self.ui.btn_conectar_puerto.configure(command=self.on_conectar_puerto)
    self.ui.btn_prueba_puerto.configure(command=self.on_prueba_puerto)
    self.ui.btn_cargar_config.configure(command=self.on_cargar_config)
    self.ui.btn_ejecutar.configure(command=self.on_ejecutar)
    self.bind('<Destroy>', lambda e: self.on_destroy())

  def on_conectar_puerto(self):
    puerto = self.ui.entry_puerto.get()
    self.arduino = conexion.conectar_puerto(puerto)
    if self.arduino:
      messagebox.showinfo('Exito', 'Se ha establecido conexión')
    else:
      messagebox.showerror('Sin respuesta', f'No se ha detectado el arduino en {puerto}')

  def on_prueba_puerto(self):
    if conexion.ping(self.arduino):
      messagebox.showinfo('Exito', 'El canal de comunicación serial está listo.')
    else:
      messagebox.showerror('Lo siento', 'Ocurrió un error durante la prueba.')

  def on_cargar_config(self):
    archivo = filedialog.askopenfile(
      initialdir=os.getcwd(),
      title='Seleccione un archivo de configuración'
    )
    if archivo:
      self.ui.entry_archivo.delete(0, 'end')
      self.ui.entry_archivo.insert(0, archivo.name)

  def on_ejecutar(self):
    archivo = Path(self.ui.entry_archivo.get())
    hilo = threading.Thread(
      target=conexion.iniciar,
      args=(self.arduino, archivo, self.ui.progress_ejecutar)
    )
    hilo.start()

  def on_destroy(self):
    if self.arduino and self.arduino.is_open:
      self.arduino.close()
