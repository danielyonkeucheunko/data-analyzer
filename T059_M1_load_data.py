# KHADIJA BAZZA, 101282644
# RYAN ALI, 101269781
# IMRAN FARAH, 101264404
# DANIEL YONKEU-CHEUNKO, 101263845

import string
from typing import List
from check_equal import check_equal


def student_failures_dictionary(filename: str) -> dict[List]:
    """
    Returns a dictionary containing a list with the data of every student, with the amount of failures they have serving as the key.

    Preconditions:
    The .csv file should be in the same folder as the python file.

    >>> student_failures_dictionary("student-mat.csv")
    {'0': [{'School': 'GP', 'Age': '18', 'StudyTime': '2', 'Health': '3', 'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'},{...} ...] ...}
    """
    lines = [line for line in open(filename)]
    myDict = {}

    for i in range(0, 11):
        myDict[i] = []

    for i in range(1, len(lines)):
        temp_arr = lines[i].split(",")
        localDict = {}
        localDict['School'] = temp_arr[0]
        localDict['Age'] = int(temp_arr[1])
        localDict['StudyTime'] = int(temp_arr[2])
        localDict['Health'] = int(temp_arr[4])
        localDict['Absences'] = int(temp_arr[5])
        localDict['G1'] = int(temp_arr[6])
        localDict['G2'] = int(temp_arr[7])
        lenG3 = len(temp_arr[8])
        localDict['G3'] = int(temp_arr[8][:lenG3 - 1])

        myDict[int(temp_arr[3])].append(localDict)
    return myDict


def student_school_dictionary(filename: str) -> dict[List]:
    """
    Returns a dictionary containing lists with the data of every student, with the school they attend serving as the key.

    Preconditions:
    The .csv file should be in the same folder as the python file.

    >>> student_school_dictionary('student-mat.csv')
    { 'GP' : [ {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6 }, {another element},… ], 'MB' : [ {'Age': 16, 'StudyTime': 2.6, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 10, 'G2': 12, 'G3': 12 }, {another element}, … ], … }
    """
    lines = [line for line in open(filename)]
    myDict = {}

    myDict['GP'] = []
    myDict['MB'] = []
    myDict['CF'] = []
    myDict['BD'] = []
    myDict['MS'] = []

    for i in range(1, len(lines)):
        temp_arr = lines[i].split(",")
        localDict = {}
        localDict['Age'] = int(temp_arr[1])
        localDict['StudyTime'] = int(temp_arr[2])
        localDict['Failures'] = int(temp_arr[3])
        localDict['Health'] = int(temp_arr[4])
        localDict['Absences'] = int(temp_arr[5])
        localDict['G1'] = int(temp_arr[6])
        localDict['G2'] = int(temp_arr[7])
        lenG3 = len(temp_arr[8])
        localDict['G3'] = int(temp_arr[8][:lenG3 - 1])

        myDict[str(temp_arr[0])].append(localDict)
    return myDict


def student_age_dictionary(filename: str) -> dict[List]:
    """
    Returns a dictionary containing lists with the data of every student, with their age serving as the key.

    Preconditions:
    The .csv file should be in the same folder as the python file.

    >>> student_age_dictionary("student-mat.csv")
    { 15 : [ {'School': 'GP', 'StudyTime': 4.2, 'Failures': 3, 'Health': 3, 'Absences': 6, 'G1': 7, 'G2': 8, 'G3': 10}, {another element}, … ], …}
    """

    lines = [line for line in open(filename)]
    myDict = {}

    for i in range(15, 23):
        myDict[i] = []

    for i in range(1, len(lines)):
        temp_arr = lines[i].split(",")
        localDict = {}
        localDict['School'] = temp_arr[0]
        localDict['StudyTime'] = int(temp_arr[2])
        localDict['Failures'] = int(temp_arr[3])
        localDict['Health'] = int(temp_arr[4])
        localDict['Absences'] = int(temp_arr[5])
        localDict['G1'] = int(temp_arr[6])
        localDict['G2'] = int(temp_arr[7])
        lenG3 = len(temp_arr[8])
        localDict['G3'] = int(temp_arr[8][:lenG3 - 1])

        myDict[int(temp_arr[1])].append(localDict)
    return myDict


def student_health_dictionary(filename: str) -> dict[List]:
    """
    Returns a dictionary containing student information (School, Age, Study Time, Failures, Absences, G1, G2, G3) based on their health.

    Preconditions:
    The .csv file should be in the same folder as the python file.

    >>> student_health_dictionary('student-mat.csv')
    { 1 : [ {'School':'GP', 'Age': 17, 'StudyTime': 4.2, 'Failures': 3, 'Absences': 6, 'G1': 7, 'G2': 8, 'G3': 10 }, {another element}, … ], 2 : [ {'School': 'MS', 'Age': 20, 'StudyTime': 1.2, 'Failures': 1, 'Absences': 10, 'G1': 9, 'G2': 11, 'G3': 7}, {another element}, … ],…}

    """
    lines = [line for line in open(filename)]
    myDict = {}

    for i in range(1, 6):
        myDict[i] = []

    for i in range(1, len(lines)):
        temp_arr = lines[i].split(",")
        localDict = {}
        localDict['School'] = temp_arr[0]
        localDict['Age'] = int(temp_arr[1])
        localDict['StudyTime'] = int(temp_arr[2])
        localDict['Failures'] = int(temp_arr[3])
        localDict['Absences'] = int(temp_arr[5])
        localDict['G1'] = int(temp_arr[6])
        localDict['G2'] = int(temp_arr[7])
        lenG3 = len(temp_arr[8])
        localDict['G3'] = int(temp_arr[8][:lenG3 - 1])

        myDict[int(temp_arr[4])].append(localDict)
    return myDict


def load_data(filename: str, key: str) -> dict[List]:
    """
    Returns a dictionary of the data from filename and sorts it depending on the value of the paramater key.

    >>> load_data("student-mat.csv", 'School')
    { 'GP' : [ {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6 }, {another element},… ], 'MB' : [ {'Age': 16, 'StudyTime': 2.6, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 10, 'G2': 12, 'G3': 12 }, {another element}, … ], … }

    >>> load_data("student-mat.csv", 'Health')
    { 1 : [ {'School':'GP', 'Age': 17, 'StudyTime': 4.2, 'Failures': 3,'Absences': 6, 'G1': 7, 'G2': 8, 'G3': 10 }, {another element}, … ], 2 : [ {'School': 'MS', 'Age': 20, 'StudyTime': 1.2, 'Failures': 1, 'Absences': 10, 'G1': 9, 'G2': 11, 'G3': 7}, {another element}, … ], … }

    >>> load_data("student-mat.csv", 'Failures')
    {'0': [{'School': 'GP', 'Age': '18', 'StudyTime': '2', 'Health': '3', 'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'},{...} ...] ...}
    """
    if key == 'School':
        return student_school_dictionary(filename)
    elif key == 'Failures':
        return student_failures_dictionary(filename)
    elif key == 'Age':
        return student_age_dictionary(filename)
    elif key == 'Health':
        return student_health_dictionary(filename)
    else:
        return {}


def add_average(dictionary: dict) -> dict:
    """Returns dictionary with the average grade as an additional attribute to the dictionary.

    >>> add_average(student_health_dictionary('student-mat.txt')) 
    { 1 : [ {'School':'GP', 'Age': 17, 'StudyTime': 4.2, 'Failures': 3,'Absences': 6, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg': 4.17 }, {another element}, … ], 2 : [ {'School': 'MS', 'Age': 20, 'StudyTime': 1.2, 'Failures': 1, 'Absences': 10, 'G1': 9, 'G2': 11, 'G3': 7, 'G_Avg': 9}, {another element}, … ], … }
    """

    for i in dictionary:
        for s in dictionary[i]:
            avg = s['G1'] + s['G2'] + s['G3']
            s['G_Avg'] = round(avg / 3, 2)

    return dictionary


def test_1() -> str:
    """
    Tests student_health_dictionary, student_failures_dictionary, 
    student_school_dictionary, and student_age_dictionary to see if the keys
    contained within them are accurate.

    >>> test_1()

    Test 1 Results
    ======================================
    student_health_dictionary Dictionary Keys PASSED
    ------
    student_failures_dictionary Dictionary Keys PASSED
    ------
    student_school_dictionary Dictionary Keys PASSED
    ------
    student_age_dictionary Dictionary Keys PASSED
    ------
    Test Passed: 4
    Test Failed: 0
    """
    test_passes = 0
    test_fails = 0

    print("\nTest 1 Results")
    print("======================================")

    health_set = {1, 2, 3, 4, 5}
    empty_health = set()

    for keys in load_data("student-mat.csv", 'Health').keys():
        empty_health.add(keys)
    check_equal('student_health_dictionary Dictionary Keys',
                empty_health, health_set)
    if empty_health == health_set:
        test_passes += 1
    else:
        test_fails += 1

    failures_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    empty_failures = set()

    for keys in load_data("student-mat.csv", 'Failures').keys():
        empty_failures.add(keys)
    check_equal('student_failures_dictionary Dictionary Keys',
                empty_failures, failures_set)
    if empty_failures == failures_set:
        test_passes += 1
    else:
        test_fails += 1

    school_set = {'GP', 'MB', 'CF', 'BD', 'MS'}
    empty_school = set()
    for keys in load_data("student-mat.csv", 'School').keys():
        empty_school.add(keys)
    check_equal('student_school_dictionary Dictionary Keys',
                empty_school, school_set)
    if empty_school == school_set:
        test_passes += 1
    else:
        test_fails += 1

    age_set = {15, 16, 17, 18, 19, 20, 21, 22}
    empty_age = set()

    for keys in load_data("student-mat.csv", 'Age').keys():
        empty_age.add(keys)
    check_equal('student_age_dictionary Dictionary Keys', empty_age, age_set)
    if empty_age == age_set:
        test_passes += 1
    else:
        test_fails += 1

    print("Test Passed: " + str(test_passes))
    print("Test Failed: " + str(test_fails))


def test_2() -> str:
    """
    Returns "Passed" based on whether the size of the lists the students are in is correct

    >>> test_2()

    Test 2 Results
    ======================================
    student_health_dictionary List Size PASSED
    ------
    student_failures_dictionary List Size PASSED
    ------
    student_school_dictionary List Size PASSED
    ------
    student_age_dictionary List Size PASSED
    ------
    Test Passed: 4
    Test Failed: 0
    """

    dict_passes = 0
    dict_fails = 0
    list_length = 395

    print("\nTest 2 Results")
    print("======================================")

    health_length = 0
    for i in range(1, 6):
        health_length += len(load_data("student-mat.csv", 'Health')[i])
    check_equal('student_health_dictionary List Size',
                health_length, list_length)
    if list_length == health_length:
        dict_passes += 1
    else:
        dict_fails += 1

    failures_length = 0
    for i in range(0, 11):
        failures_length += len(load_data("student-mat.csv", 'Failures')[i])
    check_equal('student_failures_dictionary List Size',
                failures_length, list_length)
    if list_length == failures_length:
        dict_passes += 1
    else:
        dict_fails += 1

    school_length = 0
    school_length += len(load_data("student-mat.csv", 'School')['GP'])
    school_length += len(load_data("student-mat.csv", 'School')['MB'])
    school_length += len(load_data("student-mat.csv", 'School')['CF'])
    school_length += len(load_data("student-mat.csv", 'School')['BD'])
    school_length += len(load_data("student-mat.csv", 'School')['MS'])

    check_equal('student_school_dictionary List Size',
                school_length, list_length)
    if list_length == school_length:
        dict_passes += 1
    else:
        dict_fails += 1

    age_length = 0
    for i in range(15, 23):
        age_length += len(load_data("student-mat.csv", 'Age')[i])
    check_equal('student_age_dictionary List Size', age_length, list_length)
    if list_length == age_length:
        dict_passes += 1
    else:
        dict_fails += 1

    print("Test Passed: " + str(dict_passes))
    print("Test Failed: " + str(dict_fails))


def test_3() -> str:
    """Returns "Passed" based on whether the student dictionaries are stored correctly.
    >>> test_3()

    Test 3 Results
    ======================================
    student_health_dictionary Storage PASSED
    ------
    student_failures_dictionary Storage PASSED
    ------
    student_school_dictionary Storage PASSED
    ------
    student_age_dictionary Storage PASSED
    ------
    Test Passed: 4
    Test Failed: 0
    """

    dict_passes = 0
    dict_fails = 0

    print("\nTest 3 Results")
    print("======================================")

    health_set = {'School', 'Age', 'StudyTime',
                  'Failures', 'Absences', 'G1', 'G2', 'G3'}
    blank_health = set()
    for keys in load_data("student-mat.csv", 'Health')[1][0].keys():
        blank_health.add(keys)
    check_equal('student_health_dictionary Storage',
                blank_health, health_set)
    if blank_health == health_set:
        dict_passes += 1
    else:
        dict_fails += 1

    failures_set = {'School', 'Age', 'StudyTime',
                    'Health', 'Absences', 'G1', 'G2', 'G3'}
    blank_failures = set()
    for keys in load_data("student-mat.csv", 'Failures')[1][0].keys():
        blank_failures.add(keys)
    check_equal('student_failures_dictionary Storage',
                blank_failures, failures_set)
    if blank_failures == failures_set:
        dict_passes += 1
    else:
        dict_fails += 1

    school_set = {'Age', 'StudyTime', 'Failures',
                  'Health', 'Absences', 'G1', 'G2', 'G3'}
    blank_school = set()
    for keys in load_data("student-mat.csv", 'School')['GP'][0].keys():
        blank_school.add(keys)
    check_equal('student_school_dictionary Storage',
                blank_school, school_set)
    if blank_school == school_set:
        dict_passes += 1
    else:
        dict_fails += 1

    age_set = {'School', 'StudyTime', 'Failures',
               'Health', 'Absences', 'G1', 'G2', 'G3'}
    blank_age = set()
    for keys in load_data("student-mat.csv", 'Age')[15][0].keys():
        blank_age.add(keys)
    check_equal('student_age_dictionary Storage', blank_age, age_set)
    if blank_age == age_set:
        dict_passes += 1
    else:
        dict_fails += 1

    print("Test Passed: " + str(dict_passes))
    print("Test Failed: " + str(dict_fails))


def test_4() -> str:
    """
    Returns "Passed" based on whether the size of the lists the students are in is correct

    >>> test_4()

    Test 4 Results
    ======================================
    student_health_dictionary_length PASSED
    ------
    student_failures_dictionary_length PASSED
    ------
    student_school_dictionary_length PASSED
    ------
    student_age_dictionary_length PASSED
    ------
    student_health_dictionary G_Avg Added PASSED
    ------
    student_failures_dictionary G_Avg Added PASSED
    ------
    student_school_dictionary G_Avg Added PASSED
    ------
    student_age_dictionary G_Avg Added PASSED
    ------
    student_health_dictionary G_Avg Calculations PASSED
    ------
    student_failures_dictionary G_Avg Calculations PASSED
    ------
    student_school_dictionary G_Avg Calculations PASSED
    ------
    student_age_dictionary G_Avg Calculations PASSED
    ------
    Test Passed: 12
    Test Failed: 0
    """

    dict_passes = 0
    dict_fails = 0
    list_length = 395

    print("\nTest 4 Results")
    print("======================================")

    health_length = 0
    for i in range(1, 6):
        health_length += len(add_average(
            load_data("student-mat.csv", 'Health'))[i])
    check_equal('student_health_dictionary_length',
                health_length, list_length)
    if list_length == health_length:
        dict_passes += 1
    else:
        dict_fails += 1

    failures_length = 0
    for i in range(0, 11):
        failures_length += len(add_average(
            load_data("student-mat.csv", 'Failures'))[i])
    check_equal('student_failures_dictionary_length',
                failures_length, list_length)
    if list_length == failures_length:
        dict_passes += 1
    else:
        dict_fails += 1

    school_length = 0
    school_length += len(add_average(load_data("student-mat.csv",
                         'School'))['GP'])
    school_length += len(add_average(load_data("student-mat.csv",
                         'School'))['MB'])
    school_length += len(add_average(load_data("student-mat.csv",
                         'School'))['CF'])
    school_length += len(add_average(load_data("student-mat.csv",
                         'School'))['BD'])
    school_length += len(add_average(load_data("student-mat.csv",
                         'School'))['MS'])

    check_equal('student_school_dictionary_length',
                school_length, list_length)
    if list_length == school_length:
        dict_passes += 1
    else:
        dict_fails += 1

    age_length = 0
    for i in range(15, 23):
        age_length += len(add_average(load_data("student-mat.csv",
                          'Age'))[i])
    check_equal('student_age_dictionary_length', age_length, list_length)
    if list_length == age_length:
        dict_passes += 1
    else:
        dict_fails += 1

    health_set = {'School', 'Age', 'StudyTime',
                  'Failures', 'Absences', 'G1', 'G2', 'G3', 'G_Avg'}
    blank_health = set()
    for keys in add_average(
            load_data("student-mat.csv", 'Health'))[1][0].keys():
        blank_health.add(keys)
    check_equal('student_health_dictionary G_Avg Added',
                blank_health, health_set)
    if blank_health == health_set:
        dict_passes += 1
    else:
        dict_fails += 1

    failures_set = {'School', 'Age', 'StudyTime',
                    'Health', 'Absences', 'G1', 'G2', 'G3', 'G_Avg'}
    blank_failures = set()
    for keys in add_average(
            load_data("student-mat.csv", 'Failures'))[1][0].keys():
        blank_failures.add(keys)
    check_equal('student_failures_dictionary G_Avg Added',
                blank_failures, failures_set)
    if blank_failures == failures_set:
        dict_passes += 1
    else:
        dict_fails += 1

    school_set = {'Age', 'StudyTime', 'Failures',
                  'Health', 'Absences', 'G1', 'G2', 'G3', 'G_Avg'}
    blank_school = set()
    for keys in add_average(
            load_data("student-mat.csv", 'School'))['GP'][0].keys():
        blank_school.add(keys)
    check_equal('student_school_dictionary G_Avg Added',
                blank_school, school_set)
    if blank_school == school_set:
        dict_passes += 1
    else:
        dict_fails += 1

    age_set = {'School', 'StudyTime', 'Failures',
               'Health', 'Absences', 'G1', 'G2', 'G3', 'G_Avg'}
    blank_age = set()
    for keys in add_average(
            load_data("student-mat.csv", 'Age'))[15][0].keys():
        blank_age.add(keys)
    check_equal('student_age_dictionary G_Avg Added', blank_age, age_set)
    if blank_age == age_set:
        dict_passes += 1
    else:
        dict_fails += 1

    health_calculated_g_avg = 0
    health_G_Avg = 0
    health_calculated_g_avg += add_average(
        load_data("student-mat.csv", 'Health'))[1][0]['G1']
    health_calculated_g_avg += add_average(
        load_data("student-mat.csv", 'Health'))[1][0]['G2']
    health_calculated_g_avg += add_average(
        load_data("student-mat.csv", 'Health'))[1][0]['G3']
    health_G_Avg += add_average(
        load_data("student-mat.csv", 'Health'))[1][0]['G_Avg']
    health_calculated_g_avg = round(health_calculated_g_avg / 3, 2)
    check_equal('student_health_dictionary G_Avg Calculations',
                health_calculated_g_avg, health_G_Avg)
    if health_calculated_g_avg == health_G_Avg:
        dict_passes += 1
    else:
        dict_fails += 1

    failures_calculated_g_avg = 0
    failures_G_Avg = 0
    failures_calculated_g_avg += add_average(
        load_data("student-mat.csv", 'Failures'))[1][0]['G1']
    failures_calculated_g_avg += add_average(
        load_data("student-mat.csv", 'Failures'))[1][0]['G2']
    failures_calculated_g_avg += add_average(
        load_data("student-mat.csv", 'Failures'))[1][0]['G3']
    failures_G_Avg += add_average(
        load_data("student-mat.csv", 'Failures'))[1][0]['G_Avg']
    failures_calculated_g_avg = round(failures_calculated_g_avg / 3, 2)
    check_equal('student_failures_dictionary G_Avg Calculations',
                failures_calculated_g_avg, failures_G_Avg)
    if failures_calculated_g_avg == failures_G_Avg:
        dict_passes += 1
    else:
        dict_fails += 1

    school_calculated_g_avg = 0
    school_G_Avg = 0
    school_calculated_g_avg += add_average(
        load_data("student-mat.csv", 'School'))['GP'][0]['G1']
    school_calculated_g_avg += add_average(
        load_data("student-mat.csv", 'School'))['GP'][0]['G2']
    school_calculated_g_avg += add_average(
        load_data("student-mat.csv", 'School'))['GP'][0]['G3']
    school_G_Avg += add_average(
        load_data("student-mat.csv", 'School'))['GP'][0]['G_Avg']
    school_calculated_g_avg = round(school_calculated_g_avg / 3, 2)
    check_equal('student_school_dictionary G_Avg Calculations',
                school_calculated_g_avg, school_G_Avg)
    if school_calculated_g_avg == school_G_Avg:
        dict_passes += 1
    else:
        dict_fails += 1

    age_calculated_g_avg = 0
    age_G_Avg = 0
    age_calculated_g_avg += add_average(
        load_data("student-mat.csv", 'Age'))[15][0]['G1']
    age_calculated_g_avg += add_average(
        load_data("student-mat.csv", 'Age'))[15][0]['G2']
    age_calculated_g_avg += add_average(
        load_data("student-mat.csv", 'Age'))[15][0]['G3']
    age_G_Avg += add_average(
        load_data("student-mat.csv", 'Age'))[15][0]['G_Avg']
    age_calculated_g_avg = round(age_calculated_g_avg / 3, 2)
    check_equal('student_age_dictionary G_Avg Calculations',
                age_calculated_g_avg, age_G_Avg)
    if age_calculated_g_avg == age_G_Avg:
        dict_passes += 1
    else:
        dict_fails += 1

    print("Test Passed: " + str(dict_passes))
    print("Test Failed: " + str(dict_fails))


if __name__ == '__main__':

    print(student_school_dictionary("student-mat.csv"))
    print(load_data("student-mat.csv", 'School'))
    print(add_average(load_data("student-mat.csv", 'School')))
    test_1()
    test_2()
    test_3()
    test_4()
