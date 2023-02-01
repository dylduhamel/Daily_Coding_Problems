# solid linked list problem
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
    
    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.value)
            current_node = current_node.next
        return str(result)

def remove_end(k, head):
    headPtr = head
    tailPtr = head

    for _ in range(k):
        tailPtr = tailPtr.next
    
    while tailPtr.next != None:
        headPtr = headPtr.next
        tailPtr = tailPtr.next

    # Removing the ptr
    temp = headPtr.next.next
    headPtr.next.next = None
    headPtr.next = temp

if __name__ == "__main__":
    head = Node(3)
    head.next = Node(8)
    head.next.next = Node(5)
    head.next.next.next = Node(7)
    head.next.next.next.next = Node(1)
    head.next.next.next.next.next = Node(9)

    k = 3

    print(head)
    remove_end(k, head)
    print(head)
