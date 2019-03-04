import time
import numpy as np
from functools import wraps
import requests


#定义了多个装饰器函数，如下：
#定义了一个类来实现的装饰器
#decorator装饰器：一个装饰器案例，dummy装饰器演示
#timing装饰器：衡量函数执行效率
#retry_times装饰器：在异常抛出时候，尝试重试多次（参数指定）
#log装饰器：为函数执行添加log输出打印

#------------------用类来实现的装饰器案例------------------
#因为定义了__call__方法的类，对象可以直接以函数形式调用
class decorator_cls:
    def __init__(self, func):
        self.func = func
    def __call__(self, *param):
        print("begin hook")
        self.func(*param)
        print("end hook")


@decorator_cls #解释器会执行decorator_cls(func),这会创建一个装饰器的实例，这个实例可以直接callable
def func():
    print("this is function running")

#----------------decorator装饰器案例---------------------
def decorator(func):
    @wraps(func)#这个包装器保证被包装的func函数的相关属性（比如__name__等)还是func，而不是dec_wrapper
    def dec_wrapper(*param):#输入参数可以用可变参数来指定，如果不需要对参数做任何额外的处理
        func(*param)
    return dec_wrapper

@decorator
def show(name, age):
    print('hello, my name is ' + name)
    print('im '+str(age) + ' years old')

show('jane', 18) # decorator(show)
print(show.__name__) #因为有wraps包装器，保证了这里的属性还是show函数的

#-----------------------timing decorator--------------------
# 装饰器，用来对函数调用的执行时间进行测量，评估性能好坏
def timing(func):
    def func_wrapper(*args):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        elapse = end_time - start_time
        func_name = func.__name__
        arg_str = ', '.join([repr(arg) for arg in args])
        print('[%0.8fs] %s(%s) -> %s' %(elapse, func_name, arg_str, result))
        return result
    return func_wrapper

@timing
def gen_million_numbers():
    numbers = np.random.normal(0, 3, 1000000)

gen_million_numbers()

#--------------------try_times decorator----------------------
#带参数的decorator案例：
#定义一个重试的decorator，由被装饰的对象指定重试次数，在函数出错的时候,
#在网络访问的时候，这个方法特别有用，可以平滑网络不稳定造成的偶尔失败
def try_times(max_times, sleep_secs):
    def retry_decorator(func):
        def dec_wrapper(*param):
            retry_times = 0
            while retry_times <max_times:
                try:
                    return func(*param)
                except Exception as e:
                    retry_times +=1
                    print('encount error:', e)
                    time.sleep(sleep_secs)
                    if retry_times ==max_times:
                            raise e
        return dec_wrapper
    return retry_decorator

@try_times(3, 1)
def get_page(name): #仔细观察该函数执行方式：try_times(3)(get_page)
    requests.get("https://www.google.com/search?q=python")
    print('hello this is '+name)

get_page('cyc')
print(get_page.__name__)
#测试应用timing装饰器查看函数执行效率


