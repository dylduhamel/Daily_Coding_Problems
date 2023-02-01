# Apple
import time

def jobScheduler(func, n):
    time.sleep(n/1000)
    func()

def testFunc():
    print("Hello! Dylan ROCKS\n")

jobScheduler(testFunc, 1000)