#Student_Data_Organiser


students = []

def add_student():
    print("\n---------Add Student-----------")

    
    student_id = int(input("Enter Student ID:"))
    name = input("Enter Your Name:")
    age = int(input("Enter Your Age:"))
    grade = input("Enter Your grade:")
    dob = input("Enter Your Date of Birth(DD-MM-YYYY):")

    student_fixed = (student_id, dob)

    subject_input = input("Enter Subjects separated by commas:")
    subjects = set()
    
    for subject in subject_input.split(","):
        subjects.add(subject.strip())
        
    student = {
        
        "id_dob": student_fixed,
        "Name": name,
        "Age": age,
        "Grade": grade,
        "Subjects": subjects
        }
    
    
    students.append(student)
    print("\nStudent added succesfully!")

def display_student():
    print("\n------------All Students-----------")
    if len(students) == 0:
        print("No students found.")
        return
        
    for student in students:
        print("\nStudent ID:", student["id_dob"][0])
        print("Date of Birth:",student["id_dob"][1])
        print("Name:",student["Name"])
        print("Age:", student["Age"])
        print("Grade:",student["Grade"])
        print("Subjects:",student["Subjects"])
        print("-----------------------------")
            
def update_student():
    print("\n------Update Student--------_")
    student_id = int(input("Enter Student ID to Update:"))
    for student in students:
        if student["id_dob"][0] == student_id:
            print("Student found!")
            new_age = int(input("Enter new age:"))
            new_subject_input = input("Enter new subjects separated by commas:")
            new_subjects = set()
            for subject in new_subject_input.split(","):
                new_subjects.add(subject.strip())
            student["Age"] = new_age
            student["Subjects"] = new_subjects
            print("Student updated successfully!")


def delete_student():
    print("\n--------- Delete Student-----------")
    student_id = int(input("Enter Student ID to delete:"))
    for index in range(len(students)):
        if students[index]["id_dob"][0] == student_id:
            del students[index]
            print("Student deleted successfully!")
            return
    print("Student ID not found.")

    
def display_subjects():
    print("\n----------Subjects Offered-----------")
    all_subjects = set()
    for student in students:
        all_subjects.update(student["Subjects"])
    if len(all_subjects) == 0:
       print("No subjects found.")
       return
    for subject in sorted(all_subjects):
        print(subject)

print("=======================================================")
print("      Wlecome to Student Data Organizer")
print("========================================================")

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    choice = input("Enter Your Choice:")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_subjects()
    elif choice =="6":
        print("\nThank you for using Student Data Organizer!")
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
            
    
    
