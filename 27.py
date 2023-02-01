# Important facebook [easy]
from collections import deque

def sym_braces(s):
    stack = deque()

    for c in s:
        if c == '(':
            stack.append(')')
        elif c == '[':
            stack.append(']')
        elif c == '{':
            stack.append('}')
        else:
            if not stack:
                return False
            reflection = stack.pop()
            if reflection != c:
                return False
    return not len(stack) > 0

if __name__ == "__main__":
    test = "([])[]({}))"

    print(sym_braces(test))