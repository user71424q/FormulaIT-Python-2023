import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    """Функция читает CSV файл, разбивает его на отдельные столбцы и создает
    для каждой записи словарь в формате JSON, где ключами будут названия столбцов, а значениями -
    соответствующие значения в этой строке
    :return: None"""
    with open(INPUT_FILENAME) as f:
        lines = [line for line in csv.DictReader(f)]
        with open(OUTPUT_FILENAME, 'w') as f:
            json.dump(lines, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
