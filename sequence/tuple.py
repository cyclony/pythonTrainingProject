from collections import namedtuple

# tuple as recorder and unmutable sequence
names = ["cyc", "jane", "Easta"]
score = [85, 90, 87]
score_list = [x for x in zip(names, score)]
for name, score in score_list:
    print("name is :" + name+", score is :" + str(score))


# named tuples 可以用来作为数据对象使用了
Student = namedtuple('student', 'name age scores')
Jane = Student('Jane', 18, (78, 66, 89))
print(Jane.name)
print(Jane.scores)
print(slice(0,6))

# 读取结构化文件数据并使用tuple结构化数据
file_lines = [
    'cyc; 18;  60; 70; 90;',
    'jane; 34; 56; 45; 56;',
    'Easta; 56; 34; 55; 56;'
]
l = [(x.strip().split(";")[0],x.strip().split(";")[1],tuple(x.strip().split(";")[2:5])) for x in file_lines]
print(l)
for (name, age, *_) in l:
    print("name is :" + name + "; age is :" + age)
