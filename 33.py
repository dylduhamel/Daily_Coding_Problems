# IMPORTANT
# Compute the median of a stream
# The trick for this is to use 

# Brute force and bad space complexity
def mediumStreamBF(stream):
    nums = []
    for count, i in enumerate(stream, 1):
        nums.append(i)
        nums.sort()
        if len(nums) % 1 == 0:
            print(nums[int(count/2)])
        else:
            num1 = nums[int(count/2)]
            num2 = nums[int((count/2)+1)]
            print(float(num1+num2/2))

test = [1, 4, 6, 7 ,8, 8]
mediumStreamBF(test)