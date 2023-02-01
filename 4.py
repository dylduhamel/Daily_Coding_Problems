#FINISHED

# Sorted solution (cheating) (breaks linear constraint since soring is at minimum O(n logn)
def missingInt(list):
    ptr = 0
    list.sort()

    while (ptr < len(list) - 1):
        if list[ptr] <= 0:
            ptr += 1
        else:
            if (list[ptr] + 1) != list[ptr + 1]:
                return (list[ptr] + 1)
            else:
                ptr += 1
    return (list[ptr] + 1)

sampleInput = [1,2,0]
print(missingInt(sampleInput))