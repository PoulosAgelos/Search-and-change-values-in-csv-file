# -*- coding: utf-8 -*-
import csv
from csv import writer
import pandas as pd

def appendNewRow(csvFileName, elementsToAppend):
    # open the csv file in the append mode
    with open(csvFileName, 'a+', newline='') as append_obj:
        # created a writer object from the writer module
        append_writer = writer(append_obj)
        # the created writer object which writes new row to the csv
        append_writer.writerow(elementsToAppend)

#read the file
file = open(r'C:\Users\...\filename.csv') #read the file
csvreader = csv.reader(file)
counter=0
df = pd.read_csv(r'C:\Users\...\filename.csv',low_memory=False) #===> reads in all the rows, but skips the first one as it is a header.

rows=len(df.axes[0]) #===> Axes of 0 is for a row
columns=len(df.axes[1]) #===> Axes of 0 is for a column


#rows of file
for i in range(rows):
    flag = False
    #first header-pointer
    header= next(csvreader)
    header2=header
    #columns of file
    for j in range(columns):
        # check SSS
        if(header2[j]=="strvalue") or flag:
            #print("the line is:",i)
            counter+=1
            flag=True

        if j>9:
            if flag:
                try:
                    if int(header2[j])<20:
                        #print(header[j], i, j)
                        header2[j]= None
                except:
                    pass


    appendNewRow(r'C:\Users\...\finalfile.csv',header2)   #call append function

#numbers of row with strvalue
print(counter)
file.close()




