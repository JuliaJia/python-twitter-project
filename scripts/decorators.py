import time

def timer(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print("function {funcname} cost {time} seconds".format(funcname=func.__name__,time=round(end - start, 2)))
    return inner

def timer2(n):
    def wrapper(func):
        def inner():
            start = time.time()
            func()
            end = time.time()
            print("function {funcname} cost {time} seconds,n is {n}".format(funcname=func.__name__, time=round(end - start, 2),n=n))
        return inner
    return wrapper
