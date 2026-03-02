# BST Binary Search Tree: Arbol Binario de Busqueda
# BFS Breadth First Search: Busqueda en amplitud = Avanza por Niveles
binary_tree_array = [13, 7, 15, 3, 8, 14, 19,  None, None, None, None, None, None, 18, None]

def left_child_index(index):
    return 2 * index + 1

def right_child_index(index):
    return 2 * index + 2

def pre_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return [binary_tree_array[index]] + pre_order(left_child_index(index)) + pre_order(right_child_index(index))

def in_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return in_order(left_child_index(index)) + [binary_tree_array[index]] + in_order(right_child_index(index))

def post_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return post_order(left_child_index(index)) + post_order(right_child_index(index)) + [binary_tree_array[index]]

print("Pre-order Traversal: ", pre_order(0))
print("In-order Traversal:  ", in_order(0))
print("Post-order Traversal:", post_order(0))
