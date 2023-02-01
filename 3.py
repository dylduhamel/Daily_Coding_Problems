# FINISHED
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    result = []

    def dfs(node):
        if node == None:
            result.append("N")
            return #because its the base case
        result.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return ",".join(result)

def deserialize(stringTree):
    vals = stringTree.split(',')
    
    def dfs(i):
        if vals[i] == "N":
            i += 1
            return None
        node = Node((vals[i]))
        i += 1
        node.left = dfs(i)
        node.right = dfs(i)
        return node
    return dfs(0)



# This was given, and should pass
node = Node('root', Node('left', Node('left.left')), Node('right'))
#print(serialize(node))
assert deserialize(serialize(node)).left.left.val == 'left.left'
