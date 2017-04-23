def decorator(func):
    def dec_wrapper(*param):#输入参数可以用可变参数来指定，如果不需要对参数做任何额外的处理
        print('this is decorator')
        func(*param)
    return dec_wrapper

@decorator
def show(name, age):
    print('hello, my name is ' + name)
    print('im '+str(age) + ' years old')

show('jane', 18) # decorator(show)

#带参数的decorator
def try_times(times):
    def decorator(func):
        def dec_wrapper(*param):
            for i in range(times):
              print('this is decorator')
            func(*param)
        return dec_wrapper
    return decorator

@try_times(3)
def show_times(name): #仔细观察该函数执行方式：try_times(3)(show_times)
    print('hello this is '+name)

show_times('cyc')
