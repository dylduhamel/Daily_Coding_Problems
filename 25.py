# Interesting regex problem
# My attpempt uses a stack and we pop off and do different things based on . or *

# I was naieve and should have noticed this being a recursive problem!
from collections import deque

def regex_match(s, rex):
    strStack = deque(c for c in s)
    rexStack = deque(c for c in rex)
    c = strStack.popleft()
    rex = rexStack.popleft()
    while strStack:
        rexPrev = rex
        cPrev = c
        
        if rex == "*":
            if rexPrev == ".":
                while rex != c:
                    c = strStack.popleft()
                    rex = rexStack.popleft()
            else:
                pass
        if c != rex:
            return False
        # Get new char
        c = strStack.popleft()
        rex = rexStack.popleft()

    return True


# Recursive method
# This takes O(len(s) * len(r)) time and space, since we potentially need to iterate over each suffix substring again for each character.
def match_first_char(s, r):
    # The '.' matches with anything, but must be something
    return s[0] == r[0] or (r[0] == '.' and len(s) > 0)

def matches(s, r):
    if r == '':
        return s == ''

    if len(r) == 1 or r[1] != '*':
        # The first character in the regex is not followed by a *
        if match_first_char(s, r):
            return matches(s[1:], r[1:])
        else:
            return False
    else:
        # The first char is followed by a *
        # Try zero lrngth on t
        if matches(s, r[2:]):
            return True

        # Glob more prefixes until the first char of s doesnt match
        i = 0
        while match_first_char(s[i:], r):
            if matches(s[i+1:], r[2:]):
                return True
            i += 1




if __name__ == "__main__":
    s = "ray"
    rex = "ra."
    print(regex_match(s, rex))