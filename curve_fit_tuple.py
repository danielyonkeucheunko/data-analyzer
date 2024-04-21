# KHADIJA BAZZA, 101282644
# RYAN ALI, 101269781
# IMRAN FARAH, 101264404
# DANIEL YONKEU-CHEUNKO, 101263845

from T059_M2_sort_plot import student_list
import numpy as np


def curve_fit_tuple(dictionary: dict, attribute: str, degree: int) -> tuple:
    """
    Return the equation of the best fit of G_Avg in dictionary as a list of coefficients based on the attribute levels and degree provided.

    Preconditions: attribute must be in dictionary

    >>>curve_fit(add_average(load_data("student-mat.csv", 'School')), 'Health', 2)
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
    y = []

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

        y.append(Avg_G_Avg)

    polynomial = len(y) - 1
    
    if degree > polynomial:
        z = np.polyfit(x, y, polynomial)
        l = [min(x), max(x)]
        return z, l

    else:
        x = np.linspace(x[0], x[-1], len(x))
        z = np.polyfit(x, y, 2)
        l = [min(x), max(x)]
        return z, l