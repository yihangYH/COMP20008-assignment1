# Part B Task 2
import re
import os
import sys
import argparse

def process_file():
    text_str = ""
    filename_arr = []
    ## the command line argument is crickert001.txt
    ## split it to cricket and 001.txt to help to access the file
    ## [:7] -> cricket
    ## [7:] -> 001.txt
    filename_arr.append(sys.argv[1][:7])
    filename_arr.append(sys.argv[1][7:])
    ## if command line is python partb2.py cricket001.txt
    ## when open the .txt the path is ("./cricket/001.txt")
    text = open("./" + filename_arr[0]+ "/" + filename_arr[1] ,'r')
    ## print it to standard output
    print(text_str.join(remove_char(text)))
    
def remove_char(text):
    punctuation_arr = [" ", "\n", "\t"]
    ## letter_arr store every letter
    letter_arr = []
    ## new_text array store the text that is after processing 
    new_text = []
    
    for line in text.readlines():
        ## put each letter in line to the array
        letter_arr = list(line)
        for letter in letter_arr:
            ## check letetr is Alphabet
            if letter.isalpha():
                new_text.append(letter)
            ## check if it is whitespaces, tabs and newlines char
            elif letter in punctuation_arr:
                new_text.append(letter)
            else:
                new_text.append(" ") 
    ## call function to process to whitespace          
    new_text = convert_to_space(new_text)
    ## call function to change uppercase to lowercase
    new_text = to_lower_case(new_text)
    
    return new_text
        
def convert_to_space(text):
    i = 0
    for i in range(len(text)):
        ## convert tabs and newlines char to whitespaces
        if text[i] == '\n' or text[i] == '\t':
            text[i] = ' '
    for i in range(len(text) - 1):
        ## convert mutiple whitespace to 1 whitespace
        if text[i] == ' ' and text[i+1] == ' ':
            text[i] =''
           
    return text
def to_lower_case(text):
    i = 0;
    ## convert uppercase to lwoercase
    for i in range(len(text)):
        text[i] = text[i].lower()
    return text    

process_file()