# Recursive
def powerSet(set):
    if not set:
        return [[]]
    result = powerSet(set[1:])
    return result + [subset + [set[0]] for subset in result]

# Tried an iterative implementation, not finished.
def powerSetIter(set):
    powerSet = [[], [set]]:
    for i in range(len(set)):
        powerSet.append([set[i]])
        for j in range(i, len(set)):
            powerSet.append([set[i]].append())

if __name__ == '__main__':
    testSet = [1, 2, 3]

    print(powerSet(testSet))
