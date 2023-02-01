#FINISHED LOOK AT THIS ONE

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# Impliment car and cdr

# Given implementation of cons
def cons(a, b):
    def pair(f):
        return f(a,b)
    return pair

def car(pair):
    return pair(lambda a, b : a)

def cdr(pair):
    return pair(lambda a, b : b)


print(car(cons(3,4)))