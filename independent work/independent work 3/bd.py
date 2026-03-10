def get_books():
    books = {}

    while True:
        try:
            n = int(input("Введіть кількість книг: "))
            if n <= 0:
                print("Книги не введено")
                return {}
            break
        except ValueError:
            print("Помилка. Введіть число.")

    for i in range(n):
        title = input("Назва книги: ")
        author = input("Автор: ")

        while True:
            try:
                pages = int(input("Кількість сторінок: "))
                break
            except ValueError:
                print("Помилка. Введіть число сторінок.")

        books[title] = (author, pages)

    return books


def average_pages(books):
    total = 0
    for book in books:
        total += books[book][1]
    return total / len(books)


def books_less_than_average(books, avg):
    result = []
    for title in books:
        if books[title][1] < avg:
            result.append(title)
    return result


books = get_books()

if books:
    avg = average_pages(books)
    print("Середня кількість сторінок:", avg)

    res = books_less_than_average(books, avg)

    if res:
        print("Книги з меншою кількістю сторінок за середнє:")
        for b in res:
            print(b)
    else:
        print("Таких книг немає")

print(books)