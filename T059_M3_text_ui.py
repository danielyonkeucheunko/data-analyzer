# KHADIJA BAZZA, 101282644
# RYAN ALI, 101269781
# IMRAN FARAH, 101264404
# DANIEL YONKEU-CHEUNKO, 101263845

from T059_M1_load_data import add_average, load_data
from T059_M2_sort_plot import sort_students_selection, histogram
from T059_M3_optimization import maximum, minimum

input_text = "\nThe available commands are:\n\t1. L)oad Data\n\t2. S)ort Data\n\t\t'School'    'Age'    'StudyTime'    'Failures'    'Health'\n\t\t'Absences'    'G1'    'G2'    'G3'    'G_Avg'\n\t3. H)istogram\n\t\t'School'    'Age'    'StudyTime'    'Failures'    'Health'\n\t\t'Absences'\n\t4. W)orst _____ for Grades\n\t\t'Age'    'StudyTime'    'Failures'    'Health'    'Absences'\n\t5. B)est  _____ for Grades\n\t\t'Age'    'StudyTime'    'Failures'    'Health'    'Absences'\n\t6. Q)uit\n\nPlease type your command: "

stop = False

file_loaded = False
supported_inputs = ['L', 'S', 'H', 'W', 'B', 'Q']
supported_keys = ['Health', 'School', 'Failures', 'Age']
sorting_attributes = ['School', 'Age', 'StudyTime',
                      'Failures', 'Health', 'Absences', 'G1', 'G2', 'G3', 'G_Avg']
histogram_attributes = ['School', 'Age',
                        'StudyTime', 'Failures', 'Health', 'Absences']
worst_attributes = ['Age', 'StudyTime', 'Failures', 'Health', 'Absences']

while stop == False:

    user_input = input(input_text)
    user_input = user_input.upper()

    while user_input not in supported_inputs:
        user_input = input(
            "Invalid Input. Try Again.\nPlease type your command: ")
        user_input = user_input.upper()

    if user_input == 'L':
        filename = input("Please enter the name of the file: ")
        key = input("Please enter the attribute to use as a key: ")

        while key not in supported_keys:
            key = input(
                "Invalid Key. Try Again.\nPlease enter the attribute to use as key: ")
        data = add_average(
            load_data(filename, key))
        file_loaded = True
        print("Data loaded.")

    if user_input == 'Q':
        print("Quit.")
        break

    if file_loaded:

        if user_input == 'S':
            attribute = input(
                "Please enter the attribute you want to use for sorting: ")

            while attribute not in sorting_attributes:
                attribute = input(
                    "Invalid Attribute. Try Again.\nPlease enter the attribute you want to use for sorting: ")

            sorted = sort_students_selection(data, attribute)
            print("Data Sorted.")
            display = input(
                "Do you want to display the data?: ")

            if display == 'Y' or display == 'y':
                print(sorted)
        elif user_input == 'H':
            attribute = input(
                "Please enter the attribute you want to use for the histogram: ")

            while attribute not in histogram_attributes:
                attribute = input(
                    "Invalid Attribute. Try Again.\nPlease enter the attribute you want to use for the histogram: ")

            hist = histogram(data, attribute)
        elif user_input == 'W':
            attribute = input(
                "Please enter the attribute you want to use: ")

            while attribute not in worst_attributes:
                attribute = input(
                    "Invalid Attribute. Try Again.\nPlease enter the attribute you want to use: ")
            print(minimum(data,attribute))

            print("The worst value for the attribute {0} is {1} with a grade average of {2}.".format(
                attribute, minimum(data,attribute)[0], minimum(data,attribute)[1]))

        elif user_input == 'B':
            attribute = input(
                "Please enter the attribute you want to use: ")

            while attribute not in worst_attributes:
                attribute = input(
                    "Invalid Attribute. Try Again.\nPlease enter the attribute you want to use: ")
            print("The best value for the attribute {0} is {1} with a grade average of {2}.".format(
                attribute, maximum(data,attribute)[0], maximum(data,attribute)[1]))
    else:
        print("File not loaded. Please, load a file first.")


