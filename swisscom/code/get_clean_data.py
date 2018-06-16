import numpy as np
import pandas as pd

def get_clean_data(year) :
    """
    Retrieve the data corresponding to the 100 winners of a given year from an Excel file and do some cleaning of the data.
    """
    filename = '../data/WinnerStartups'+str(year)+'.xlsx'

    df = pd.read_excel(filename)
    #print(df.head())

    dfPart1 = df.loc[np.arange(0,df.shape[0],2),]
    #print(dfPart1.head())
    #print(dfPart1.shape)

    dfPart2 = df.loc[np.arange(1,df.shape[0],2),]
    #print(dfPart2['Startup'].head())

    dfPart2['Location'],dfPart2['Year']=dfPart2['Startup'].str.split(', ',1).str
    #print(dfPart2[['Location','Year']].head())

    dfPart1Temp = dfPart1.reset_index()
    #print(dfPart1Temp.head())

    dfPart2Temp = dfPart2.reset_index()
    #print(dfPart2Temp.head())

    dfClean = pd.DataFrame()
    for col in ['Rank','Startup','Description'] :
        dfClean[col] = dfPart1Temp[col]
    for col in ['Location','Year'] :
        dfClean[col] = dfPart2Temp[col]

    return dfClean
