# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result
from operator import index
from tkinter.font import names

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
#добавяем новую запись в начале списка
my_records = ('Elena', 'Chuchupalova', 30, 'QA', 'Odessa')
people_records.insert(0, my_records)

#Меняем местами
people_records[1], people_records[5] = people_records[5], people_records[1]
print("Modified records:")
for i, person in enumerate(people_records):
    print(i, person)

#Проверка все ли люди в мод. списке с инд. 6, 10, 13 имеют возраст=>30
indexes_to_check = [6, 10, 13]
age_check = all(people_records[i][2]>= 30 for i in indexes_to_check)
print("Modified list:", people_records)
print("Do people at indexes 6, 10, 13 have age >= 30?", age_check)
