adwentures_of_tom_sawer = (
    "Tom gave up the brush with reluctance in his .... face but alacrity "
    "in his heart. And while the late steamer "
    "\"Big Missouri\" worked .... and sweated in the sun, "
    "the retired artist sat on a barrel in the .... shade close by, dangled his legs, "
    "munched his apple, and planned the slaughter of more innocents. "
    "There was no lack of material; boys happened along every little while; "
    "they came to jeer, but .... remained to whitewash. .... "
    "By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for "
    "a kite, in good repair; and when he played out, Johnny Miller bought in "
    "for a dead rat and a string to swing it with—and so on, and so on, "
    "hour after hour. And when the middle of the afternoon came, from being a "
    "poor poverty, stricken boy in the .... morning, Tom was literally rolling in wealth."
)
##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
text = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
text = text.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
import re
text = re.sub(r"\s+", " ", text)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
count_h = text.count("h")
print("number of letter 'h':", count_h)


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
words = text.split()
capital_words = [w for w in words if w [0].isupper()]
print(capital_words:", len(capital_words))


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
first = text.find("Tom")
second = text.find("Tom", first + 1)
print("first 'Tom':", second)")


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = text.split(".")


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
if len(adwentures_of_tom_sawer_sentences) >= 4:
    fourth_sentences = adwentures_of_tom_sawer_sentences[3].strip().lower()
    print("fourth_sentences:", fourth_sentences)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
starts_with_by = any(s.strip().startswith("By the time") for s in adwentures_of_tom_sawer_sentences)
print("sentence that begins 'By the time':", starts_with_by)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1].strip()
word_count = len(last_sentence.split())
print("number of words in the last sentence:", word_count)