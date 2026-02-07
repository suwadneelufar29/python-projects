# Student Management System (Console-Based)

students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    students[roll] = {"Name": name, "Marks": marks}
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
    else:
        for roll, details in students.items():
            print(f"Roll: {roll}, Name: {details['Name']}, Marks: {details['Marks']}")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
