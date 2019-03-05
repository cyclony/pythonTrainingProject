import itertools

#normal
class ArithmaticGen:
    def __init__(self, begin, step, end=10):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        i=0
        while i<self.end:
            yield self.begin + i*self.step
            i+=1

a = ArithmaticGen(1,0.25)
print(list(a))


#use itertools to figure it out
gen = itertools.takewhile(lambda n:n<5, itertools.count(1,0.25))
print(list(gen))

#itertools.product M * N matrix array
letters = 'A B C D'.split()
numbers = [str(x) for x in range(1,4)]
gen = itertools.product(letters, numbers)
print(list(gen))

#use itertools.filter
gen = itertools.filterfalse(lambda n:n%2==0, range(10))
print(list(gen))
gen = filter(lambda n:n%2==0, range(20)) #buildin function
print(list(gen))

#itertools.accumulate
gen = itertools.accumulate(numbers)
print(list(gen))

gen = itertools.chain(letters, numbers)
print(list(gen))