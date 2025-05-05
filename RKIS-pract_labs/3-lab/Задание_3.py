class Calculation:
    def __init__(self):
        self.calculationLine = ""
    def SetCalculationLine(self, value):
        self.calculationLine = value
    def SetLastSymbolCalculationLine(self, symbol):
        self.calculationLine += symbol
    def GetCalculationLine(self):
        return self.calculationLine
    def GetLastSymbol(self):
        if self.calculationLine:
            return self.calculationLine[-1]
        return ""
    def DeleteLastSymbol(self):
        if self.calculationLine:
            self.calculationLine = self.calculationLine[:-1]
if __name__ == "__main__":
    calc = Calculation()
    calc.SetCalculationLine("123")
    print("Текущая строка:", calc.GetCalculationLine())
    calc.SetLastSymbolCalculationLine("+")
    print("После добавления символа:", calc.GetCalculationLine())
    print("Последний символ:", calc.GetLastSymbol())
    calc.DeleteLastSymbol()
    print("После удаления последнего символа:", calc.GetCalculationLine())
    calc.SetLastSymbolCalculationLine("*")
    print("После добавления нового символа:", calc.GetCalculationLine())