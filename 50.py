class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def arithmetic(root):
    return arithRecursive(root)

def arithRecursive(node):
    if not Node:
        return

    opperand = node.val
    if opperand == '+':
        return arithRecursive(node.left) + arithRecursive(node.right)
    elif opperand == '-':
        return arithRecursive(node.left) - arithRecursive(node.right)
    elif opperand == '*':
        return arithRecursive(node.left) * arithRecursive(node.right)
    elif opperand == '/':
        return arithRecursive(node.left) / arithRecursive(node.right)
    elif opperand >= 0:
        return opperand

if __name__ == '__main__':
    root = Node('*')
    root.left = Node('+')
    root.right = Node('+')
    root.left.left = Node(3)
    root.left.right = Node(2)
    root.right.left = Node(4)
    root.right.right = Node(5)

    print(arithmetic(root))
