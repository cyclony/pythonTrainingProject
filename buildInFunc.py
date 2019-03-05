#filter, map, zip, reduce, sum, all, any, 都是针对列表数据进行快速处理的

squares = [x**2 for x in range(1,11)]#使用列表推导生成一个list
l1 = [1,2,3]
l2 = [4,5,6]

#map操作
print(list(map(lambda x:x*2, squares))) #使用map对列表每个数据进行变换处理
print([x*2 for x in squares])           #仅仅使用列表推导也能实现同样的map工作
print(list(map(lambda x,y:x+y, l1,l2))) #对于多个列表的map，这个操作无法使用列表推导来实现

#zip操作
print('list(zip)',list(zip(l1,l2)))                  #zip将两个list中对应位置的数据合并成tuple
print('*zip',*zip(l1,l2))
print(list(filter(lambda x: x>=30 and x<= 70, squares)))

#all， any
print(all([True,False, False])) #if all elements is true then return true
print(any([True, True, False])) #if any one element is true the return true
print(any([True, True, False]))
