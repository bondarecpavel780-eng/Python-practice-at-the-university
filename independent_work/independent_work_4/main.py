from input import input_employees
from salary import calculate_all_salaries
from recursion import print_employees_recursive
from test import input1

employees = input_employees()

print("\nСписок співробітників:")
names = list(employees.keys())
print_employees_recursive(names)

print("\nЗарплати співробітників:")
salaries = calculate_all_salaries(employees)

for name, salary in salaries.items():
    print(f"{name}: {salary:.2f} грн")

num = input1()