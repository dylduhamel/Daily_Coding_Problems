#Note, you can improve the O(N) space complexity by only ever storing the
#last two elements, instead of a whole other maxSums arr
def maxSubset(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]

    maxSums = [0 for _ in array]

    maxSums[0] = array[0]
    maxSums[1] = max(maxSums[0], array[1])

    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])

    return maxSums[-1]

testList = [2, 4, 6, 2, 5]

print(maxSubset(testList))