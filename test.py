import pandas as pd
from tkinter.filedialog import askopenfilename
import numpy as np
import datetime

class Weather():
    def __init__(self, start_date, end_date):
        self.start_date = pd.to_datetime(start_date, format = '%Y-%m-%d')
        self.end_date = pd.to_datetime(end_date, format = '%Y-%m-%d')
        self.df = pd.read_csv(askopenfilename())
        self.df["Date"] = pd.to_datetime(self.df["Date"], format='%Y-%m-%d')
        self.masker = (self.df['Date'] > self.start_date) & (self.df['Date'] <= self.end_date)
        self.df = self.df.loc[self.masker]

    def celcius_conv(self):
        f = lambda x: round((x - 32) * (5/9))
        self.df1 = self.df.copy().iloc[:, 0]
        self.df2 = self.df.copy().iloc[:, 1:4]
        self.df2 = self.df2.applymap(f)
        self.df2["Date"] = self.df1
        self.df = self.df2.reindex(columns=['Date',"TempHighF","TempAvgF","TempLowF"])

    

def main():
    #start_date = pd.to_datetime("2014-02-23", format = '%Y-%m-%d')
    #end_date = pd.to_datetime("2014-03-1", format = '%Y-%m-%d')
    abbe = Weather("2014-02-23", "2014-03-2")
    abbe.celcius_conv()
    print(abbe.df)

if __name__ == "__main__":
    main()