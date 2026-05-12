import json
from cli.args import parse_arguments
from reader.file_reader import read_csv_generator
from parser.student_parser import parse_students
from analysis.statistics import calculate_averages
from analysis.containers import build_containers
from reporting.charts import plot_group_averages, plot_subject_distribution


def main():
    args = parse_arguments()

    try:
        # 1. Ітеративне зчитування даних
        row_gen = read_csv_generator(args.file)

        # 2. Парсинг у структури
        students = parse_students(row_gen)
    except FileNotFoundError:
        print(f"Помилка: Файл {args.file} не знайдено.")
        return

    # Застосування фільтру по групі, якщо вказано через аргумент --group
    if args.group:
        students = [s for s in students if s['group'] == args.group]

    if not students:
        print("Не знайдено студентів за заданими критеріями.")
        return

    # 3. Обчислення статистик
    group_averages, above_average = calculate_averages(students)

    # 4. Робота з асоціативними контейнерами
    group_dict, excellent_groups = build_containers(students)

    # Вивід результатів у консоль
    print("\n--- Аналітика успішності ---")
    print(f"Середні бали по групах: {group_averages}")
    print(f"Студенти з балом вище середнього по групі: {above_average}")
    print(f"Склад груп: {group_dict}")
    print(f"Групи з відмінниками (усі оцінки >=90): {list(excellent_groups)}")

    # Експорт у JSON, якщо вказано аргумент --export
    if args.export:
        export_data = {
            "group_averages": group_averages,
            "above_average": above_average,
            "group_dict": group_dict,
            "excellent_groups": list(excellent_groups)
        }
        with open(args.export, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, ensure_ascii=False, indent=4)
        print(f"\n✅ Результати експортовано у файл: {args.export}")

    # 5. Графічна візуалізація
    plot_group_averages(group_averages)
    plot_subject_distribution(students)


if __name__ == "__main__":
    main()