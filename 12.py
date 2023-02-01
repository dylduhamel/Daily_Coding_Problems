def uniqueStair(n):
    if n <= 1:
        return 1

    total = 0

    # This is basically the fib sequence
    # Runs in 2^N time, very bad
    if n >= 2:
        total += uniqueStair(n-2)
    total += uniqueStair(n-1)

    return total

def staircase(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a

testStair = 4

print(uniqueStair(testStair)) 