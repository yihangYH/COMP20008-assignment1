## Part B Task 1
import re
import pandas as pd
import os
import argparse

def process_file():
    ## file path
    path = './cricket'
    files = os.listdir(path)
    
    filename = []
    IDs = []
    ## for loop go thourgh all the .txt files
    for file in files:
        if ".txt" in file:
            ## store filename into filename array
            filename.append(file)
            text = open("./cricket/" + file,'r')
            ## read text line by line
            for line in text.readlines():
                ## creat word array for current line
                word = line.split(" ")
                ## go through each words to check
                for w in word:
                    if "\n" in w:
                        w = w.rstrip("\n")
                    ## if "-" in word, it is possibly be the document ID    
                    if "-" in w:
                        ## split word into 2 parts to check 
                        splitedarr = w.split("-")
                        ## ID is comprised of four letters followed by a hyphen, followed by three numbers
                        if splitedarr[0].isalpha() and splitedarr[1].isnumeric() and splitedarr[0].isupper():
                            ## find ID and add to ID array    
                            IDs.append(w)

                        ## check sconed half part is form like 222A 111C        
                        elif splitedarr[0].isupper() and  len(splitedarr[1]) >= 4 and splitedarr[1][3].isalpha() and splitedarr[1][3].isupper() :
                            IDs.append(w)
                            
                        ## check seconed half part contains numebr  
                        elif splitedarr[0].isupper() and len(splitedarr[1]) >= 4 and splitedarr[1][:2].isnumeric() and not splitedarr[1][3].isalpha():
                            IDs.append(w)
                                                   

 
    ID = find_id(IDs)
    
    
    
    ## read arugument from command line
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    agrs = parser.parse_args()
    ## creat new df to store filename and ID
    df = pd.DataFrame(list(zip(filename,ID)),columns = ["filename","documentID"])
    df.to_csv(agrs.filename,index = False)
    
def find_id(ID_arr):
    IDs = []

    for id in ID_arr:
        ## the ID has 2 formats ABCD-111 length is 8 and ABCD-111A len is 9
        if len(id) == 8 or (len(id) == 9 and id[8].isalpha()):
            IDs.append(id)
        ## check the situtation ABC-111Adog it will give ID ABC-111A   
        elif len(id) > 10 and id[8].isalpha() and id[9].isalpha() and id[8].isupper() and id[9].isupper():
            
            IDs.append(id[:9])
        ## other situtations like in 004.txt, ID in the text is YWCE-738India, the actual ID is YWCE-738, so we only need [:8] parts      
        elif len(id) > 9:
            
            IDs.append(id[:8])
        
    return IDs

process_file()