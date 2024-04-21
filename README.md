# Analyzer Version 1.0 11/12/2022
## _The Only Data Analyzer You Need!_

---

Analyzer is a compact, ready to use, data analyzer that specializes in analyzing .csv files.

## Features

- Load a .csv file and sort it according to certain attributes
- Make a histogram out of your .csv file's data
- Find the best and worst attributes level for each attribute of your .csv file's data

A Comma Separated Values (CSV) file is a plain text file that contains a list of data. Depending on the size of the file, analyzing the data can be quite tedious which is Analyzer comes in!

## Tech

Analyzer uses a number of libraries to function properly:

- [Numpy] - HTML enhanced for web apps!
- [Scipy] - awesome web-based text editor
- [Matplotlib] - Markdown parser done right. Fast and easy to extend.

## Installation

Analyzer requires [Python3], as well as the IDE of your choice to run properly.

If you do not have Python 3 installed click [here] for an in-depth tutorial.

We recommend [Wing101] if you are in need of an IDE.

## Usage
Analyzer uses text UI to display its commands and register inputs.
Note: you must use the load data command before before any of the other commands are able to function
```
        1. L)oad Data
        2. S)ort Data
                'School'    'Age'    'StudyTime'    'Failures'    'Health'
                'Absences'    'G1'    'G2'    'G3'    'G_Avg'
        3. H)istogram
                'School'    'Age'    'StudyTime'    'Failures'    'Health'
                'Absences'
        4. W)orst _____ for Grades
                'Age'    'StudyTime'    'Failures'    'Health'    'Absences'
        5. B)est  _____ for Grades
                'Age'    'StudyTime'    'Failures'    'Health'    'Absences'
        6. Q)uit
Please type your command: 
```
Analyzer can also use batch files to register inputs.
Each input has to be seperated by a semi-colon.
An Example of this can be seen below
```
L;student-mat.csv;Age
s;Health;N
b;Failures
w;Health
h;StudyTime
Q
```


## Credits
Credit to the team behind Analyzer:

### Daniel Yonkeu-Cheunko:
```sh
student_failures_dictionary()
load_data()
test_3()
student_list()
curve_fit()
Module 1: Text User Interface
README.md
```

### Imran Farah:

```sh
student_school_dictionary()
test_1()
sort_students_bubble()
minimum()
```

### Ryan Ali:

```sh
student_health_dictionary()
test_4()
sort_students_selection()
Module 2: Batch User Interface
```

### Khadija Bazza:

```sh
student_age_dictionary()
test_2()
histogram()
maximum()
```


## Contact Informtion:
Phone: 613-312-7427
Email: danielyonkeucheunko@cmail.carleton.ca

## License
MIT

   [Python3]: <https://www.python.org/downloads/>
   [here]: <https://www.digitalocean.com/community/tutorials/install-python-windows-10>
   [Wing101]: <https://wingware.com/downloads/wing-101>
   [Numpy]: <https://numpy.org/install/>
   [Scipy]: <https://scipy.org/install/>
   [Matplotlib]: <https://matplotlib.org/stable/users/installing/index.html>