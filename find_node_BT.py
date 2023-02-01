# How to find and return a node in a binary tree
# https://www.youtube.com/watch?v=YaofE8aDaWY
class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def find_node(value, node):
    if node is None:
        return None
    if node.value == value:
        return node
    left_node = find_node(value, node.left)
    if left_node: # left_node != None
        return left_node
    right_node = find_node(value, node.right)
    if right_node: # right_node != None
        return right_node
    return None

if __name__ == '__main__':
    root = Node(5)
    root.left = Node(10)
    root.right = Node(7)
    root.right.right = Node(2)
    root.left.right = Node(99)

    print(find_node(99, root).value)
