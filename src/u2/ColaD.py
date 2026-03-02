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
        return True if self.primero == None else False  # operador ternario
        # return not self.primero
     
    def peek(self):
        if self.isEmpty():
            return None
        return self.primero.valor

    def enqueue(self, valor):
        nuevoNodo = Nodo(valor)
        self.size += 1
        if self.isEmpty():
            self.primero = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            self.ultimo.sig = nuevoNodo
            self.ultimo = nuevoNodo
    
    def dequeue(self):
        pass
        
    
            
    def show(self):
        current = self.primero
        while current:
            print(current.valor, end ="->")
            current = current.sig
        print("NULL")

def main():
    myH = Cola()
    myM = Cola()
    myH.show() 
    
    myH.enqueue("Melchor")
    myH.enqueue("Gaspar")
    myH.enqueue("Baltazar")
    
    myH.show()

if __name__ == "__main__":
    os.system("cls")
    main()
    os.system("pause")
    
            
            
            
            
            
            
            
        
        

        
     


        