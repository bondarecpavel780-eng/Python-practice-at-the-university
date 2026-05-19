def read_csv_generator(filepath):
    """Генератор для построкового читання CSV-файлу, пропускаючи заголовок."""
    with open(filepath, 'r', encoding='utf-8') as f:
        next(f)  # Пропускаємо заголовок
        for line in f:
            stripped_line = line.strip() #видаляє всі пробіли, зайві символм
            if stripped_line:
                yield stripped_line #видає по одному рядку