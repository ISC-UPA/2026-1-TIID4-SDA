import sys
import os
# Add the parent directory of 'src' to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
#sys.path.append('g:/Mi unidad/home/core/code/2026-1-TIID4-SDA/')
# Esto añade: g:\Mi unidad\home\core\code\2026-1-TIID4-SDA\
import src.mat.fn as app
#from src.mat import fn as app

# Entrada de datos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

F = len(matriz)        # número de filas
C = len(matriz[0])     # número de columnas

# Proceso: calcular la transpuesta
# transpuesta = [[0] * F for _ in range(C)]
# transpuesta = [[0 for _ in range(F)] for _ in range(C)]

transpuesta = app.transponer_matriz(matriz)

# Salida de datos
print("Matriz Original:")
app.imprimir_matriz(matriz)

print("\nMatriz Transpuesta:")
app.imprimir_matriz(transpuesta)