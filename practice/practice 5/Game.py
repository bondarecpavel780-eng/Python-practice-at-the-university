import tkinter as tk
import random

# Основні налаштування вікна
root = tk.Tk()
root.title("Ловець яєць")
root.resizable(False, False)

# Налаштування полотна (Canvas)
canvas_width = 800
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="deep sky blue")
canvas.pack()

# Тло: зелена трава знизу
canvas.create_rectangle(0, 350, 800, 400, fill="forest green", outline="forest green")

# Змінні гри
score = 0
missed = 0
egg_speed = 5
egg_interval = 2000  # Час між появою нових яєць (в мілісекундах)
catcher_speed = 30
eggs = []

# Створення ловця (кошика)
catcher_width = 100
catcher_height = 20
catcher_start_x = 350
catcher_start_y = 330
catcher = canvas.create_rectangle(catcher_start_x, catcher_start_y,
                                  catcher_start_x + catcher_width,
                                  catcher_start_y + catcher_height,
                                  fill="dark blue", outline="black")

# Текст інтерфейсу (Рахунок та Пропущені)
score_text = canvas.create_text(60, 20, text=f"Рахунок: {score}", fill="white", font=("Arial", 14, "bold"))
missed_text = canvas.create_text(720, 20, text=f"Пропущено: {missed}/5", fill="white", font=("Arial", 14, "bold"))


# Функція створення нового яйця
def create_egg():
    if missed <= 5:
        # Випадкова позиція по осі X
        x = random.randint(30, 770)
        y = 0
        # Створення яйця
        egg = canvas.create_oval(x - 15, y, x + 15, y + 40, fill="white", outline="light gray")
        eggs.append(egg)
        # Плануємо появу наступного яйця
        root.after(egg_interval, create_egg)


# Функція руху яєць
def move_eggs():
    global missed, score, egg_speed

    for egg in eggs:
        canvas.move(egg, 0, egg_speed)
        egg_coords = canvas.coords(egg)

        # Перевірка, чи впало яйце повз кошик (досягло землі)
        if egg_coords[3] > 400:
            eggs.remove(egg)
            canvas.delete(egg)
            missed += 1
            canvas.itemconfig(missed_text, text=f"Пропущено: {missed}/5")

            # Якщо пропущено більше 5, гра закінчується
            if missed > 5:
                game_over()
                return

    # Перевірка на те, чи зловив кошик яйце
    check_catch()

    # Якщо гра триває, продовжуємо рух
    if missed <= 5:
        root.after(30, move_eggs)


# Перевірка зіткнення яйця та кошика
def check_catch():
    global score, egg_speed, egg_interval
    catcher_coords = canvas.coords(catcher)

    for egg in eggs:
        egg_coords = canvas.coords(egg)

        # Перевіряємо, чи перетинаються координати яйця та кошика
        if (egg_coords[2] > catcher_coords[0] and
                egg_coords[0] < catcher_coords[2] and
                egg_coords[3] > catcher_coords[1] and
                egg_coords[3] < catcher_coords[3]):

            eggs.remove(egg)
            canvas.delete(egg)
            score += 10
            canvas.itemconfig(score_text, text=f"Рахунок: {score}")

            # Трохи ускладнюємо гру з часом (збільшуємо швидкість)
            if score % 50 == 0:
                egg_speed += 1
                if egg_interval > 500:
                    egg_interval -= 200


# Функції руху кошика
def move_left(event):
    coords = canvas.coords(catcher)
    if coords[0] > 0:
        canvas.move(catcher, -catcher_speed, 0)


def move_right(event):
    coords = canvas.coords(catcher)
    if coords[2] < canvas_width:
        canvas.move(catcher, catcher_speed, 0)


# Функція завершення гри
def game_over():
    canvas.create_text(400, 180, text="ГРА ЗАКІНЧЕНА!", fill="red", font=("Arial", 40, "bold"))
    canvas.create_text(400, 230, text=f"Ваш фінальний рахунок: {score}", fill="yellow", font=("Arial", 20, "bold"))
    # Видаляємо всі яйця, що залишилися
    for egg in eggs:
        canvas.delete(egg)
    eggs.clear()


# Прив'язка клавіш до функцій руху
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# Запуск ігрових циклів
root.after(1000, create_egg)  # Перше яйце з'явиться через 1 секунду
root.after(30, move_eggs)  # Запуск циклу оновлення кадрів

# Головний цикл Tkinter
root.mainloop()