#ДЗ 1 Студент и изменение среднего балла
class Student:
    def __init__(self, first_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def update_grade(self, new_grade):
        self.average_grade = new_grade
#ДЗ 2 Проверка слова на букву 'h'
def has_h_letter(word: str) -> bool:
    return "h" in word.lower()

#ДЗ 3Сумма чисел со стр.
def sum_nambers_from_string(s: str):
    try:
        return sum(map(int(x) for x in s.split(","))
    except Exception:
        return 0
