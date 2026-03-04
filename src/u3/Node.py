class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
       return str(self.left.data if self.left else None) + "<-" + str(self.data) + "->" + str(self.right.data if self.right else None)

