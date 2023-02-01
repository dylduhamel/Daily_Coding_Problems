##
# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
##
import random

def randLongStream(stream):
    randValue = 0
    count = 0
    i = 0

    while(1):
        if random.randint(0, count) == 1:
            randomValue = stream[i]
        
        count += 1
        i += 1
    
    return randValue

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element

randLongStream()