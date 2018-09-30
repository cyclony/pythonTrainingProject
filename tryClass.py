#coding=utf-8

#define class
class myClass:
    def __init__(self, name, age): #init constructor function with params
        self.name = name
        self.age = age
    def showInfo(self): #def function here
        print("hi, this is "+ self.name +", and I'm " + str(self.age))

me = myClass("cyc",15)
me.showInfo()

#类继承list,并扩展方法和属性
class myList(list):
    def __init__(self):
        self.total = 0

    def showTotal(self):
        print(self.total)
    def append(self, obj):  #覆盖父类的方法
        list.append(self,obj)   #调用父类方法（需要显式传递self参数
        self.total = obj + self.total

print (myList())

l = myList()
l.append(3)
l.append(4)
print(l)
l.showTotal()

