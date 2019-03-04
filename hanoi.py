def hanoi(n):
    if n == 1:return 1
    else: return 2 + 3*hanoi(n-1)
     
# f(n) = 3 + f(n-1)
print(hanoi(10))