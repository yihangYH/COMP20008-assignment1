## Part B Task 4
import re
import pandas as pd
import os
import sys
import nltk
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer 
nltk.download('wordnet')

def main():
    text_str = ""
    args = []
    ID_list =[]
    ## the logic for below code as same as partb3.py
    for i in range(1,len(sys.argv)):
        args.append(sys.argv[i].lower())
        
    df = pd.read_csv('partb1.csv')
    for index, row in df.iterrows():
        if (match(text_str.join(remove_char(row['filename'])),args)) > 0:
                ID_list.append(row['documentID'])
            
        
    print(ID_list)


## the code is quite same as parb3.py, but has some code to do with inexact matching
def match(text, args):
    ps = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    count = 0;
    check_args = []
    for word in text.split(" "):
        for keyword in args:
            ## check the keywords in text. include inexact matching(missing also match with miss missed)
            if keyword == word or ps.stem(keyword) == ps.stem(word) or lemmatizer.lemmatize(keyword) == lemmatizer.lemmatize(word)  :
                check_args.append(keyword)
                count += 1;
                
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




