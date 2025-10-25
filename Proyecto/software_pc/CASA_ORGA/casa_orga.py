#!/usr/bin/python3

# CASA ORGA
#
# Pequeño modulo de Python que carga la configuración
# de uno o varios perfiles al controlador (Arduino en este caso)
# de la casa automatizada.
#
# Laboratorio de Organizacion Computacional B
# Segundo semestre 2025
# Grupo #2

from controlador import App

if __name__ == '__main__':
  app = App()
  app.mainloop()