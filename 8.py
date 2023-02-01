#FINISHED IMPORTANT
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def unival(root):

    def dfs(node):
        if node.left is None and node.right is None:
            return 1
        else: 
            return dfs(node.left) + dfs(node.right)
    
    return dfs(root)

# Making given node
root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.right = Node(0)
root.right.left = Node(1)
root.right.left.left = Node(1)
root.right.left.right = Node(1)

print(unival(root))