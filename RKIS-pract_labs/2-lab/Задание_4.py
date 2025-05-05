class Counter:
    def __init__(self, initial_value=0):
        self._value = initial_value
    def increse(self):
        self._value += 1
    def decrese(self):
        self._value -= 1
    @property
    def value(self):
        return self._value
if __name__ == "__main__":
    counter1 = Counter()
    print("Счетчик 1:",counter1.value)
    counter1.increse()
    print("После увеличения:", counter1.value)
    counter1.decrese()
    print("После уменьшения:", counter1.value)
    counter2 = Counter(8)
    print("\nСчетчик 2:", counter2.value)
    counter2.increse()
    counter2.increse()
    print("После двух увеличений:", counter2.value)
    counter2.decrese()
    print("После уменьшения:", counter2.value)