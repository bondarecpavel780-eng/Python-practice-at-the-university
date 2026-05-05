from Person import Person

class PartTimeStudent(Person):
    def __init__(self, name, age, prac_score, prac_count, exam_scr):
        super().__init__(name, age, prac_score, prac_count, exam_scr)

    def total_score(self):
        S_pr = self.avg_practice_score()
        S_ex = self.exam_scr
        return 0.7 * S_pr + 0.3 * S_ex

    def display_info(self):
        print("Форма навчання: заочна")
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age}")
        print(f"Середній бал за практичні: {self.avg_practice_score()}")