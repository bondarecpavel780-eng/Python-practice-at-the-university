def calculate_salary(employee_data):
    salary = employee_data["salary"]
    days = employee_data["days"]

    return (salary / 30) * days


def calculate_all_salaries(employees):
    results = {}

    for name, data in employees.items():
        results[name] = calculate_salary(data)

    return results