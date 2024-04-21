# KHADIJA BAZZA, 101282644
# RYAN ALI, 101269781
# IMRAN FARAH, 101264404
# DANIEL YONKEU-CHEUNKO, 101263845

from T059_M1_load_data import add_average, load_data
from T059_M2_sort_plot import sort_students_selection, histogram
from T059_M3_optimization import maximum, minimum

file_loaded = False

filename = input("Please enter the name of the file where your commands are stored: ")
batch_file = open(filename)

for line in batch_file:
    commands = line.strip('\n').split(";")

    if commands[0].upper() == 'L':
        filename = commands[1]
        key = commands[2]

        data = add_average(load_data(filename, key))
        file_loaded = True
        print("Data loaded.")

    if commands[0].upper() == 'Q':
        print("Quit.")
        break

    if file_loaded:

        if commands[0].upper() == 'S':
            attribute = commands[1]
            sorted = sort_students_selection(data, attribute)
            display = commands[2]

            print("Data sorted.")

            if display == 'Y' or display == 'y':
                print(sorted)
        elif commands[0].upper() == 'H':
            attribute = commands[1]

            hist = histogram(data, attribute)
        elif commands[0].upper() == 'W':
            attribute = commands[1]

            print("The worst value for the attribute {0} is {1} with a grade average of {2}.".format(attribute, minimum(data,attribute)[0], minimum(data,attribute)[1]))

        elif commands[0].upper() == 'B':
            attribute = commands[1]

            print("The best value for {0} is {1}.".format(attribute, maximum(data,attribute)[0]))
    else:
        print("File not loaded. Please, load a file first.")