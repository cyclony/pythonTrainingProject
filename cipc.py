def fib(n):#定义一个递归过程实现
    if n == 1: return 1
    return fib(n-1) * n

print( fib(5))

def fib1(n): #定义一个迭代过程实现
    def iter_fib(total, n, i):
        total = total * i
        if i == n: return total
        else:
            return iter_fib(total, n, i+1)
    return iter_fib(1, n, 1)

print(fib1(5))

