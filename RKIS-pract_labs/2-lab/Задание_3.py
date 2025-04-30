class Numbers:
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2
    def display(self):
        print(f"Первое число: {self.num1}")
        print(f"Второе число: {self.num2}")
    def change_numbers(self, new_num1: int, new_num2: int):
        self.num1 = new_num1
        self.num2 = new_num2
    def getsum(self) -> int:
        return self.num1 + self.num2
    def getmaximum(self) -> int:
        return max(self.num1, self.num2)
if __name__ == "__main__":
    numbers = Numbers(10, 5)
    numbers.display()
    print("\nСумма чисел:", numbers.getsum())
    print("Наибольшее число:", numbers.getmaximum())
    numbers.change_numbers(20, 30)
    print("\nПосле смены чисел:")
    numbers.display()