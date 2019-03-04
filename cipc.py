import functools
import operator


def factorial(n):  # 定义一个递归过程实现
    if n == 1: return 1
    return factorial(n - 1) * n

print(factorial(5))


def factorial1(n):  # 定义一个迭代过程实现
    def iter_fact(total, n, i):
        total = total * i
        if i == n: return total
        else:
            return iter_fact(total, n, i+1)
    return iter_fact(1, n, 1)


# 使用reduce来累计计算乘积，求得阶乘（不需要使用递归)
def factorial2(n):
    return functools.reduce(operator.mul, range(1, n+1))
print(factorial1(10))

