import json


def task() -> float:
    file_path = "./input.json"
    with open(file_path) as f:
        data = json.load(f)
    total_score = sum(item['weight'] * item['score'] for item in data)
    return round(total_score, 3)


print(task())
