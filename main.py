import os

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")


students = []


# 🔹 Load data from file
def load_students():
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as file:
            for line in file:
                name, roll = line.strip().split(",")
                students.append(Student(name, roll))


# 🔹 Save student to file
def save_student(name, roll):
    with open("students.txt", "a") as file:
        file.write(f"{name},{roll}\n")


def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll no: ")

    students.append(Student(name, roll))
    save_student(name, roll)

    print("Student added & saved!\n")


def view_students():
    if not students:
        print("No students found.\n")
        return

    print("\n--- Student List ---")
    for s in students:
        s.display()
    print()


def search_student():
    roll = input("Enter roll to search: ")

    for s in students:
        if s.roll == roll:
            print("Student found:")
            s.display()
            return

    print("Student not found.\n")


def delete_student():
    roll = input("Enter roll to delete: ")

    for s in students:
        if s.roll == roll:
            students.remove(s)

            # rewrite file after deletion
            with open("students.txt", "w") as file:
                for stu in students:
                    file.write(f"{stu.name},{stu.roll}\n")

            print("Student deleted.\n")
            return

    print("Student not found.\n")


def main():
    load_students()  # 🔥 load on start

    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice\n")


main() 
