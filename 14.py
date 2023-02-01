from random import uniform
from math import pow

def generate():
    return (uniform(-1,1), uniform(-1,1))

def inCircle(coord):
    return coord[0] * coord[0] + coord[1] * coord[1] < 1

def montiCarloPii():
    iterations = 10000000
    numInCircle = 0
    numOutCircle = 0

    for _ in range(iterations):
        if inCircle(generate()):
            numInCircle += 1
        else:
            numOutCircle += 1
    
    return (numOutCircle/numInCircle) * 4

print(montiCarloPii())