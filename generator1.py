print("Обучалка")


def simple_generator():
    yield 3
    yield 6
    yield 345890


gen = simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))

print("Здание 1")


def count_up_to(max_value):
    count = 7
    while count <= max_value:
        yield count
        count += 1


for num in count_up_to(9):
    print(num)

print("Задание 2")


def number_generator(n):
    number = 1
    while number <= n:
        yield number
        number += 1


gen = number_generator(5)
print(list(gen))

print("Задание 3")


def even_number_generator(n):
    number = 0
    while number <= n:
        yield number
        number += 2


for num in even_number_generator(10):
    print(num)

print("Задание 4")


def square_even_numbers_generator(n):
    number = 1
    while number <= n:
        if number % 2 == 0:
            yield pow(number, 2)
        number += 1


for num in square_even_numbers_generator(10):
    print(num)

print("Задание 5")


def fibonacci_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


for num in fibonacci_generator(10):
    print(num)

print("Задание 6")


def step_generator(n, step):
    number = 0
    while number <= n:
        yield number
        number += step


for num in step_generator(10, 3):
    print(num)
