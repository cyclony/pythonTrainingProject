#通过set剔除list中的重复数据

l= [1,2,2,3,3,5]
l = list(set(l))
print(l)

#集合的操作，交，并，差操作
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
#集合的交集
print(len(s1 & s2))
#集合的差集
print(s1 - s2)
#集合的与非
print(s1 ^ s2)
#集合的并集
print(s1| s2)
#是否子集盘点
print(s1 <= s2)
print(s1 < s2)

#是否是其中的元素
print(1 in s1)
