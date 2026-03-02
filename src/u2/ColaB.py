import os

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.sig = None

class Cola:
     def __init__(self):
         self.primero = None 
         self.ultimo = None
         self.size = 0

     def isEmpty(self):
         if self.primero is None:
             return True
         else:
             return False
         #return true if self.size == 0 else false 
         #return self.size == 0
         #return not self.primero
         
     def peek(self):  # muestra el primero     
        if self.isEmpty():
            return None
        return self.primero.valor
    
     def enqueue(self, x):
        nuevoNodo = Nodo(x)
        self.size= self.size + 1
        if self.isEmpty():
            self.primero = self.ultimo = nuevoNodo
        else:
            self.ultimo.sig = nuevoNodo
            self.ultimo = nuevoNodo

     def dequeue(self):
        pass
    
        
     def show(self):
        current = self.primero
        while current:
            print(current.valor, end = "->")
            current = current.sig
        print("Null")    
    
    
def main():
    myH = Cola()
    myM = Cola()
    myH.enqueue("Melchor")
    myH.enqueue("Gaspar")
    myH.enqueue("Baltazar")
    print(myH)
    myH.show()
    
    myM = Cola()
    myM.enqueue("Mary")
    myM.enqueue("Rosa")
    print("Direccion: ", myM)
    myM.show()
    

if __name__ == "__main__":
    os.system('cls')
    main()
    os.system('pause')
    
  
         
        