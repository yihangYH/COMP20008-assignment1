## some code idea is from unimelb COMP20008 2021 sem 1 lecture slide
## Part B Task 5
import re
import os
import sys
import pandas as pd
import nltk
from nltk.stem import PorterStemmer
import math
from numpy import dot
import operator
from nltk.stem import WordNetLemmatizer 
nltk.download('wordnet')

def main():
    result = {}
    text_str = ""
    args = []
    ID_list =[]
    score = 0
    ## read commandline arguments
    ## if command line like python partb4.py keyword1 keyword2 keyword3
    ## sys.argv gives partb4.py keyword1 keyword2 keyword3
    ## onle need keyword1 keyword2 keyword3
    for i in range(1,len(sys.argv)):
        args.append(sys.argv[i].lower())
    df = pd.read_csv('partb1.csv')
    
    for index, row in df.iterrows():
        if (match(text_str.join(remove_char(row['filename'])),args)) > 0:
                ID_list.append(row['documentID'])
                ## call TFidf function to caculate TFidf
                score = TFidf(text_str.join(remove_char(row['filename'])),args)
                result[row["documentID"]] = score[0]
    ## print_result function print the final result            
    print_result(result)
    
def print_result(result):
    ## sort the score in descending order
    result = dict(sorted(result.items(),key = operator.itemgetter(1),reverse = True))
    print("documentID" + " " + "score")
    for ID, score in result.items():
        ## format ID let it Align left, the len("documentID") is 10, 4 decimal palces
        print("{:10s}".format(ID) + " " + "{:.4f}".format(score))
    
def TFidf(text, args):
    ps = PorterStemmer()
    lemmatizer = WordNetLemmatizer()                             
    wordDict = dict.fromkeys(args,0)
    tfDict = {}
    for word in text.split(" "):
        for keyword in args:
            if keyword == word or ps.stem(keyword) == ps.stem(word) or lemmatizer.lemmatize(keyword) == lemmatizer.lemmatize(word):
                wordDict[keyword] += 1
    # tf            
    textLen = len(text.split(" "))
    for word, count in wordDict.items():
        tfDict[word] = count/float(textLen)
        
    # idf
    idfDict = dict.fromkeys(tfDict.keys(),0)
    for word,value in tfDict.items():
        idfDict[word] = math.log(1/value) + 1
        
    tfidfDict = dict.fromkeys(tfDict.keys(),0)
    for word,value in idfDict.items():
        tfidfDict[word] = tfDict[word] * idfDict[word]
    normalizedDict = dict.fromkeys(tfDict.keys(),0)
    total = 0
    for word,value in tfidfDict.items():
            total += pow(tfidfDict[word],2)
            
    for word,value in normalizedDict.items():
        normalizedDict[word] = tfidfDict[word]/(math.sqrt(total))
    query_vector = []
    for word in text.split(" "):
        for keyword in args:
            if keyword == word or ps.stem(keyword) == ps.stem(word) :
                query_vector.append(1)
            else:
                query_vector.append(0)
    q_unit = [x/math.sqrt(len(args)) for x in query_vector]
    q_unit = list(filter(lambda num : num != 0 , q_unit))
    for word,value in tfidfDict.items():
        return list(dict.fromkeys(dot(q_unit, tfidfDict[word])))
        

## the code below is the same as partb4.py solutions    
def match(text, args):
    ps = PorterStemmer()
    lemmatizer = WordNetLemmatizer()                             
    count = 0;
    check_args = []
    for word in text.split(" "):
        for keyword in args:
            if keyword == word or ps.stem(keyword) == ps.stem(word) or lemmatizer.lemmatize(keyword) == lemmatizer.lemmatize(word) :
                check_args.append(keyword)
                count += 1;
               
    check_args = list(dict.fromkeys(check_args))       

    
    
    return len(check_args) == len(args)   
        

def remove_char(text):
    punctuation_arr = [" ", "\n", "\t"]
    text_arr = []
    letter_arr = []
    new_text = []
    read_text = open("./cricket/" + text, 'r')
    for line in read_text:
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