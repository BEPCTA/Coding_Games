# -*- coding: utf-8 -*-

def memo(f):
    """
    Decorator that caches the return value for each call to f(args).
    Then when called again with the same args, we can just look it up
    """
    cache = {}
    def _f(*args):
        print("cache is ", cache)
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f

@memo
def fib(n):
    if n<= 1:
        return 1
    return fib(n-1) + fib(n-2)

@memo
def square(n):
    return n*n

print(fib(5))
print(fib(5))

print(square(5))
print(square(5))
print(fib(6))

    