#coding=utf-8
#list comperehension 和map操作一样，都比python的loop快得多（将近两倍的速度），因为是解析成c语言操作

#List comperehension VS map
#bad code
my_list = []
for i in range(1,11):
    my_list.append(i**3)
#just 1 line statement with list comperehension
my_list = [x**3 for x in range(1, 11)]

#just 1 line statement beautiful with map
my_list = [x**3 for x in range(1,11)]

#List comperehension VS filter
#bad code!
my_list = []
for i in range(1,11):
    if i%2 == 0:
        my_list.append(i)

#condition filter to generate list comprehension
my_list = [x for x in range(1,11) if x%2==0]
my_list = [x if x%2==0 else 0 for x in range(1,11)]

#combinate filter and map to generate a list below
my_list = list(map(lambda x:x**3, filter(lambda x:x%2==0, range(1,11))))
my_list = [x**3 for x in range(1,11) if x%2==0]

my_list = list(map(lambda x,y: x*y, range(1,11), range(1,11)))

my_list = list(x*y for x,y in zip(range(1,11), range(1,11)))
my_list = list(x*y*z for x,y,z in zip(range(1,11), range(1,11), range(1,11)))

print(my_list)
my_list = [(x,y,z) for x in range(3) for y in 'ABC' for z in [40, 50, 60]]

for _,x,_ in my_list:
    print(x)

print([x*y for x,y in zip([x for x in range(10)], [y for y in range(10)])])
