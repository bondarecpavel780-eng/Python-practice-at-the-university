def get_student_data():
    students = {}

    while True:
        try:
            num_students = int(input("Введіть кількість студентів: "))
            if num_students <= 0:
                print("Кількість має бути більше 0")
            else:
                break
        except ValueError:
            print("Error")

    for i in range(num_students):

        while True:
            name = input("\nВведіть ім'я студента: ").strip()
            if name:
                break
            else:
                print("Ім'я не може бути порожнім!")

        while True:
            try:
                scores = list(map(int, input(f"Введіть оцінки {name}: ").strip().split()))

                if not scores:
                    print("Оцінки не можуть бути порожніми!")
                elif any(score < 0 or score > 100 for score in scores):
                    print("Оцінки мають бути в межах 0-100")
                else:
                    students[name] = scores
                    break

            except ValueError:
                print("Error")

    return students

students_data = get_student_data()
print(students_data)

def calculate_average(grades_dict):
    total_sum = 0
    total_count = 0
    for scores in grades_dict.values():
        total_sum += sum(scores)
        total_count += len(scores)
    if total_count == 0:
        return 0
    return total_sum / total_count


print(calculate_average(students_data))

def find_students_below_average(grades_dict, avg):
    below_average_students = {}
    for student, scores in grades_dict.items():
        student_average = sum(scores) / len(scores)
        if student_average < avg:
            below_average_students[student] = student_average

    return below_average_students
print(find_students_below_average(students_data, calculate_average(students_data)))
