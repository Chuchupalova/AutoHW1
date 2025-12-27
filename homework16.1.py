#Task1
import csv
from multiprocessing.reduction import duplicate

file1 = 'random.csv'
file2 = 'random-michaels.csv'
output_file = 'result_chuchupalova.csv'
rows = []
for path in (file1, file2):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            rows.append(tuple(row))

unique_rows = list(set(rows))
duplicates_count = len(rows) - len(unique_rows)

with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(unique_rows)

print("Done ✔️")
print("Удалено дубликатов:", duplicates_count)
print("Всего строк:", len(rows))
print("Осталось строк (уникальных):", len(unique_rows))
print("Файл сохранён как:", output_file)

#Task2

import json
import logging

log_file = 'json_chuchupaloa.log'
logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
files = [
    'localization_en.json',
    'localization_ru.json',
    'login.json',
    'swagger.json'
]
for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            json.load(f)
        print(f'{file} - валидный JSON')

    except Exception as e:
        logging.error(f'{file} - невалидный JSON: {e}')
        print(f'{file} - не валидный, ошибка записана в лог')


#Task3

import xml.etree.ElementTree as ET
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
file = 'groups.xml'

def get_incoming_value(group_number: str):
    tree = ET.parse(file)
    root = tree.getroot()
    for group in root.findall('group'):
        number = group.find('number')
        if number is not None and number.text == group_number:
            timing = group.find('timingExbytes')
            if timing is not None:
                incoming = timing.find('incoming')
                if incoming is not None:
                    return incoming.text
    return None

number_to_find = '3'
value = get_incoming_value(number_to_find)
if value:
    logging.info(f'for group/number={number_to_find} значение incoming = {value}')
else:
    logging.info(f'group with number={number_to_find} not faund')
    