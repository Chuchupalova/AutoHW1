#Генератор парных чисел от 0 до N

def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)

#Генератор чисел Фибоначчи до N

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

for num in fibonacci(50):
    print(num)

#Итератор для вывода списка

class ListIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        value = self.items[self.index]
        self.index += 1
        return value

my_list = ListIterator([1, 2, 3, 4])
for item in my_list:
    print(item)

#Итератор парных чисел в диапазоне 0 до N

class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.current <= self.n:
            num = self.current
            self.current += 1
            if num % 2 == 0:
                return num
            raise StopIteration

for x in EvenIterator(15):
    print(x)

#Декоратор логирует аргументы и результат

def log_call(func):
    def wrapper(*args, **kwargs):
        print('Args:', args, 'kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return wrapper

#Декоратор перехват и обрабатывает ошибки

def catch_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print('Error:', e)
    return wrapper
