## Part B Task 3
import re
import sys
import pandas as pd
import nltk
import os

def main():
    text_str = ""
    args = []
    ID_list =[]
    ## read commandline arguments
    ## if command line like python partb4.py keyword1 keyword2 keyword3
    ## sys.argv gives partb4.py keyword1 keyword2 keyword3
    ## onle need keyword1 keyword2 keyword3
    for i in range(1,len(sys.argv)):
        args.append(sys.argv[i].lower())
        
    ## this requires run partb1.py first    
    df = pd.read_csv('partb1.csv')
    for index, row in df.iterrows():
        ## call match function wo find if keywords match txt
        if match(text_str.join(remove_char(row['filename'])),args) > 0 :
                ID_list.append(row['documentID'])
            
    ## print ID array which contain all the keywords    
    print(ID_list)
    
def match(text, args):
    ## find the match words
    check_args = []
    for word in text.split(" "):
        for keyword in args:
            ## if find match add the word into check_args
            if keyword == word:
                check_args.append(keyword)
    ## in one text it might contains mutiple keywords, need to delete duplicate            
    check_args = list(dict.fromkeys(check_args))
    ## if length of check_args == length args means text contains all the keywords, return true    
    return len(check_args) == len(args)
        
    
## the code below is the same as the partb2.py which is processing the text
def remove_char(text):
    punctuation_arr = [" ", "\n", "\t"]
    letter_arr = []
    new_text = []
    read_text = open("./cricket/" + text, 'r')
    for line in read_text.readlines():
        letter_arr = list(line)
        for letter in letter_arr:
            if letter.isalpha():
                new_text.append(letter)
            elif letter in punctuation_arr:
                new_text.append(letter)
            else:
                new_text.append(" ")
          
    new_text = convert_to_space(new_text)
    new_text = to_lower_case(new_text)
   
    return new_text
        
def convert_to_space(text):
    i = 0
    for i in range(len(text)):
        if text[i] == '\n' or text[i] == '\t':
            text[i] = ' '
    for i in range(len(text) - 1):
        if text[i] == ' ' and text[i+1] == ' ':
            text[i] =''
    return text

def to_lower_case(text):
    i = 0;
    for i in range(len(text)):
        text[i] = text[i].lower()
    return text      
    
main()        