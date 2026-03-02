import os

class Nodo:
    def __init__(self, valor):
        self.value = valor
        self.next = None

class Cola:
    def __init__(self):
        self.first = None
        self.last  = None
        self.size = 0
        
    def isEmpty(self):
        # return self.size == 0
        # if self.size == 0:
        #     return True
        # else:
        #     return False
        # return False if self.size == 0 else True
        
        # return not self.first
        return False if self.first else True

    def peek(self):
        if not self.isEmpty():
            return self.first.value
        return None
        
    def show(self):
        current = self.first
        while current:
            print(current.value, end='->')
            current = current.next
        print('NULL')
    
    def enqueue(self, x):
        newNode = Nodo(x)
        self.size += 1
        if self.isEmpty():
            self.first = newNode
            self.last =  newNode
        else:
            self.last.next = newNode
            self.last = newNode
 
def main():
     myH = Cola()
     myM = Cola()
     
     myH.enqueue("Melchor")
     myH.enqueue('Gaspar')
     myH.enqueue("Baltazar")
     myH.show()
          

     
if __name__ == "__main__":
    os.system("cls")
    main()
    os.system("pause")
    
    