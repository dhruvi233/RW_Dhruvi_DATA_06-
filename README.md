# Fundamental Booster - Personal Data Collector
## Project Description
This project is a simple interactive Personal Data Collector created using Python.
The program collects basic information from the user such as:
-Name
-Age
-Height
-Favourite Number
It processes the collected information, calculate the user's approximate birth year, and displays birth year, and displays the data type and memory address of each variable.
## Python Concepts Used
-print() function
-input() function
-Variables
-Data Types
-Type casting
-Arithmetic Operators
- type() function
- id() function
- ## Features
- Interactive user input
- Basic data processing
- Approximate birth-year calculation
- Data type identification
- Memory address display
- User-Friendly final summary

  ## Author
  Dhruvi Das
***

#  Student Data Organizer

The **Student Data Organizer** is a Python-based, menu-driven console application created to store and manage student information.

The program allows the user to add student records, display all students, update student information, delete a student using the Student ID, and display all unique subjects offered.

This project demonstrates important Python programming concepts such as **lists, dictionaries, tuples, sets, string manipulation, type casting, mutability and immutability, functions, loops, conditional statements, the `del` keyword, and a menu-driven interface.**

***

##  Project Video Demonstration

Watch my complete Student Data Organizer project explanation and live demonstration here:

Project 3 video](https://drive.google.com/file/d/1AGDq2pEKLmtxGQ0WI0GmvnSmR7jzv34p/view?usp=sharing)

***

##  Objectives

- Create a menu-driven Python application.
- Store and manage multiple student records.
- Demonstrate the use of Python lists.
- Demonstrate dictionaries for storing student information.
- Demonstrate tuples for storing fixed student information.
- Demonstrate sets for storing unique subjects.
- Practice string manipulation using `split()` and `strip()`.
- Practice type casting using `int()`.
- Understand mutable and immutable data structures.
- Use functions to organize the program.
- Use loops and conditional statements.
- Use the `del` keyword to delete student records.
- Display unique subjects offered by all students.

***

##  Features

###  1. Add Student

The program allows the user to enter:

- Student ID
- Student Name
- Age
- Grade
- Date of Birth
- Subjects

The Student ID and Date of Birth are stored together in a tuple.

The student information is then stored in a dictionary.

The dictionary is added to the main `students` list.

Subjects are stored in a set so that duplicate subjects are not stored.

***

###  2. Display All Students

The program displays all stored student records.

For each student, it displays:

- Student ID
- Date of Birth
- Name
- Age
- Grade
- Subjects

If no students have been added, the program displays:

```text
No students found.
```

***

###  3. Update Student Information

The user can enter a Student ID to find a particular student.

If the Student ID is found, the program allows the user to update:

- Age
- Subjects

The updated age and subjects replace the previous values.

The program then displays:

```text
Student updated successfully!
```

***

###  4. Delete Student

The user can enter a Student ID to delete a student.

The program searches through the student list and checks the Student ID.

When the matching student is found, the program uses the `del` keyword to remove that student record from the list.

Example:

```python
del students[index]
```

After deletion, the program displays:

```text
Student deleted successfully!
```

If the Student ID is not found, the program displays:

```text
Student ID not found.
```

***

###  5. Display Subjects Offered

The program collects subjects from all students.

A set named `all_subjects` is used to store the subjects without duplicates.

Example:

```python
all_subjects = set()
```

The subjects are collected from every student record and then displayed in sorted order.

This feature demonstrates the use of **sets, loops, and the `sorted()` function**.

***

###  6. Exit Program

The user can select option `6` to exit the program.

The program displays:

```text
Thank you for using Student Data Organizer!
Goodbye!
```

***

##  Python Concepts Used

###  Lists

A list is used to store multiple student records.

Example:

```python
students = []
```

Each student dictionary is added to the list using:

```python
students.append(student)
```

Lists are mutable, meaning their contents can be changed after creation.

***

###  Dictionaries

A dictionary is used to store information about each student using key-value pairs.

Example:

```python
student = {
    "id_dob": student_fixed,
    "Name": name,
    "Age": age,
    "Grade": grade,
    "Subjects": subjects
}
```

The dictionary allows different pieces of information about a student to be stored together.

***

###  Tuples

A tuple is used to store the Student ID and Date of Birth together.

Example:

```python
student_fixed = (student_id, dob)
```

The tuple demonstrates an immutable data structure.

***

###  Sets

Sets are used for storing unique subjects.

Example:

```python
subjects = set()
```

Sets automatically avoid duplicate values.

The program also creates another set to collect all subjects offered by the students:

```python
all_subjects = set()
```

***

###  String Manipulation

The project uses `split()` and `strip()` to process subjects entered by the user.

Example:

```python
for subject in subject_input.split(","):
    subjects.add(subject.strip())
```

Here:

- `split(",")` separates the subjects using commas.
- `strip()` removes unnecessary spaces around each subject.

***

###  Type Casting

The program uses `int()` to convert user input into integers.

Example:

```python
student_id = int(input("Enter Student ID:"))
age = int(input("Enter Your Age:"))
```

This allows numeric input to be used for comparisons and other operations.

***

###  Mutability and Immutability

The project demonstrates different Python data structures.

**Mutable data structures:**

- Lists
- Dictionaries
- Sets

**Immutable data structures:**

- Tuples
- Strings

Mutable objects can be modified after creation, while immutable objects cannot be changed directly.

***

### `del` Keyword

The `del` keyword is used to remove a student record from the list.

Example:

```python
del students[index]
```

This removes the selected student from the current list.

***

##  Loops and Conditional Statements

The program uses loops and conditional statements throughout the application.

### `while` Loop

The main menu uses:

```python
while True:
```

This keeps the menu running until the user selects the Exit option.

### `for` Loop

`for` loops are used to:

- Search student records.
- Process subjects.
- Display student information.
- Collect subjects from all students.

### Conditional Statements

The program uses:

- `if`
- `elif`
- `else`

to process menu choices and check different conditions.

***

##  Functions Used

The program is divided into different user-defined functions to keep the code organized.

### `add_student()`

Takes student details from the user and creates a new student record.

### `display_student()`

Displays all stored student records.

### `update_student()`

Searches for a student using the Student ID and updates the student's age and subjects.

### `delete_student()`

Searches for a student using the Student ID and deletes the matching record.

### `display_subjects()`

Collects subjects from all students and displays the unique subjects in sorted order.

***

##  Menu-Driven Interface

The program provides a menu-driven interface with the following options:

```text
=======================================================
      Welcome to Student Data Organizer
=======================================================

Select an option:

1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
```

The user selects an option by entering the corresponding number.

The `while` loop keeps displaying the menu until option `6` is selected.

***

##  How to Run the Program

1. Open Python or IDLE.
2. Open the Python file:

```text
Student_Data_Organiser.py
```

3. Run the program.
4. The main menu will appear.
5. Enter the number of the required option.
6. Follow the instructions displayed by the program.
7. Select option `6` when you want to exit.

***

##  Program Structure

```text
Student_Data_Organiser/
│
├── Student_Data_Organiser.py
└── README.md
```

The `Student_Data_Organiser.py` file contains the complete Python program.

The `README.md` file contains the project description, objectives, features, concepts, instructions, and other project information.

***

##  Sample Workflow

A typical demonstration of the program can follow this sequence:

### Step 1 – Add Student

Select:

```text
1. Add Student
```

Enter the student's:

- ID
- Name
- Age
- Grade
- Date of Birth
- Subjects

The program stores the student record.

### Step 2 – Display Student

Select:

```text
2. Display All Students
```

The program displays the stored student information.

### Step 3 – Delete Student

Select:

```text
4. Delete Student
```

Enter the Student ID.

The program removes the matching student record.

### Step 4 – Display Students Again

Select:

```text
2. Display All Students
```

The program displays the updated student list after deletion.

### Step 5 – Exit

Select:

```text
6. Exit
```

The program displays the goodbye message and terminates.

***

##  Input Handling and Conditions

The program includes basic conditions for different situations.

These include:

- Checking whether the student list is empty.
- Checking whether a Student ID matches an existing student.
- Checking whether subjects are available.
- Checking the selected menu option.
- Converting Student ID and Age into integers using `int()`.

For example, if there are no students:

```text
No students found.
```

If there are no subjects:

```text
No subjects found.
```

If a Student ID does not exist during deletion:

```text
Student ID not found.
```

***

##  Assumptions

- Student ID is entered as an integer.
- Age is entered as an integer.
- Subjects are entered separated by commas.
- Date of Birth is entered in `DD-MM-YYYY` format.
- The program stores data only while the program is running.
- Student records are not permanently stored in a database or file.
- The user follows the input format requested by the program.

***

## 👩‍💻 Author

**Dhruvi Das**

This project was created as part of my Python programming learning and practice.

