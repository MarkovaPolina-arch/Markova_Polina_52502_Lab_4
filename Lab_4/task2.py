# TODO импортировать необходимые молули

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    fieldnames = [
        'longitude',
        'latitude',
        'housing_median_age',
        'total_rooms',
        'total_bedrooms',
        'population',
        'households',
        'median_income',
        'median_house_value'
    ]
    with open(INPUT_FILENAME, 'r') as f:
        next(f) # пропуск 1 строки
        reader = csv.DictReader(f, fieldnames=fieldnames)
        data = list(reader)

    with open(OUTPUT_FILENAME, 'w') as f:
        json.dump(data, f, indent=4)

    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
