import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))  # Agrega el directorio raíz al path

from src.mat.fn import suma 

def main():
    a = [[ 0 for _ in range(5)] for _ in range(3)]  # 3 X 5
    b = [[0]*5 for _ in range(3)]  # 3 X 5
    c = [[0]*5]*3  # 3 X 5

    print(suma(2, 3))

if __name__ == "__main__":
    os.system('cls') 
    main()
    print()
    os.system('pause')    


# PS G:\Mi unidad\home\core\code\2026-1-TIID4-SDa> $env:PYTHONPATH = "$PWD\src"
# PS G:\Mi unidad\home\core\code\2026-1-TIID4-SDa> python src/u1/matrices.py
#    G:\Mi unidad\home\core\code\2026-1-TIID4-SDA> python -m src.u1.Matrices
# Resultado de la suma: 5