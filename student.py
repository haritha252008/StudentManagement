students = []

# Function to add a student
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Student Course: ")

    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)
    print("Student added successfully!")


# Function to display student details
def display_students():
    if not students:
        print("No student records found.")
    else:
        print("\n--- Student Details ---")

        for student in students:
            print("Student ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])


# Function to search for a student
def search_student():
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["ID"] == student_id:
            print("\nStudent Found!")
            print("Student ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            return

    print("Student not found.")


# Function to delete a student
def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")

