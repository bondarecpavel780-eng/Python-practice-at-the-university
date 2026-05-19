def write_numbers_to_file(filename, numbers_list):
    try:
        # Відкриваємо файл у режимі запису
        with open(filename, 'w', encoding='utf-8') as file:
            for number in numbers_list:
                # Записуємо кожне число з нового рядка
                file.write(f"{number}\n")
        print(f"Дані успішно записано у файл '{filename}'.")
    except Exception as e:
        print(f"Сталася помилка: {e}")


# Список, що містить цілі та дійсні числа
my_numbers = [10, 3.14, -5, 42.0, 0, 2.71828]

# Ім'я файлу, у який будуть записані дані
file_name = "numbers_output.txt"

write_numbers_to_file(file_name, my_numbers)