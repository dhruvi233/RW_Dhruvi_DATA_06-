#Functional_Treat

data = []
summary_count = 0
summary_average = 0

def input_data():
    """Take 1D data from the user."""

    global data
    print("\n1. Enter data manually")
    print("2. Use sample data")

    choice = input("Enter You Choice:")
    if choice == "1":
        values = input("Enter number seprated by spaces:")
        data = [int(x) for x in values.split()]

    elif choice == "2":
        data = [11, 29, 24, 2, 44, 25, 39]

    else:
        print("Invalid choice.")
        return
        

    print("Data stored:", data)

def display_summary():
    """Display basic statistics using built-in functions."""

    if len(data)== 0:
        print("No data available.")
        return
    print("\nData Summary")
    print("Total values:", len(data))
    print("Minimum value:", min(data))
    print("Maximum value:", max(data))
    print("Sum:", sum(data))
    print("Average:", sum(data)/ len(data))

def calculate_average(numbers):
    """Calculate the average of the data"""
    return sum(numbers)/ len(numbers)

def find_duplicates():
    """Find duplicate values in the list."""
    duplicates = []

    for number in data:
        if data.count(number) > 1 and number not in duplicates:
            duplicates.append(number)
    print("Duplicate values:", duplicates)

def find_unique():
    """Display unique value in the list."""
    unique = []

    for number in data:
        if number not in unique:
            unique.append(number)

    print("Unique values:", unique)

def factorial(number):
    """Calculate factorial using recursion."""

    if number == 0 or number ==1:
        return 1
    return number*factorial(number - 1)

def factorial_program():
    """Take a number and display its factorial."""
    number = int(input("Enter a number:"))
    if number < 0:
        print("Factorial is not possible for negative numbers.")
    else:
        print("Factorial:", factorial(number))

def filter_data():
    """Filter data using lambda and filter"""

    if len(data) == 0:
        print("No data available")
        return

    limit = int(input("Enter the threshold:"))
    result = list(filter(lambda x: x>= limit, data))
    print("Values greater than or equal to", limit)
    print(result)

def transform_data():
    """Transform data using lambda and map"""
    if len(data) == 0:
        print("No data available")
        return

    result = list(map(lambda x: x * 2, data))
    print("Original data:", data)
    print("Data after multiplying by 2:", result)


def sort_data():
    """Sort the 1D list using sort:"""

    if len(data) == 0:
        print("No data available")
        return
    print("1. Ascending")
    print("2. Descending")

    choice = input("Enter Your Choice:")

    if choice == "1":
        data.sort()
        print("Ascending order:", data)

    elif choice == "2":
        data.sort(reverse=True)
        print("Descending order:", data)

    else:
        print("Invalid choice")


def multiply_values(numbers):
    """Return multiple statistics."""

    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = sum(numbers)/ len(numbers)

    return minimum, maximum, total, average


def display_statistics():
    """Display multiple returned statistics."""


    if len(data) == 0:
        print("No data available")
        return

    minimum, maximum, total, average = multiply_values(data)

    print("\nDataset  Statistics")
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Total:", total)
    print("Average:", average)


def show_args(*args):
    """Accept and display multiple values using args."""
    print("Values using *args:")

    for value in args:
        print(value)

def args_program():
    """Demonstrate the use of args."""

    if len(data) == 0:
        print("No data available")
        return
    show_args(*data)
    


def show_kwargs (**kwargs):
    """Display key-value pairs using kwargs."""

    for key, value in kwargs.items():
        print(key, ":", value)

def kwargs_program():
    """Demonstrate the use of kwargs."""

    if len(data) == 0:
        print("No data available")
        return

    show_kwargs(
        total_values=len(data),
        minimum=min(data),
        maximum=max(data),
        average=sum(data)/len(data)
    )

def documentation():
    """Display function documentation."""

    print("\nFunction Documentation")
    print("input_data:", input_data.__doc__)
    print("display_summary:", display_summary.__doc__)
    print("calculate_average:", calculate_average.__doc__)
    print("find_duplicates:", find_duplicates.__doc__)
    print("factorial:", factorial.__doc__)
    print("filter_data:", filter_data.__doc__)
    print("transform_data:", transform_data.__doc__)
    print("sort_data:", sort_data.__doc__)

def global_summary():
    """Store dataset summary using global variables."""

    global summary_count
    global summary_average

    if len(data) == 0:
        print("No data available")
        return

    summary_count = len(data)
    summary_average= sum(data)/len(data)

    print("Total values:", summary_count)
    print("Overall average:", summary_average)

def input_2d_list():
    """Take 2D list from the user and display it as a grid."""

    rows = int(input("Enter the  number of rows:"))
    columns = int(input("Enter the number of columns:"))

    matrix = []

    for i in range(rows):
        row = []

        for j in range(columns):
            value = int(input("Enter the value:"))
            row.append(value)

        matrix.append(row)


    print("\n2D List:")
    for row in matrix:
        print(row)

    print("\nGrid:")
    for row in matrix:
        for value in row:
            print(value, end="\t")
        print()

    return matrix

def sample_2d_list():
    """Display a sample 2D list and sort its row."""

    matrix = [
        [30, 20],
        [50, 70],
        [80, 10],
    ]

    print("Original 2D list:")
    print(matrix)
    new_matrix = sorted(matrix)
    print("Sorted 2D list:")
    print(new_matrix)

print("Welcome to the Data Analyzer and Transformer Program")
while True:
    print("\n----------Main Menu--------")
    print("1. Input 1D Data")
    print("2. Display Data Summary")
    print("3. Calculate Average")
    print("4. Find the Duplicate Values")
    print("5. Display Unique Values")
    print("6. Calculate Factorial")
    print("7. Filter Data using Lambda")
    print("8. Transform data using map")
    print("9. Sort 1D Data")
    print("10. Display Dataset Statistics")
    print("11. Demonstrate *args")
    print("12. Demonstrate **kwargs")
    print("13. Display Function Documentation")
    print("14. Use of Global Summary")
    print("15. Enter 2D List")
    print("16. Sort 2D List using sorted()")
    print("17. Exit")

    choice = input("Enter Your Choice:")

    if choice == "1":
        input_data()

    elif choice == "2":
        display_summary()

    elif choice == "3":
        if len(data) == 0:
            print("No data available.")
        else:
            print("Average:", calculate_average(data))

    elif choice == "4":
        if len(data) == 0:
            print("No data available.")
        else:
            find_duplicates()
    elif choice == "5":
        if len (data) == 0:
            print("No data available.")

        else:
            find_unique()

    elif choice == "6":
        factorial_program()
    elif choice == "7":
        filter_data()
    elif choice == "8":
        transform_data()
    elif choice == "9":
        sort_data()
    elif choice == "10":
        display_statistics()
    elif choice == "11":
        args_program()
    elif choice == "12":
        kwargs_program()
    elif choice == "13":
        documentation()
    elif choice == "14":
        global_summary()
    elif choice == "15":
        input_2d_list()
    elif choice == "16":
        sample_2d_list()
    elif choice == "17":
        print("Thank you for using the Data Analyzer and Transformer Program.")
        break
    else:
        print("Invalid choice.")
    
    
    



        





































    


    






























    
























    
    
