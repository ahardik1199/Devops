# student_grades.py

def add_student(grades: dict, name: str, grade: str) -> bool:
    """
    Add a new student with grade.
    Returns True if added, False if student already exists.
    """
    name = name.strip()
    grade = grade.strip().upper()
    if name in grades:
        return False
    grades[name] = grade
    return True

def update_grade(grades: dict, name: str, new_grade: str) -> bool:
    """
    Update an existing student's grade.
    Returns True if updated, False if student not found.
    """
    name = name.strip()
    new_grade = new_grade.strip().upper()
    if name not in grades:
        return False
    grades[name] = new_grade
    return True

def get_all_grades(grades: dict) -> dict:
    """
    Return a copy of all student grades.
    """
    return dict(grades)

def main():
    grades = {}
    while True:
        print("\nStudent Grades Manager")
        print("1. Add new student and grade")
        print("2. Update existing student's grade")
        print("3. Print all student grades")
        print("4. Exit")
        choice = input("Select an option (1–4): ").strip()

        if choice == "1":
            name = input("Enter student name: ")
            grade = input(f"Enter grade for {name}: ")
            if add_student(grades, name, grade):
                print(f"Added: {name.strip()} → {grades[name.strip()]}")
            else:
                print(f"Student '{name.strip()}' already exists with grade {grades[name.strip()]}.")

        elif choice == "2":
            name = input("Enter student name to update: ")
            new_grade = input(f"Enter new grade for {name.strip()}: ")
            if update_grade(grades, name, new_grade):
                print(f"Updated: {name.strip()} → {grades[name.strip()]}")
            else:
                print(f"No record found for student '{name.strip()}'.")

        elif choice == "3":
            if not grades:
                print("No student records to display.")
            else:
                print("\nAll Student Grades:")
                for student, grade in grades.items():
                    print(f"- {student}: {grade}")

        elif choice == "4":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid option, please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
