import sys
import time
import functools
import itertools

sys.setrecursionlimit(1000)
results = dict()
counts = dict()

# 装饰器，记录调用函数执行结果的累计次数，以评估优化前后调用次数的差异性
def counter(func):
    def func_wrapper(n):
        if n in counts: counts[n] += 1
        else: counts[n] = 1
        return func(n)
    return func_wrapper

# 装饰器，用来对函数调用的执行时间进行测量，评估性能好坏
def timing(func):
    def func_wrapper(*args):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        elapse = end_time - start_time
        func_name = func.__name__
        arg_str = ', '.join([repr(arg) for arg in args])
        print('[%0.8fs] %s(%s) -> %s' %(elapse, func_name, arg_str, result))
        return result
    return func_wrapper


# decorator function，模拟functions.lru_cache 对被装饰的函数执行结果进行缓存，一旦调用结果被缓存命中，则执行返回缓存数据
def cache(func):
    result_dic = {}
    def func_wrapper(n):
        if n not in result_dic: #  没有命中，则调用原函数执行，并对结果进行缓存
            result = func(n)
            result_dic[n] = result
        return result_dic[n]  # 命中缓存，直接返回之前调用生成的结果
    return func_wrapper


@timing
def fib1(n):
    if n == 0:
        results.update({0: 0})

    if n == 1:
        results.update({1: 0})
        return 0
    if n == 2:
        results.update({2: 1})
        return 1
    if n in results:
        return results[n]
    else:
        result = fib1(n - 1) + fib1(n - 2)
        results.update({n: result})
        return result


@functools.lru_cache()
@counter
def fib2(n):
    if n == 0: return 0
    if n == 1: return 0
    if n == 2: return 1
    else:
        return fib2(n-1) + fib2(n-2)

fib2(20)
print(counts)
print(sum(counts.values()))


#  仅仅使用generator函数，就能方便的实现fibonacci数列
def fib_gen():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield b


def fib_list(n):
    return list(itertools.islice(fib_gen(), n+1))


def fib3(n):
    return list(itertools.islice(fib_gen(), n+1))[n-1]
