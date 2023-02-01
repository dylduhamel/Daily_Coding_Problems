class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def reconstruct(inOrd, preOrd):
	if not inOrd or not preOrd:
		return None

	root = Node(preOrd[0])
	mid = inOrd.index(preOrd[0])
	
	root.left = reconstruct(inOrd[:mid], preOrd[1:mid+1])
	root.right = reconstruct(inOrd[mid+1:], preOrd[mid+1:])
	return root


if __name__ == '__main__':
	preOrder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
	inOrder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']

	print(reconstruct(inOrder, preOrder).value)