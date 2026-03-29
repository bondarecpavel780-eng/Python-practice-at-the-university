from Person import Person

class FullTimeStudent(Person):
    def __init__(self, name, age, prac_score, prac_count, exam_scr, attend_pct):
        super().__init__(name, age, prac_score, prac_count, exam_scr)
        self.attend_pct = attend_pct

    def total_score(self):
        S_pr = self.avg_practice_score()
        S_ex = self.exam_scr
        S_att = self.attend_pct
        return 0.6 * S_pr + 0.3 * S_ex + 0.1 * S_att

    def display_info(self):
        print("Форма навчання: очна")
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age}")
        print(f"Середній бал за практичні: {self.avg_practice_score()}")