#yield相当于声明一个function是一个generator类，其行为类似一个iterator
import collections
def generator_test(lists):
    for x in lists:
        if isinstance(x, collections.Iterable): yield from generator_test(x)
        else:yield x

aa = [1,2,[3,4,[3,4]]]


a=[1,0,3,4,0,5]
def fun():
    yield 1
    return
    yield 2
    yield 3



for i,  in enumerate(aa):
    print(i)

for x in fun():
    print(x)

