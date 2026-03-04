# main.py

# 1. Importaciones estándar de Python
import os
import sys
import subprocess

# 2. Importaciones de terceros
# import requests
import numpy as np

# 3. Importaciones locales (tus propios módulos)
from src.sumar_restar import sumar, restar  # importar funciones específicas
import src.sumar_restar as calc             # importar todo el módulo
from src.Database import Database

# 4. Funciones auxiliares
def main():  
    db = Database()
    db.agregar("Elemento 1")
    db.agregar("Elemento 2")
    obtener = db.obtener_todos()
    print(f"Elementos en la base de datos: {obtener}")
    for dato in obtener:
            print(f"  - {dato}")  

# 5. Punto de entrada principal
if __name__ == "__main__":
    os.system('cls') # Comando para limpiar pantalla en Windows
    print(calc.sumar(5, 3))
    main()
    
    # No recomendado: ejecutar un script como un subproceso
    resultado = subprocess.run(
        ["python", "src/sumar_restar.py"],
        capture_output=True,
        text=True
    )
    print(resultado.stdout)

    print(". . .Hecho")    
