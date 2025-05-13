import sqlite3
from dataclasses import dataclass
@dataclass
class Student:
    id: int
    first_name: str
    last_name: str
    middle_name: str
    group: str
    grades: list
class StudentDatabase:
    def __init__(self, db_name='students.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    def create_table(self):

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                middle_name TEXT,
                group_name TEXT NOT NULL,
                grade1 INTEGER NOT NULL,
                grade2 INTEGER NOT NULL,
                grade3 INTEGER NOT NULL,
                grade4 INTEGER NOT NULL
            )
        ''')
        self.conn.commit()
    def add_student(self, student):
        self.cursor.execute('''
            INSERT INTO students (first_name, last_name, middle_name, group_name, grade1, grade2, grade3, grade4)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            student.first_name,
            student.last_name,
            student.middle_name,
            student.group,
            *student.grades
        ))
        self.conn.commit()
        return self.cursor.lastrowid
    def get_all_students(self):
        self.cursor.execute('SELECT * FROM students')
        rows = self.cursor.fetchall()
        return [self.row_to_student(row) for row in rows]
    def get_student(self, student_id):
        self.cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
        row = self.cursor.fetchone()
        if row:
            return self.row_to_student(row)
        return None
    def update_student(self, student):
        self.cursor.execute('''
            UPDATE students
            SET first_name = ?, last_name = ?, middle_name = ?, group_name = ?,
                grade1 = ?, grade2 = ?, grade3 = ?, grade4 = ?
            WHERE id = ?
        ''', (
            student.first_name,
            student.last_name,
            student.middle_name,
            student.group,
            *student.grades,
            student.id
        ))
        self.conn.commit()
    def delete_student(self, student_id):
        self.cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        self.conn.commit()
    def get_group_average(self, group_name):
        self.cursor.execute('''
            SELECT 
                AVG((grade1 + grade2 + grade3 + grade4) / 4.0) as avg_grade
            FROM students
            WHERE group_name = ?
        ''', (group_name,))
        result = self.cursor.fetchone()
        return result[0] if result and result[0] is not None else 0.0
    def row_to_student(self, row):
        return Student(
            id=row[0],
            first_name=row[1],
            last_name=row[2],
            middle_name=row[3],
            group=row[4],
            grades=[row[5], row[6], row[7], row[8]]
        )
    def close(self):
        self.conn.close()
def print_student(student):
    avg_grade = sum(student.grades) / len(student.grades)
    print(f"ID: {student.id}")
    print(f"ФИО: {student.last_name} {student.first_name} {student.middle_name}")
    print(f"Группа: {student.group}")
    print(f"Оценки: {', '.join(map(str, student.grades))}")
    print(f"Средний балл: {avg_grade:.2f}")
    print("-" * 30)
def main():
    db = StudentDatabase()
    while True:
        print("\nМеню:")
        print("1. Добавить нового студента")
        print("2. Просмотреть всех студентов")
        print("3. Просмотреть одного студента")
        print("4. Редактировать студента")
        print("5. Удалить студента")
        print("6. Просмотреть средний балл группы")
        print("0. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("\nДобавление нового студента:")
            first_name = input("Имя: ")
            last_name = input("Фамилия: ")
            middle_name = input("Отчество: ")
            group = input("Группа: ")
            grades = []
            for i in range(4):
                grade = int(input(f"Оценка {i + 1}: "))
                grades.append(grade)
            student = Student(
                id=0,
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                group=group,
                grades=grades
            )
            db.add_student(student)
            print("Студент успешно добавлен!")
        elif choice == "2":
            print("\nСписок всех студентов:")
            students = db.get_all_students()
            for student in students:
                print_student(student)
        elif choice == "3":
            student_id = int(input("Введите ID студента: "))
            student = db.get_student(student_id)
            if student:
                print("\nИнформация о студенте:")
                print_student(student)
            else:
                print("Студент не найден!")
        elif choice == "4":
            student_id = int(input("Введите ID студента для редактирования: "))
            student = db.get_student(student_id)
            if student:
                print("\nТекущие данные студента:")
                print_student(student)
                print("Введите новые данные (оставьте пустым, чтобы не изменять):")
                first_name = input(f"Имя [{student.first_name}]: ") or student.first_name
                last_name = input(f"Фамилия [{student.last_name}]: ") or student.last_name
                middle_name = input(f"Отчество [{student.middle_name}]: ") or student.middle_name
                group = input(f"Группа [{student.group}]: ") or student.group
                grades = []
                for i in range(4):
                    grade = input(f"Оценка {i + 1} [{student.grades[i]}]: ")
                    grades.append(int(grade) if grade else student.grades[i])
                updated_student = Student(
                    id=student.id,
                    first_name=first_name,
                    last_name=last_name,
                    middle_name=middle_name,
                    group=group,
                    grades=grades
                )
                db.update_student(updated_student)
                print("Данные студента обновлены!")
            else:
                print("Студент не найден!")
        elif choice == "5":
            student_id = int(input("Введите ID студента для удаления: "))
            student = db.get_student(student_id)
            if student:
                db.delete_student(student_id)
                print("Студент удален!")
            else:
                print("Студент не найден!")
        elif choice == "6":
            group = input("Введите название группы: ")
            avg = db.get_group_average(group)
            print(f"\nСредний балл группы {group}: {avg:.2f}")
        elif choice == "0":
            db.close()
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
if __name__ == "__main__":
    main()