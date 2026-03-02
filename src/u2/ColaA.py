import os

class Nodo: 
    def __init__(self, valor):
        self.valor = valor
        self.sig = None
        
        def __str__(self):
            return str(self.valor) + "->" + str(self.sig)
        
class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
        
    def isEmpty(self):
        #if self.size == 0:
        #    return True
        #return False
        # return True if self.size == 0 else False
        # return self.size == 0
        return not self.primero
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.primero.valor
    
    def show(self):
        current = self.primero
        while current:
            print(current.valor,  end="->")
            current = current.sig 
        print('NULL')
        
    def showCadena(self):
        arreglo = []
        current = self.primero
        while current:
            arreglo.append(current.valor)
            current = current.sig 
        return arreglo
    
    def enqueue(self, x):
        nuevoNodo = Nodo(x)
        self.size +=1
        if self.isEmpty():
            self.primero = nuevoNodo 
            self.ultimo =  nuevoNodo        
        else:
            self.ultimo.sig = nuevoNodo
            self.ultimo = nuevoNodo
            
    def dequeue(self):
        if self.isEmpty():
            self.ultimo = None
            return None
        self.size-=1
        valor=self.primero.valor
        self.primero =self.primero.sig
        return valor            
    
def main():
    myH = Cola()
    myM = Cola()
    
    myH.enqueue("Melchor")
    myH.enqueue("Gaspar")
    myH.enqueue("Baltazar")
    print(myH)
    print(myH.showCadena()) 
    print(myH.dequeue()) #1
    print(myH.showCadena())
    print(myH.dequeue()) #2
    print(myH.showCadena())
    print(myH.dequeue()) #3
    print(myH.showCadena())
    print(myH.dequeue()) #4 None
    print(myH.showCadena()) #NULL
    
    myM.enqueue("La niña")
    myM.enqueue("La pinta")
    myM.enqueue("La Santa Maria")

    myH.show()
    myM.show()
        

if __name__ == "__main__":
    os.system("cls")
    main()
    os.system("pause")

        
    
            
    
        
        
        
        
