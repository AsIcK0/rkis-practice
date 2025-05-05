class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days
    def get_salary(self):
        return self.rate * self.days
if __name__ == "__main__":
    worker = Worker("Петро", "Грифель", 1230, 19)
    print(f"Работник: {worker.name} {worker.surname}")
    print(f"Зарплата: {worker.get_salary()} рублей")