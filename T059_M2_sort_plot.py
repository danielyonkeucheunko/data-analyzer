# KHADIJA BAZZA, 101282644
# RYAN ALI, 101269781
# IMRAN FARAH, 101264404
# DANIEL YONKEU-CHEUNKO, 101263845

from T059_M1_load_data import add_average, load_data
from typing import List
import numpy as np
import matplotlib.pyplot as plt


def student_list(dictionary: dict) -> list:
    """
    Returns a list of dictionary values from dictionary.

    >>>student_list(add_average(load_data("student-mat.csv", 'Health')))
    [{'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6, 'G_Avg': 5.67},{...}, ...]
    """
    new_list = []
    dict_keys = dictionary.keys()
    for key in dict_keys:
        for items in dictionary[key]:
            new_list += [items]
    return new_list


def sort_students_bubble(dictionary: dict, attribute: str) -> List[dict]:
    """
    Returns a sorted list of dictionary based on attribute.

    >>>sort_students_bubble(add_average(load_data("student-mat.csv", 'Failures')), 'Health')
    [{'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Health': 1, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6, 'G_Avg': 5.67}, {...}, ...]
    """
    student = student_list(dictionary)

    n = len(student)
    swapped = False

    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if student[j][attribute] > student[j + 1][attribute]:
                swapped = True
                student[j], student[j + 1] = student[j + 1], student[j]

        if not swapped:
            return

    return student


def sort_students_selection(dictionary: dict, attribute: str) -> List[dict]:
    """
    Returns a sorted list of dictionary based on attribute.

    >>>sort_students_selection(add_average(load_data("student-mat.csv", 'Failures')), 'Health')
    [{'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Health': 1, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6, 'G_Avg': 5.67}, {...}, ...]
    """
    student = student_list(dictionary)

    for index in range(len(student)):
        min_index = index
        for j in student[index]:
            for x in range(index + 1, len(student)):

                if student[x][attribute] < student[min_index][attribute]:
                    min_index = x

            student[index], student[min_index] = student[min_index], student[index]
    return student


def curve_fit(dictionary: dict, attribute: str, degree: int) -> list:
    """
    Return the equation of the best fit of G_Avg in dictionary as a list of coefficients based on the attribute levels and degree provided.

    Preconditions: attribute must be in dictionary

    >>> curve_fit(add_average(load_data("student-mat.csv", 'School')), 'Health', 5)
    [-0.03333333  0.24       -0.27166667 -0.935      11.87      ]
    """
    students = student_list(dictionary)
    temp_dict = {}
    x = []
    y = []

    for student in students:
        if temp_dict.get(student[attribute], 0) != 0:
            temp_dict[student[attribute]] += 1
        else:
            temp_dict[student[attribute]] = 1

    for key in temp_dict.keys():
        x.append(key)

    swap = True
    while swap:
        swap = False
        for i in range(len(x) - 1):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
                swap = True

    for item in x:
        y.append(temp_dict[item])

    sum_y = sum(y)
    num = x[0]

    for j in x:
        count = 0
        total_G_Avg = 0
        for i in range(sum_y):
            if students[i][attribute] == j:
                total_G_Avg += students[i]['G_Avg']
                count += 1
        if count == 0:
            continue
        Avg_G_Avg = round(total_G_Avg / count, 2)

        y[j - num] = Avg_G_Avg

    polynomial = len(y) - 1

    if degree > polynomial:
        z = np.polyfit(x, y, polynomial)
        return z

    else:
        x = np.linspace(0, x[-1] - num, len(x))
        z = np.polyfit(x, y, 2)
        return z


def histogram(dictionary: dict, attribute: str) -> None:
    """
    Plots and shows histogram of dictionary based on the attribute.

    Preconditions: attribute must be in dictionary

    >>> histogram(add_average(load_data("student-mat.csv", 'Failures')), 'School')
    None
    """
    students = student_list(dictionary)
    temp_dict = {}
    x = []
    y = []

    for student in students:
        if temp_dict.get(student[attribute], 0) != 0:
            temp_dict[student[attribute]] += 1
        else:
            temp_dict[student[attribute]] = 1

    for key in temp_dict.keys():
        x.append(key)

    swap = True
    while swap:
        swap = False
        for i in range(len(x) - 1):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
                swap = True

    for item in x:
        y.append(temp_dict[item])

    fig1 = plt.figure()
    plt.title("Student Data Histogram")
    plt.xlabel('Levels')
    plt.ylabel('Number of Students')
    plt.bar(x, y, width=1.0, edgecolor="black", color='violet')
    plt.show()


if __name__ == '__main__':
    print(student_list(add_average(load_data("student-mat.csv", 'Failures'))))
    print(sort_students_bubble(add_average(
        load_data("student-mat.csv", 'Failures')), 'Health'))
    print(sort_students_selection(add_average(
        load_data("student-mat.csv", 'Failures')), 'Health'))
    print(curve_fit(add_average(load_data("student-mat.csv", 'School')), 'Age', 3))
    print(histogram(add_average(load_data("student-mat.csv", 'Failures')), 'School'))
