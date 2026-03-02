from src.mat.fn import suma 

a = [[ 0 for _ in range(5)] for _ in range(3)]  # 3 X 5
b = [[0]*5 for _ in range(3)]  # 3 X 5
c = [[0]*5]*3  # 3 X 5

r = suma(2, 3)
print("Resultado de la suma:", r)


