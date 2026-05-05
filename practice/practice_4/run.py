from FullTimeStudent import FullTimeStudent
from PartTimeStudent import PartTimeStudent

# Створення студентів
student1 = FullTimeStudent("KOLA", 24, 910, 10, 95, 85)
student2 = FullTimeStudent("Klavdia Petrivna", 19, 930, 10, 99, 20)
student3 = PartTimeStudent("CHEEV", 22, 390, 4, 78)
student4 = PartTimeStudent("YAKTAK", 21, 480, 5, 82)

# Список студентів
students = [student1, student2, student3, student4]

# Вивід результатів
for student in students:
    student.display_info()
    print(f"Загальний бал: {student.total_score()}")
    print("---------")