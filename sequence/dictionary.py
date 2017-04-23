#dictionary init

d = {}
d[2] = "jane"
d[1] = "cyc"
d[3] = "Easta"
print(d)
#dict init from 2lists with zip() BIF
l1 = [1,2,3]
l2 = ["jane", "cyc", "Easta"]
d = dict(zip(l1, l2))
print(d)
d = {x:y for x,y in zip(l1,l2)}
print(d)
print(d.get(45,0))

l = zip(l1, l2)
print(l)
print(zip(*l))

#---------------------------
#sorting keys
sortedKeys = sorted(d.keys())
for i in sortedKeys:
    print(i)
    print(d[i])