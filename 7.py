# FINISHED LOOK AT THIS ONE
def num_encodings(s):
    if s.startswith('0'):
        return 0
    elif len(s) <= 1: # This covers empty string
        return 1

    total = 0 # The origional calling function will have the total added by all of the others

    if int(s[:2]) <= 26:
        total += num_encodings(s[2:]) # If 2 works, then start after that

    total += num_encodings(s[1:]) # But would also want to do 11 as a + a, not just as 11 K
    return total


testMessage = '111'

print(num_encodings(testMessage))