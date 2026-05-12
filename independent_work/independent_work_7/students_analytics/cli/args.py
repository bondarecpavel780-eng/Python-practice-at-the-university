import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Аналітика успішності студентів")
    parser.add_argument("--file", default="data/grades.csv", help="Шлях до файлу CSV")
    parser.add_argument("--group", help="Фільтр по групі (наприклад, KN-21)")
    parser.add_argument("--export", help="Шлях для збереження результатів у JSON (наприклад, OUT.json)")
    return parser.parse_args()