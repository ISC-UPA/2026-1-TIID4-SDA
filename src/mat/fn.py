

def suma(a, b):
    return a + b

# definir una funcion que reciba una matriz y la imprima
def imprimir_matriz(matriz):      # snake_case,  camelCase   
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="\t")
        print()

def transponer_matriz(matriz):
    F = len(matriz)
    C = len(matriz[0])
    
    transpuesta = [[0] * F for i in range(C)]
    #transpuesta = [[0 for _ in range(F)] for _ in range(C)]

    # int[][] transpuesta = new int[C][F];  // Java

    for i in range(F):
        for j in range(C):
            transpuesta[j][i] = matriz[i][j]
    return transpuesta      

if __name__ == "__main__":
    # Ejemplo de uso
    matriz_ejemplo = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    transpuesta = transponer_matriz(matriz_ejemplo)
    print("Matriz original:")
    imprimir_matriz(matriz_ejemplo)

    print("\nMatriz transpuesta:")
    imprimir_matriz(transpuesta)