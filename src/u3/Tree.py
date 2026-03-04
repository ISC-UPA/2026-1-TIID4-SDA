import os, sys
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))  # Agrega el directorio raíz al path
# from src.u3.Node import Node

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  
# from u3.Node import Node   # Importa la clase Node

from Node import Node

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
       return str(self.left.data if self.left else None) + "<-" + str(self.data) + "->" + str(self.right.data if self.right else None)
'''

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def show(self):
        if self.root is not None:
            self.graphTree(self.root)
        else:
            print("Tree is empty")

    def graphTree(self, nodo_actual, prefix="", is_left=True):
        if nodo_actual is not None:
            self.graphTree(nodo_actual.right, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(nodo_actual.data))
            self.graphTree(nodo_actual.left, prefix + ("    " if is_left else "│   "), True)

    def insert(self, data):
        def _insert(node, data):
            if node is None:
                return Node(data)
            if data < node.data:
                node.left = _insert(node.left, data)
            elif data > node.data:
                node.right = _insert(node.right, data)
            return node

        self.root = _insert(self.root, data)
        self.size += 1

    def inorder(self, node=None):
        # Si no se pasa nodo, empezamos desde la raíz
        if node is None:
            node = self.root

        # Caso base: si el nodo es None, no hacemos nada
        if node is None:
            return

        # Recursión: izquierda -> nodo -> derecha
        if node.left:
            self.inorder(node.left)
        print(node.data, end=" ")
        if node.right:
            self.inorder(node.right)

    def search(self, data):
        def _search(node, data):
            if node is None:
                return False
            if node.data == data:
                return True
            elif data < node.data:
                return _search(node.left, data)
            else:
                return _search(node.right, data)
        return _search(self.root, data)


