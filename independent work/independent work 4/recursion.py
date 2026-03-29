def print_employees_recursive(names_list, index=0):
    if index >= len(names_list):
        return

    print(names_list[index])
    print_employees_recursive(names_list, index + 1)