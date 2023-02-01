# IMPORTANT 
# If I was to draw this out, the solution is obvious

# Recursive method to find len
def length(head):
    if head.next == None:
        return 0
    return 1 + length(head.next)

def intersection(a, b):
    aLen = length(a)
    bLen = length(b)

    currA = a
    currB = b

    # Making the len from 0 to the chared element the same for each
    if aLen > bLen:
        for _ in len(aLen - bLen):
            currA = currA.next
    elif bLen > aLen:
        for _ in len(bLen - aLen):
            currB = currB.next
    
    while currA != currB:
        currA = currA.next
        currB = currB.next
    
    return currA