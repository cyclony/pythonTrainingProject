# list comprenhensions

threes_and_fives = [x
                    for x in range(1, 16)
                    if x % 3 == 0 or x % 5 == 0]
print(threes_and_fives)

l1 = [1, 2, 3]
l2 = ["abc", "def", "Easta"]

# dictionary comprehensions
d = {l1[i]:l2[i] for i in range(len(l1))}
d = {i: i*2 for i in l1}
# list comprehensions
l = [a.upper() for a in l2]

# dict convert to list

l = d.items()


myList = []

print(l)
