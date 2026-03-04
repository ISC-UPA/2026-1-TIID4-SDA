# PS G:\Mi unidad\home\core\code\2026-1-TIID4-SDA> python.exe -m src.u3.testTree 
import os, sys
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))  # Agrega el directorio raíz al path

from Tree import Tree


def main():
    myH = Tree()
    myH.show()

    myH.insert("Melchor")
    myH.insert("Gaspar")
    myH.insert("Obama")
    myH.insert("Nava")
    myH.insert("Perez")

    print("\nÁrbol en forma gráfica:")
    myH.show()

    print("\nRecorrido inorder:")
    myH.inorder()

    print("\n\nBuscar 'Gaspar':", myH.search("Gaspar"))
    print("Buscar 'Carlos':", myH.search("Carlos"))


if __name__ == "__main__":
    main()
    os.system("pause")