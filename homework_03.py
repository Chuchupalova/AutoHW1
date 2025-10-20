alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don't much care where ——" said Alice.\n'
    '"Then it doesn't matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
single_quotes = [char for char in alice_in_wonderland if char == "'"]
print("\n=== Task 02 ===")
print("Одинарні лапки в тексті:", single_quotes)
print("Кількість одинарних лапок:", len(single_quotes))
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
black_sea = 436_402
azov_sea = 37_800
total_area = black_sea + azov_sea



# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods = 375_291
first_second = 250_449
second_third = 222_950
y = first_second + second_third - total_goods
x = first_second - y
z = second_third - y

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
month = 18
montly_payment = 1179
computer_price = month * montly_payment
print("computer_price =", computer_price, "grn" 

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("8019 % 8 =", 8019 % 8) 
print("9907 % 9 =", 9907 % 9) 
print("2789 % 5 =", 2789 % 5) 
print("7248 % 6 =", 7248 % 6)
print (7128 % 5 =", 7128 % 5)
print (19224 % 9 =", 19224 % 9)

# task 08
"""(
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
order = {
    "Pizza large": (4, 274),
    "Pizza medium": (2, 218),
    "Djuice": (4, 35),
    "Cake": (1, 350),
    "Water": (3, 21)
 }
 total_cost = sum(quantity * price for quantity, price in order.items())   
    

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos = 232
photos_per_page = 8
pages_needed = -(-photos // photos_per_page)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
fuel_per_100km = 9
tank_capacity = 48
fuel_needed = distance * fuel_per_100km / 100
refuels_needed = -(-fuel_needed // tank_capacity)
