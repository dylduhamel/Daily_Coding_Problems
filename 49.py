# Problem states to do this in O(N) time

# Decently simple, all you really have to do is loop throught
# and find max of the element, or the progress up to that element
# if the element is bigger, then we start with that, if not we add the element
# to the running sum
def subarrayMax(list):
    maxSoFar = maxFromHere = 0
    for num in list:
        maxFromHere = max(num, maxFromHere + num)
        maxSoFar = max(maxSoFar, maxFromHere)
    return maxSoFar

if __name__ == '__main__':
    testInput = [34, -50, 42, 14, -5, 86]
    print(subarrayMax(testInput))
