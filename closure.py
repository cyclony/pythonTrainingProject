from dis import dis


def make_average():  # 闭包函数，闭包是一个拥有自由变量（如下例的serial）的函数，自由变量在后续
    serial = []  # 这是一个闭包变量，在内部定义函数执行期间，类似一个扩展的局部变量

    def average(value):
        serial.append(value)
        return sum(serial)/len(serial)
    return average

avg = make_average()
print(avg(10))
print(avg(11))
print(avg(12))

print(avg.__closure__)
print(avg.__code__.co_freevars)
dis(make_average)  # 这个BIF方便我们很清楚知道编译后的字节码，清楚知道执行情况


# -------------如果闭包的自由变量是不可变的，那么需要通过nolocal声明来避免问题------------
def make_average():  # 闭包函数
    total = 0
    count = 0

    def average(value):
        nonlocal total  # 通过声明nonlocal 使得类似整型，字符串等不可变类型变量的闭包引用
        nonlocal count
        count += 1
        total += value
        return total / count
    return average

