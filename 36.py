# Important In-order traversal of BST
# BST is sorted, so we can do an in-order traversal
# But normal in-order gives us smallest first, so we do that
# backwards and onlt store 2 values

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def secondLargest(root):
    def inOrder(node):
        # This is the base case
        if not node or count[0] == 2:
            return
        
        if node.right:
            inOrder(node.right)
        
        count[0] += 1

        if count[0] == 2:
            val.append(node.value)
            return
        
        if node.left:
            inOrder(node.left)
    
    count = [0]
    val = []
    inOrder(root)
    return val[0]

root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(7)

print(secondLargest(root))