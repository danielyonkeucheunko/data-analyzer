# KHADIJA BAZZA, 101282644
# RYAN ALI, 101269781
# IMRAN FARAH, 101264404
# DANIEL YONKEU-CHEUNKO, 101263845

from T059_M2_sort_plot import add_average, load_data
import scipy.optimize as opt
from curve_fit_tuple import curve_fit_tuple

def minimum(dictionary: dict, attribute: str) -> tuple:
    """
    Returns a tuple containing the x and y value of the local minimum between 
    the lowest and highest value of the attribute.

    >>> minimum(add_average(load_data("student-mat.csv", 'School')),'Age')
    (22.0, 8.02)
    """
    packed = curve_fit_tuple(dictionary, attribute, 2)
    (coef, interval) = packed
    
    def f(x): 
        return 1 * \
        coef[0]*x**2 + coef[1]*x + coef[2]
    min_x = round(opt.fminbound(f, interval[0], interval[1]), 2)
    min_y = round(f(min_x), 2)
    
    return min_x, min_y

def maximum(dictionary: dict, attribute: str) -> tuple:
    """
    Returns a tuple containing the x and y value of the local maximum between 
    the lowest and highest value of the attribute.

    >>> maximum(add_average(load_data("student-mat.csv", 'School')),'Age')
    (16.89, 11.15)    
    """
    packed = curve_fit_tuple(dictionary, attribute, 2)
    (coef, interval) = packed
    
    def f(x): 
        return -(coef[0]*x**2 + coef[1]*x + coef[2])
    max_x = round(opt.fminbound(f, interval[0], interval[1]), 2)
    max_y = round(f(max_x), 2)
    
    return max_x, -max_y


if __name__ == '__main__':
    print(curve_fit_tuple(add_average(load_data("student-mat.csv", 'School')), 'Age', 2))
    print(curve_fit_tuple(add_average(load_data("student-mat.csv", 'School')), 'Health', 2))
    print(curve_fit_tuple(add_average(load_data("student-mat.csv", 'School')), 'Failures', 2))
    print(curve_fit_tuple(add_average(load_data("student-mat.csv", 'School')), 'StudyTime', 2))
    print(curve_fit_tuple(add_average(load_data("student-mat.csv", 'School')), 'Absences', 2))
    print(maximum(add_average(load_data("student-mat.csv", 'School')),'Age'))
    print(maximum(add_average(load_data("student-mat.csv", 'School')),'Health'))
    print(maximum(add_average(load_data("student-mat.csv", 'School')),'Failures'))
    print(maximum(add_average(load_data("student-mat.csv", 'School')),'StudyTime'))
    print(maximum(add_average(load_data("student-mat.csv", 'School')),'Absences'))
    print(minimum(add_average(load_data("student-mat.csv", 'School')),'Age'))
    print(minimum(add_average(load_data("student-mat.csv", 'School')),'Health'))
    print(minimum(add_average(load_data("student-mat.csv", 'School')),'Failures'))
    print(minimum(add_average(load_data("student-mat.csv", 'School')),'StudyTime'))
    print(minimum(add_average(load_data("student-mat.csv", 'School')),'Absences'))