class Train:
    def __init__(self, destination, train_number, departure_time):
        self.destination = destination
        self.train_number = train_number
        self.departure_time = departure_time
    def show_info(self):
        print(f"\nИнформация о поезде:")
        print(f"Номер поезда: {self.train_number}")
        print(f"Пункт назначения: {self.destination}")
        print(f"Время отправления: {self.departure_time}")
if __name__ == "__main__":
    trains = [
        Train("Москва", "101", "18:20"),
        Train("Санкт-Петербург", "102", "20:31")
    ]
    while True:
        print("\nПоиск информации о поезде")
        train_number = input("Введите номер поезда (или '0' для выхода): ")

        if train_number == '0':
            break
        for train in trains:
            if train.train_number == train_number:
                train.show_info()
                break