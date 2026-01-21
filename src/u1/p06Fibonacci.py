#Python code for fibonacci Series
def fibonacci(n):
   if n == 0:
      return 0
   elif n == 1:
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
   # se cuenta a partir de la posicion 0
   # pos:       0  1  2  3  4  5  6
   # fib(pos):  0  1  1  2  3  5  8
   n = 6
   
   print("Fibonacci series upto number",n, "are:")
   print("0 1 2 3 4 5 6")
   for i in range(n+1):
      print(fibonacci(i) , end = " ")
   print()   
   print(fibonacci(6))
