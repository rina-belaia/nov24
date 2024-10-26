#простой декоратор import time

def time_func(func):
    def wrapper():
        time_start_func = time.time()
        func()
        time_end_func = time.time()
        res = time_end_func - time_start_func
        print(f"{func.__name__} lasts {res} sec.")
    return wrapper

@time_func
def f_func():
    x_list = [i for i in range(1,1000000)]

@time_func
def s_func():
    x_list = [i for i in range(1, 1000000)]
@time_func
def t_func():
    x_list = [i for i in range(1, 1000000)]


f_func()
s_func()
t_func()


