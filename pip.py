import json
import pandas as pd
import query
import tab
json_data=open('spec.json')
jdata = json.load(json_data)
df = pd.DataFrame.from_csv('data.csv')
#Clear output file
f = open("output.csv","w")
f.truncate()
f.close()
#Traverse JSON Object
print (jdata.keys())
for key in jdata.keys():
    first_col = jdata[key]["col"]
    #second_col element not mandatory
    if 'second_col' in jdata[key]:
        second_col = jdata[key]["second_col"]
    else:
        second_col = ""
    func=jdata[key]["func"]
    #query element not mandatory
    if 'query' in jdata[key]:
        querystring = jdata[key]["query"]
    else:
        querystring = ""
    #If query element exists, process query and then carry out tabulate
    if (querystring!=""):
        processedquery=query.query_filter(df,querystring)
        #Generate filtered dataframe which will be input for tab function
        exec (processedquery)
        #Filtered dataframe as per conditions specified in query element
        #print (newdf)
        #Tabulate on filtered dataframe
        tab.tabf(newdf,first_col,second_col)
    else:
        #tabulate directly when no query element in key
        tab.tabf(df, first_col, second_col)
json_data.close()
