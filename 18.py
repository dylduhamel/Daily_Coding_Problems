# Important

# Brute force has O(N*K)
def bruteForceKMax(arr, k):
    results = []
    for i in range(len(arr) - k + 1):
        results.append(max(arr[i:i+k]))
    
    return results

def KMax(arr, k)

testInput = [10, 5, 2, 7, 8, 7]
k = 3

print(bruteForceKMax(testInput, k))