import json
import csv

def print_table(stats: dict):
    print("+---------------------------+--------+")
    print("| Показник                  |Значення|")
    print("+---------------------------+--------+")
    for key, value in stats.items():
        print(f"| {key:<25} | {value:>6} |")
    print("+---------------------------+--------+")

def export_to_json(data: dict, filepath: str):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"\n[+] Збережено у {filepath}")

def export_to_csv(data: dict, filepath: str):
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Показник", "Значення"])
        for key, value in data.items():
            writer.writerow([key, value])
    print(f"\n[+] Збережено у {filepath}")