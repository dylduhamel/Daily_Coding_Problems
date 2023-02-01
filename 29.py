# Run length encoding

def run_length(s):
    encoded = ""
    count = 0

    for i in range(len(s)):
        count += 1
        # Last element
        if i == (len(s)-1):
            encoded += str(count) + s[i]
        elif s[i+1] != s[i] or s[i+1] == None:
            encoded += str(count) + s[i]
            count = 0

    return encoded

if __name__ == '__main__':
    test = "AAAABBBCCDAA"
    print(run_length(test))
