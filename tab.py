import pandas as pd
def tabf(df,firstcol,secondcol):
    #If no second column, carry out one-way tabulate
    if (secondcol == ""):
        #All unique elements of column with frequency counts
        valuecounts=df[firstcol].value_counts()
        total=0
        perc = []
        cumul = []
        #Calulate totals for percentage and calculate cumulative for each item
        for i in range(0,len(valuecounts)):
            total=total+valuecounts[i]
            cumul.append(total)
            i=i+1;
        #Caculate percentage of total for each item
        for i in range(0,len(valuecounts)):
            perc.append(round(((valuecounts[i]/total)*100),2))
        #Merge lists to one dataframe
        df1= pd.DataFrame({'frequency':valuecounts,'cumulative':cumul,'percentage':perc})
        df1.index.names=['values']
        #Append dataframe to csv file
        f1=open("output.csv","a")
        df1[['frequency','cumulative','percentage']].to_csv(f1,mode='a',header=True)
        f1.close()
    else:
        #Two-way Tabulate
        #Perform two-way tabulate
        df2=df.groupby([firstcol,secondcol])[secondcol].count().unstack()
        #Change default NaN values to N/A
        df2 = df2.where((pd.notnull(df2)), "N/A")
        #Format dataframe for csv output
        df2.insert(0,'value',df2.index)
        #Append dataframe to csv file
        f2=open("output.csv","a")
        df2.to_csv(f2,mode='a',index=False)
        f2.close()
        #print(df2)