import bisect
import random
# 通过 bisect实现对有序序列插入或者检索
grade = list(reversed('ABCDE'))
score_seg = [int(score) for score in '60 70 80 90'.split()]
for i in range(10):
    rd_score = random.randint(40, 100)
    print('score is', rd_score, 'grade is', grade[bisect.bisect(score_seg, rd_score)])

# 制作一个九九乘法表，并打印
x_list = []
for x in range(1, 10):
    x_list.append(' '.join(('{1}X{0}={2}'.format(x, y, x*y) for y in range(1, x+1))))

[print(x) for x in x_list]
