#yield相当于声明一个function是一个generator类，其行为类似一个iterator
import collections
def generator_test(lists):
    for x in lists:
        if isinstance(x, collections.Iterable): #if x is iterable the take recursive call
            yield from generator_test(x)
        else:yield x

aa = [1,2,[3,4,[3,4]]]


for x in generator_test(aa):
    print(x)


