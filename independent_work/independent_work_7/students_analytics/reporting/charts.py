import matplotlib.pyplot as plt
import numpy as np

from practice import students


def plot_group_averages(group_averages):
    """Будує стовпчикову діаграму середнього балу по групах."""
    groups = list(group_averages.keys())
    averages = list(group_averages.values())

    plt.figure(figsize=(8, 5))
    plt.bar(groups, averages, color='skyblue')
    plt.title('Середній бал по групах')
    plt.xlabel('Група')
    plt.ylabel('Середній бал')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def plot_subject_distribution(students):
    """Будує boxplot розподілу оцінок по предметах."""
    # Конвертуємо всі оцінки в 2D numpy масив (Nx3)
    all_grades = np.array([s['grades'] for s in students])

    if all_grades.size == 0:
        return

    plt.figure(figsize=(8, 5))
    # Кожна колонка — це окремий предмет: Math, Physics, Python
    plt.boxplot([all_grades[:, 0], all_grades[:, 1], all_grades[:, 2]],
                tick_labels=['Math', 'Physics', 'Python'])
    plt.title('Розподіл оцінок по предметах')
    plt.ylabel('Оцінки')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


