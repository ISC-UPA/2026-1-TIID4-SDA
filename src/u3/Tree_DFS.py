# DFS Depth First Search = Busqueda en profundidad
# arbol en profundidad: preorden, inorden y postorden.
import os

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
       return str(self.left.data if self.left else None) + "<-" + str(self.data) + "->" + str(self.right.data if self.right else None)
    
def graphTree(nodo_actual, prefix="", is_left=True):
    if nodo_actual is not None:
        graphTree(nodo_actual.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(nodo_actual.data))
        graphTree(nodo_actual.left, prefix + ("    " if is_left else "│   "), True)

def preOrderTraversal(node): # Nid +ab
    if node: 
        print(node.data, end=", ")
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)

def inOrderTraversal(node): # iNd  a+b
    if node:
        inOrderTraversal(node.left)
        print(node.data, end=", ")
        inOrderTraversal(node.right)

def postOrderTraversal(node): # idN ab+
    if node:
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        print(node.data, end=", ")

def inOrderTraversalArray(node): # iNd a+b
    global array
    if node:
        inOrderTraversalArray(node.left)
        array.append(node.data)
        inOrderTraversalArray(node.right)

def inOrderTraversalStr(node): # iNd a+b
    if node is None:
        return []
    return inOrderTraversalStr(node.left) + [str(node.data)] + inOrderTraversalStr(node.right)

def main():
    root = TreeNode(13)
    node7 = TreeNode(7)
    node15 = TreeNode(15)
    node3 = TreeNode(3)
    node8 = TreeNode(8)
    node14 = TreeNode(14)
    node19 = TreeNode(19)
    node18 = TreeNode(18)

    root.left = node7
    root.right = node15

    node7.left = node3
    node7.right = node8

    node15.left = node14
    node15.right = node19

    node19.left = node18

    # Test
    print("Nodo:", root)
    
    
    print("root.right.left.data:", root.right.left.data)
    graphTree(root)
    # Traverse
    inOrderTraversal(root)

    inOrderTraversalArray(root)
    print("\nArray:", array)
    
    cadena = " ".join(inOrderTraversalStr(root))
    print("\nCadena:", cadena)

if __name__ == "__main__":
    os.system("cls")
    array=[]
    main()
    print()
    os.system("pause")
