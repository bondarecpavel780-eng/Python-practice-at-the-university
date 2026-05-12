def parse_students(row_generator):
    """Парсить рядки з генератора та повертає список студентів (словників)."""
    students = []
    for row in row_generator:
        parts = row.split(',')
        if len(parts) >= 5:
            student = {
                'name': parts[0],
                'group': parts[1],
                'grades': [int(x) for x in parts[2:]] # Зберігаємо як list[int]
            }
            students.append(student)
    return students