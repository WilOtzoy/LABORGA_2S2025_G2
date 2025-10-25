# Contiene todos los procedimientos y funciones que serán utilizados
# al momento de establecer conexión serial con Arduino

import time
from pathlib import Path
from tkinter import messagebox
from tkinter.ttk import Progressbar

import serial


#################################################
# CONEXIÓN CON ARDUINO
#################################################
def conectar_puerto(puerto: str):
  con = serial.Serial(puerto, 9600, timeout=1)
  time.sleep(6)
  try:
    if not con.is_open:
      con.open()
      time.sleep(6)
  except Exception as e:
    print(e)
    return None
  return con

def ping(conexion: serial.Serial):
  try:
    if not conexion.is_open:
      conexion.open()
      time.sleep(6)
    conexion.write(b'ping')
    time.sleep(1)
    res = conexion.readline()
    if res.decode() == 'pong':
      return True
  except Exception as e:
    print(e)
    return False
  
def _enviar(conexion: serial.Serial,  comandos: list[str]):
  conexion.write(b'PC')
  time.sleep(2)
  for cmd in comandos:
    conexion.write(cmd.encode())
    time.sleep(0.5)
    res = conexion.readline().decode().strip()
    print(res)
    if res == 'OK':
      continue
    elif res == 'ERROR':
      raise SyntaxError('Se ha detectado un error en la sintaxis del archivo .org\n\nPor favor revise y vuelva a intentar.')
    elif res == 'EEPROM':
      raise SystemError('Se ha experimentado un error con la memoria EEPROM de arduino\n\nPor favor revise y vuelva a intentar.')
    else:
      raise Exception('Se ha experimentado un error desconocido.')
  return True


#################################################
# ANALISIS DE ARCHIVO .ORG
#################################################
def _limpiar(contenido: list[str]):
  buffer: list[str] = []
  for c in contenido:
    if c.startswith('//') or c.isspace() or len(c) == 0:
      continue
    else:
      buffer.append(c.split('//')[0].strip().replace("LED’S", "LED'S").lower())

  
  return buffer

def _leer(archivo: Path):
  buffer = []
  with open(archivo, 'r') as f:
    buffer = f.readlines()
  return buffer

#################################################
# CONTROL DE ELEMENTOS GRÁFICOS
#################################################
def _control_progressbar(pb: Progressbar, activar = True):
  if activar:
    pb.start()
  else:
    pb.stop()


#################################################
# PROCESO PRINCIPAL
#################################################

def iniciar(conexion: serial.Serial, archivo: Path, pb: Progressbar):
  _control_progressbar(pb)
  contenido = _leer(archivo)
  contenido = _limpiar(contenido)
  contenido.append('eof') # End Of File
  try:
    _enviar(conexion, contenido)
    messagebox.showinfo('Éxito', 'Se ha procesado el archivo con éxito.')
  except SyntaxError as e:
    messagebox.showerror('SyntaxError', str(e))
  except SystemError as e:
    messagebox.showerror('SystemError', str(e))
  except Exception as e:
    messagebox.showerror('Error desconocido', str(e))
    print(e)
  finally:
    _control_progressbar(pb, False)
    
