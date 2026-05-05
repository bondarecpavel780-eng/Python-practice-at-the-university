def input_employees():
    employees = {}

    n = int(input("Скільки співробітників? "))

    for i in range(n):
        name = input("Ім'я співробітника: ")
        salary = float(input("Зарплата (за місяць): "))
        days = int(input("Відпрацьовані дні: "))

        employees[name] = {
            "salary": salary,
            "days": days
        }

    return employees
