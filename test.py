import pandas as pd
from tkinter.filedialog import askopenfilename
import numpy as np
import datetime
import math

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
        

    def criterias(self, df, temp, active_time = "day"):

        conf = lambda x: 1-x*0.04

        link = {"day": "TempHighF", "night": "TempLowF", "all_day": "TempAvgF"}

        test = df.to_numpy()
    
        storer = []
  
        for i in range(0, len(test)):
            storer.append(i)

        storer = [*map(conf, storer)]

        df["acc"] = storer

        self.suggest = self.df.loc[ self.df[ link[active_time] ] > temp]

        self.suggest["score"] = (self.suggest[ link[active_time] ]   ) * self.suggest["acc"] * 2

        self.suggest = self.suggest.sort_values(by ='score', ascending = False)




    

def main():
    inspo = Weather("2016-05-25", "2016-06-2")
    inspo.celcius_conv()
    inspo.criterias(inspo.df, 20)

    print(inspo.suggest)

if __name__ == "__main__":
    main()