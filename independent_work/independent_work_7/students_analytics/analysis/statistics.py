import numpy as np


def calculate_averages(students):
    """Обчислює середні бали за допомогою numpy."""
    # Середній бал для кожного студента
    for student in students:
        grades_array = np.array(student['grades'])
        student['average'] = float(np.mean(grades_array))

    group_averages = {}
    groups = set(s['group'] for s in students)

    # Середній бал по групі
    for g in groups:
        g_grades = np.array([s['average'] for s in students if s['group'] == g])
        group_averages[g] = float(np.mean(g_grades))

    # Список студентів з успішністю вище за середнє по групі
    above_average = [
        s['name'] for s in students
        if s['average'] > group_averages[s['group']]
    ]

    return group_averages, above_average