#String[] valor = {"A","2","3","4","5","6","7","8","9","10","J","Q","K"};
#String[] figura = {"C♥","D♦","T♣","P♠"};















import random


def triangular1(n):
    for i in [[1 if i<=j else 0 for i in range(n)] for j in range(n)]: # [::-1]
        print(i)

def triangular2(n):
    for i in [[1 if i<=j else 0 for i in range(n)] for j in range(n)] [::-1]:
        print(i)

triangular1(5)
print()
triangular2(5)

matrix = [[random.randint(0,20) for i in range(5)] for j in range(5)]
print(matrix)

for i in range(5):
    for j in range(5):
        print(matrix[i][j], end="\t")
    print()
print()    
print(matrix[::-1])
