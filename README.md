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

##  Author

**Dhruvi Das**

This project was created as part of my Python programming learning and practice.

***

#  Functional Treat – Data Analyzer and Transformer

The **Functional Treat – Data Analyzer and Transformer** is a Python-based, menu-driven console application designed to analyze and transform numerical data using 1D and 2D lists.

This project demonstrates important Python programming concepts including **built-in functions, user-defined functions, recursion, lambda functions, `map()`, `filter()`, `*args`, `**kwargs`, `__doc__`, global variables, multiple return values, list sorting, and 2D lists.**

The program provides a menu-driven interface where the user can enter data, calculate statistics, find duplicate and unique values, filter and transform data, sort lists, calculate factorials, demonstrate function arguments, display function documentation, and work with 2D lists.

***

##  Project Video Demonstration

Watch my complete Data Analyzer and Transformer project explanation and live demonstration here:

Project 4 video(https://drive.google.com/file/d/13jBunhts7HmDpawKKjjVW6Y7adMP53Jz/view?usp=sharing)

***

##  Objectives

- Create a menu-driven Python application.
- Work with 1D and 2D lists.
- Take numerical data from the user.
- Demonstrate Python built-in functions.
- Create and use user-defined functions.
- Calculate basic statistics.
- Find duplicate and unique values.
- Demonstrate recursion using factorial calculation.
- Use lambda functions with `filter()`.
- Use lambda functions with `map()`.
- Sort 1D data using `sort()`.
- Sort a 2D list using `sorted()`.
- Demonstrate `*args`.
- Demonstrate `**kwargs`.
- Demonstrate function documentation using `__doc__`.
- Demonstrate the `global` keyword.
- Return multiple values from a function.
- Display a 2D list as a grid.

***

## Features

###  1. Input 1D Data

The program allows the user to enter 1D numerical data manually or use predefined sample data.

The user can choose:

```text
1. Enter data manually
2. Use sample data
```

Manual values are entered separated by spaces.

Example:

```text
10 20 30 40 50
```

The entered values are converted into integers and stored in a list.

***

###  2. Display Data Summary

The program calculates basic statistics using Python built-in functions.

It displays:

- Total number of values
- Minimum value
- Maximum value
- Sum
- Average

The built-in functions used include:

```python
len()
min()
max()
sum()
```

***

###  3. Calculate Average

The program uses a user-defined function called `calculate_average()`.

Example:

```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```

The function calculates and returns the average of the dataset.

***

###  4. Find Duplicate Values

The program searches the dataset for values that occur more than once.

It uses the `count()` method to identify duplicate values.

Duplicate values are stored in a separate list and displayed to the user.

***

###  5. Display Unique Values

The program identifies values that have not already been added to the unique-values list.

A separate list is used to ensure that each value is displayed only once.

***

###  6. Calculate Factorial

The project demonstrates **recursion** through factorial calculation.

The factorial function calls itself until it reaches a base condition.

Example:

```python
def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)
```

For example:

```text
5! = 120
```

The program also checks whether the entered number is negative.

***

###  7. Filter Data Using Lambda

The project demonstrates a lambda function together with `filter()`.

The user enters a threshold value.

The program displays values greater than or equal to that threshold.

Example:

```python
result = list(filter(lambda x: x >= limit, data))
```

***

###  8. Transform Data Using `map()`

The project uses `map()` with a lambda function to transform the dataset.

Each value is multiplied by 2.

Example:

```python
result = list(map(lambda x: x * 2, data))
```

The program displays both the original data and transformed data.

***

###  9. Sort 1D Data

The program allows the user to sort the 1D list.

The available choices are:

```text
1. Ascending
2. Descending
```

The project uses the list `sort()` method.

Example:

```python
data.sort()
```

For descending order:

```python
data.sort(reverse=True)
```

The `sort()` method changes the original list.

***

###  10. Display Dataset Statistics

The program uses a function called `multiply_values()` to calculate multiple statistics.

It returns:

- Minimum
- Maximum
- Total
- Average

Example:

```python
minimum, maximum, total, average = multiply_values(data)
```

This demonstrates returning multiple values from a function.

***

###  11. Demonstrate `*args`

The project demonstrates the use of `*args` to accept multiple positional values.

Example:

```python
def show_args(*args):
```

The values are displayed using a loop.

***

###  12. Demonstrate `**kwargs`

The project demonstrates keyword arguments using `**kwargs`.

Example:

```python
def show_kwargs(**kwargs):
```

The function receives key-value pairs and displays them.

The demonstration includes:

- Total values
- Minimum
- Maximum
- Average

***

###  13. Display Function Documentation

The project demonstrates the `__doc__` attribute.

Functions contain documentation strings called docstrings.

The program displays selected function documentation using:

```python
function_name.__doc__
```

This demonstrates how Python can access documentation written inside functions.

***

###  14. Global Summary

The project demonstrates the `global` keyword.

Two global variables are created:

```python
summary_count = 0
summary_average = 0
```

The `global_summary()` function updates these variables with:

- Total number of values
- Overall average

***

###  15. Enter 2D List

The program allows the user to create a 2D list by entering:

- Number of rows
- Number of columns
- Values for each position

The program displays the 2D list and also displays it as a formatted grid.

Example:

```text
10    20    30
40    50    60
70    80    90
```

***

###  16. Sort 2D List Using `sorted()`

The program contains a sample 2D list:

```python
matrix = [
    [30, 20],
    [50, 70],
    [80, 10]
]
```

The program uses:

```python
new_matrix = sorted(matrix)
```

to create a new sorted version of the 2D list.

This demonstrates the difference between `sort()` and `sorted()`.

The `sort()` method changes the original list, while `sorted()` returns a new sorted list.

***

###  17. Exit Program

The user can select option `17` to exit the application.

The program displays a thank-you message before terminating.

***

##  Python Concepts Used

###  Built-in Functions

The project uses several Python built-in functions:

```python
len()
sum()
min()
max()
```

These functions are used to calculate basic dataset statistics.

***

###  User-Defined Functions

The project is divided into multiple user-defined functions.

Examples include:

```python
input_data()
display_summary()
calculate_average()
find_duplicates()
find_unique()
factorial()
filter_data()
transform_data()
sort_data()
```

Functions make the program organized and easier to understand.

***

###  Recursion

Recursion is demonstrated through the `factorial()` function.

The function calls itself with a smaller number until it reaches the base condition.

***

###  Lambda Functions

Lambda functions are used for short operations.

Examples include:

```python
lambda x: x >= limit
```

and:

```python
lambda x: x * 2
```

***

###  `filter()`

The `filter()` function is used with a lambda function to select values based on a condition.

```python
filter(lambda x: x >= limit, data)
```

***

###  `map()`

The `map()` function is used with a lambda function to transform every value in the dataset.

```python
map(lambda x: x * 2, data)
```

***

###  `sort()` and `sorted()`

The project demonstrates both sorting approaches.

`sort()` modifies the original list:

```python
data.sort()
```

`sorted()` returns a new sorted list:

```python
new_matrix = sorted(matrix)
```

***

###  `*args`

`*args` allows a function to accept multiple positional arguments.

Example:

```python
def show_args(*args):
```

***

###  `**kwargs`

`**kwargs` allows a function to accept multiple keyword arguments.

Example:

```python
def show_kwargs(**kwargs):
```

***

###  `__doc__`

The `__doc__` attribute is used to access a function's documentation string.

Example:

```python
input_data.__doc__
```

***

###  `global` Keyword

The `global` keyword allows a function to modify variables defined outside the function.

The project uses it for:

```python
summary_count
summary_average
```

***

###  Multiple Return Values

The function `multiply_values()` returns multiple values:

```python
return minimum, maximum, total, average
```

These values are then assigned to separate variables.

***

##  Loops and Conditional Statements

The project uses loops and conditional statements throughout the program.

### `while` Loop

The main menu runs continuously using:

```python
while True:
```

The loop stops when the user selects the Exit option.

### `for` Loop

`for` loops are used for:

- Finding duplicate values.
- Finding unique values.
- Displaying `*args`.
- Processing 2D lists.
- Displaying grid values.

### Conditional Statements

The project uses:

- `if`
- `elif`
- `else`

to process menu choices and control different program operations.

***

##  Functions Used

The main functions in the project are:

### `input_data()`

Takes 1D data manually or loads sample data.

### `display_summary()`

Displays basic dataset statistics.

### `calculate_average()`

Calculates the average of the dataset.

### `find_duplicates()`

Finds duplicate values.

### `find_unique()`

Displays unique values.

### `factorial()`

Calculates factorial using recursion.

### `factorial_program()`

Takes a number from the user and displays its factorial.

### `filter_data()`

Filters data using a lambda function and `filter()`.

### `transform_data()`

Transforms data using a lambda function and `map()`.

### `sort_data()`

Sorts the 1D list in ascending or descending order.

### `multiply_values()`

Returns minimum, maximum, total, and average.

### `display_statistics()`

Displays the multiple returned statistics.

### `show_args()`

Demonstrates `*args`.

### `args_program()`

Runs the `*args` demonstration.

### `show_kwargs()`

Demonstrates `**kwargs`.

### `kwargs_program()`

Runs the `**kwargs` demonstration.

### `documentation()`

Displays selected function documentation.

### `global_summary()`

Stores and displays dataset summary using global variables.

### `input_2d_list()`

Creates and displays a user-defined 2D list as a grid.

### `sample_2d_list()`

Displays a sample 2D list and demonstrates `sorted()`.

***

##  Menu-Driven Interface

The program provides the following menu:

```text
1. Input 1D Data
2. Display Data Summary
3. Calculate Average
4. Find the Duplicate Values
5. Display Unique Values
6. Calculate Factorial
7. Filter Data using Lambda
8. Transform data using map
9. Sort 1D Data
10. Display Dataset Statistics
11. Demonstrate *args
12. Demonstrate **kwargs
13. Display Function Documentation
14. Use of Global Summary
15. Enter 2D List
16. Sort 2D List using sorted()
17. Exit
```

The user selects an option by entering the corresponding number.

The `while` loop keeps displaying the menu until option `17` is selected.

***

## 💻 How to Run the Program

1. Open Python or IDLE.
2. Open the Python file:

```text
Functional_Treat.py
```

3. Run the program.
4. The main menu will appear.
5. Enter the number of the required option.
6. Follow the instructions displayed by the program.
7. Select option `17` to exit.

***

## 📂 Program Structure

```text
Functional_Treat/
│
├── Functional_Treat.py
└── README.md
```

The `Functional_Treat.py` file contains the complete Python program.

The `README.md` file contains the project description, objectives, features, concepts, instructions, and other project information.

***

## 🧪 Sample Workflow

A typical demonstration of the program can include:

### Step 1 – Input 1D Data

Select:

```text
1. Input 1D Data
```

The user can enter data manually or select the sample data.

### Step 2 – Display Data Summary

Select:

```text
2. Display Data Summary
```

The program displays the count, minimum, maximum, sum, and average.

### Step 3 – Calculate Average

Select:

```text
3. Calculate Average
```

The program calculates the average using a user-defined function.

### Step 4 – Find Duplicate and Unique Values

Select options:

```text
4. Find the Duplicate Values
5. Display Unique Values
```

The program analyzes the dataset.

### Step 5 – Calculate Factorial

Select:

```text
6. Calculate Factorial
```

Enter a number and the program calculates its factorial using recursion.

### Step 6 – Filter and Transform Data

Select:

```text
7. Filter Data using Lambda
8. Transform data using map
```

The program filters values according to a threshold and transforms the dataset by multiplying values by 2.

### Step 7 – Sort Data

Select:

```text
9. Sort 1D Data
```

Choose ascending or descending order.

### Step 8 – Demonstrate Functions

The user can demonstrate:

```text
11. *args
12. **kwargs
13. Function Documentation
14. Global Summary
```

### Step 9 – Work With 2D Lists

Select:

```text
15. Enter 2D List
16. Sort 2D List using sorted()
```

The program demonstrates creating a 2D list, displaying it as a grid, and sorting a sample 2D list.

### Step 10 – Exit

Select:

```text
17. Exit
```

The program displays the thank-you message and terminates.

***

##  Input Handling and Conditions

The program includes basic checks for different situations.

These include:

- Checking whether data is available before performing calculations.
- Checking whether the user selects a valid menu option.
- Checking for negative numbers before calculating factorial.
- Converting numerical input into integers using `int()`.
- Checking whether a dataset contains values before filtering, transforming, or sorting.

When no data is available, the program displays:

```text
No data available.
```

For an invalid menu choice, the program displays:

```text
Invalid choice.
```

For a negative factorial input, the program displays:

```text
Factorial is not possible for negative numbers.
```

***

##  Assumptions

- 1D data is entered as integers separated by spaces.
- The factorial operation is performed only for non-negative numbers.
- 2D list values are entered as integers.
- The number of values entered for a 2D list depends on the number of rows and columns specified.
- The program stores data only during the current program session.
- No external database is used.
- No external Python libraries are required.

***

##  Author

**Dhruvi Das**

This project was created as part of my Python programming learning and practice.




