import sys
import time
sys.setrecursionlimit(1000)
results = dict()

def timing(func):
    def func_wrapper(n):
        start_time = time.perf_counter()
        result = func(n)
        end_time = time.perf_counter()
        print('fib1 process ', str(n), ' the time is', str(end_time - start_time))
        return result
    return func_wrapper

@timing
def fib1(n):
    if n == 1:
        results.update({1:0})
        return 0
    if n == 2:
        results.update({2:1})
        return 1
    if results.get(n): return results.get(n)
    else:
        result = fib1(n - 1) + fib1(n - 2)
        results.update({n:result})
        return result

def fib2(n):
    if n == 1: return 0
    if n == 2: return 1
    else:
        return fib2(n-1) + fib2(n-2)

print(fib1(30))
print(fib1(40))
print(fib1(80))

