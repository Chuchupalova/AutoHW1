# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f"{number}x{multiplier}={result})

        # Increment the appropriate variable
        multiplier +=1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def add_numbers(a,b):
    return a + b

print(add_numbers(3, 5))
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    if len(numbers) == 0:
        return numbers 0
        return sum(numbers) / len(numbers)
        print(average([1, 2, 3, 4])

        #task 4##
        # """  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
def reverse_string(string):
        return string[::-1]
print(reverse_string("hello"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
def longest_word(words):
    if not words:
        return None
    return max(len(word) for word in words)
    print(longest_word(words))    

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    index = str1.find(str2)
    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
def add_numbers(a,b):
    return a + b

def average(numbers):
    if len(numbers) == 0:
    return numbers 0
        return sum(numbers) / len(numbers)

def reverse_string(string):
    return string[::-1]

def longest_word(words):
    if not words:
        return None
    return max(len(word) for word in words)
