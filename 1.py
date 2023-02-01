# FINISHED
def addK(list, k):
    map = {}
    y = 0;

    for x in list:
        y = k - x
        if map.get(y):
            return True
        else:
            map[x] = True
    # if nothing returned true
    return False

testIn = [10, 7]
k = 17

print(addK(testIn, k))
