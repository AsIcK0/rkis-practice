class Student:
    def __init__(self,firstName,date_of_birth,groupNumber,performance):
        self.firstName = firstName
        self.date_of_birth = date_of_birth
        self.groupNumber = groupNumber
        self.performance = performance
    def change_surname(self, new_firstName):
        self.firstName = new_firstName
    def change_birth_date(self, new_birth_date):
        self.date_of_birth = new_birth_date
    def change_group_number(self,new_number):
        self.groupNumber = new_number
    def show_info(self):
        return f'Фамилия: {self.firstName}\nДата рождения: {self.date_of_birth}\nНомер группы: {self.groupNumber}\nУспеваемость: {self.performance}'
if __name__ == '__main__':
    students = [
        Student('Похавал', '01.01.2000','101', [5,4,4,2,5]),
        Student('Хавал', '15.03.2001', '102', [4, 4, 4, 4, 4])
    ]
def show_student_info():
    for student in students:
        print(student.show_info())
def search_student():
    student_search_firstName, student_search_birth_date = input(), input()
    for student in students:
        if student.firstName.lower() == student_search_firstName.lower() and student.date_of_birth.lower() == student_search_birth_date.lower():
            print(student.show_info())
            break
def change_student_info():
    studentnumber = int(input())
    students[studentnumber].change_surname(input('Фамилия: '))
    students[studentnumber].change_birth_date(input('Дата: '))
    students[studentnumber].change_group_number(input('Номер: '))
while True:
    print('\n1 - Вывод всей инфы\n2 - Поиск студента\n3 - Смена данных студента')
    a = str(input())
    if a == '1':
        show_student_info()
    elif a == '2':
        search_student()
    elif a == '3':
        change_student_info()