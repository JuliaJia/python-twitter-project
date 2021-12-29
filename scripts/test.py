from decorators import timer
from decorators import timer2
import time


@timer
def testfunc():
    time.sleep(0.2)

testfunc()

n = 3
@timer2(n)
def testfunc2():
    time.sleep(0.2)

testfunc2()