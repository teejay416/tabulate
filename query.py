import csv
import re
import pandas as pd

def query_filter(df,query):
    #Store query in a buffer
    querytmp=query
    #Identify and store all string operands
    stringoperands = re.findall("\'[\w\d\s]+\'", query)
    #Make sure values in series are unique
    stringoperands=pd.Series(stringoperands).unique()
    #Clear string operands from query buffer to identify number operands
    i=0
    while i<len(stringoperands):
      querytmp=str.replace(querytmp,stringoperands[i]," ")
      i=i+1
    #Identify and store all number operands
    numberoperands=re.findall("(?<=\s)\d+",querytmp)
    #Make sure values in series are unique
    numberoperands=pd.Series(numberoperands).unique()
    # Clear number operands from query buffer to identify column names
    i=0
    while i<len(numberoperands):
      querytmp=str.replace(querytmp,numberoperands[i]," ")
      i=i+1
    #Remove ( ) from query buffer to identify column names
    querytmp=str.replace(querytmp,"("," ")
    querytmp=str.replace(querytmp,")"," ")
    columnlist=re.findall("[A-Z_a-z\d]+",querytmp)
    #Make sure values in series are unique
    columnlist=pd.Series(columnlist).unique()
    #Format query for dataframe filtering
    i=0
    while i<len(columnlist):
        query=str.replace(query,columnlist[i],"(df['"+columnlist[i]+"']")
        i=i+1
    i=0
    while i<len(numberoperands):
        query = str.replace(query, numberoperands[i], numberoperands[i] + ")")
        i=i+1
    i=0
    while i<len(stringoperands):
        query = str.replace(query, stringoperands[i], stringoperands[i] + ")")
        i=i+1
    #Format for dataframe filtering in Python
    query=str.replace(query,"&&","&")
    query=str.replace(query,"||","|")
    query=str.replace(query,";","")
    #Correctly formatted query that will filter values are create new dataframe
    processedquery="newdf = df[("+query+")]"
    return processedquery
