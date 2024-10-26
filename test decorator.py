def square_func(n):
    num = 1
    while num <= n:
        yield pow(num, 2)
        num += 1


for num in square_func(20):
    print(num)
