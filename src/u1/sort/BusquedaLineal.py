# generar un metodo que reciba un arreglo ordenado de enteros y un entero objetivo, 
# y retorne el indice del entero objetivo en el arreglo, o -1 si no se encuentra,
# utilando una busqueda lineal

# Busqueda lineal en un arreglo ordenado
# este metodo es ineficiente para arreglos ordenados,
# debemos modificarlo para que se detenga si el valor actual es mayor que el objetivo, ya que el arreglo esta ordenado

def busqueda_lineal(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1

def busqueda_lineal_mejorada(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
        elif arr[i] > objetivo:
            break
    return -1

def busqueda_lineal_while(arr, objetivo):
    i = 0
    while i < len(arr) and arr[i] <= objetivo:
        if arr[i] == objetivo:
            return i
        i += 1
    return -1


if __name__ == "__main__":
    arreglo_ordenado = [1, 3, 5, 7, 9, 11, 13, 15]
    objetivo = 20
    indice = busqueda_lineal(arreglo_ordenado, objetivo)
    if indice != -1:
        print(f"El entero {objetivo} se encuentra en el índice {indice}.")
    else:
        print(f"El entero {objetivo} no se encuentra en el arreglo.")


    indice_mejorada = busqueda_lineal_mejorada(arreglo_ordenado, objetivo)
    if indice_mejorada != -1:
        print(f"(Mejorada) El entero {objetivo} se encuentra en el índice {indice_mejorada}.")
    else:
        print(f"(Mejorada) El entero {objetivo} no se encuentra en el arreglo.")

    indice_while = busqueda_lineal_while(arreglo_ordenado, objetivo)
    if indice_while != -1:
        print(f"(While) El entero {objetivo} se encuentra en el índice {indice_while}.")
    else:
        print(f"(While) El entero {objetivo} no se encuentra en el arreglo.")
