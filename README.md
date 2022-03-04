# COMP20008 2021 Semester 1 Assignment 1

## student information

Student name: Yihang Liu
Student ID: 1061578

## programming language

Python

## assignment description

### partA

download the dataset and do data pre_processing, visualisation, write a report.

data pre-processing include get useful columns and calculate case fatality rate yearly and monthly for different locations.

visualisation include use pre-processed data to create two scatter plots

a report of visual analysis of the two scatter plots from visualisation

### partB

build a search engine that allows a user to specify keywords and find all articles that contain those keywords. the search engine contains regular expressions, pre-processing article, basic search, advanced search, search ranking. 

regular expressions find the uniquely ID for each article

pre-processing article perform some pre-processing and make the article easier to search.

basic search allows the user to search for articles containing particular keywords.

advance search based on the basic search, feature to enable inexact matching.

search ranking based on the advance search, feature to enable documents to be ranked.



## general information

the dataset is from https://covid.ourworldindata.org/data/owid-covid-data.csv. Download the .csv file from this link and add it to the directory for the future use.



## issues

ensure the machine have installed pandas and nltk before running the code, otherwise, it will cause ModuleNotFoundError.

there are 2 ways to access the dataset,

- 1st way use link https://covid.ourworldindata.org/data/owid-covid-data.csv to access the .csv.

  ```python
  df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', encoding = 'ISO-8859-1')
  ```

- 2nd way download the .csv file from link first and save it to the same directory, and then read .csv file.

  ```python
  df = pd.read_csv('owid-covid-data.csv', encoding = 'ISO-8859-1')
  ```

doth ways are works, for this assignment, I choose the second way.


in order to run **partb3.py, partb4.py, partb5.py,** the **parta1.py** need to run first. Because **parta1.py** will output a .csv file containing important information for partb3, b4, b5. If **parta1.py** does not run before the others, it will cause an error.

if pull from Github, the output file path for parta1.py is also might affect the other question. Make sure the output file from part1.py should in the same directory.



## list of dependencies

### parta1.py

import the datetime library to help process the df.

the code idea related to argparse is from https://www.youtube.com/watch?v=cdblJqEUDNo (Python Tutorial - Argparse by Johnny Metz)

### parta2.py

the code idea of argparse is mentioned parta1.py. 

plot.scatter() function idea is from University Of Melbourne COMP20008 sem1 2021 lecture.

### partb1.py

import os library to help process the cricket directory. the idea is from https://www.tutorialspoint.com/python/os_listdir.htm (Python os.listdir() Method)

the code idea of argparse is mentioned parta1.py. 

### partb2.py

import sys library to get argv from command line. the idea is from https://www.tutorialsteacher.com/python/sys-module (Python - sys Module)

### partb3.py



### partb4.py

import nltk library to help find the match word. the idea is from University Of Melbourne COMP20008 sem1 2021 lecture. https://www.geeksforgeeks.org/python-stemming-words-with-nltk/ (Python | Stemming words with NLTK), https://pythonprogramming.net/stemming-nltk-tutorial/ (Stemming words with NLTK)

### partb5.py

import operator library to sort the score in descending order. the idea is from https://stackoverflow.com/questions/18595686/how-do-operator-itemgetter-and-sort-work  (How do operator.itemgetter() and sort() work?)

import numpy library to find the dot product. the idea is from https://www.tutorialspoint.com/numpy/numpy_dot.htm (numpy.dot())