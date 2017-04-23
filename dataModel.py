import random

class Factor:
    def __init__(self, n):
        self.i = 1
        self.total = 1
        self.n = n
    def __iter__(self):#python解释器一旦碰到的类有这个方法，则该类对象是iterable的
        return self

    def __next__(self): #for循环执行的时候会内部调用该方法来实现迭代。
        if self.i == self.n:
            raise StopIteration
        self.total = self.total * self.i
        self.i += 1
        return self.total

factor = Factor(10)
for i in factor:
    print(i)

l = [x*y for x in range(5)
         for y in range(10)
     if x>0 and y>0]

odds = [x for x in range(100)
                if x%2 != 0]
print("this is odds:")
print(odds)

l += [123,456,789]



