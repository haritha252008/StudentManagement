# Import student module
import student

# Welcome message
print("\nWelcome to Student Management System")

# Menu-driven program
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")
    print("5. Delete Student")

    choice = input("Enter your choice: ")

    if choice == "1":
        student.add_student()

    elif choice == "2":
        student.display_students()

    elif choice == "3":
        student.search_student()

    elif choice == "4":
        print("Thank you for using Student Management System!")
        break

    elif choice == "5":
        student.delete_student()

    else:
        print("Invalid choice! Please try again.")

