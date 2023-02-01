def isPalindrome(s: str) -> bool:
    result = ""
    for c in s:
        if c.isalnum():
            result += c.lower()

    startPtr = 0
    endPtr = len(result)-1
    while startPtr <= endPtr:
        if result[startPtr] != result[endPtr]:
            return False
        else:
            startPtr += 1
            endPtr -= 1
    return True
if __name__ == '__main__':
    s = "haah"
    print(isPalindrome(s))
