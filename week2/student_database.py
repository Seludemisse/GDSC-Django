students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    
    student = {
        'name': name,
        'age': age,
        'grade': grade
    }
    
    students.append(student)
    print("Student added successfully!")

def view_student():
    name = input("Enter student name to view detail: ")
    
    for student in students:
        if student['name'] == name:
            print("Student Details:")
            print("Name:", student['name'])
            print("Age:", student['age'])
            print("Grade:", student['grade'])
            return
    
    print("Student not found!")

def list_all_students():
    print("List of Students:")
    for student in students:
        print("Name:", student['name'])
        print("Age:", student['age'])
        print("Grade:", student['grade'])
        print()

def update_student_information():
    name = input("Enter student name to update information: ")
    if name in students:
        age = int(input("Enter new age: "))
        grade = input("Enter new grade: ")

        students[name]['Age'] = age
        students[name]['Grade'] = grade
        print(f"Information for {name} updated.")
    else:
        print(f"Student {name} not found in the database.")
def delete_student():
    name = input("Enter student's name: ")
    
    for student in students:
        if student['name'] == name:
            students.remove(student)
            print("Student deleted successfully!")
            return
    
    print("Student not found!")

def main():
 while True:
    print()
    print("Student Database Menu:")
    print("1. Add Student")
    print("2. View Student")
    print("3. List All Students")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        list_all_students()
    elif choice == '4':
        update_student_information()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting the program...")
        break
    else:
        print("YOu input invalid choice. Please try again.")
        
if __name__ == "__main__" :
  main()