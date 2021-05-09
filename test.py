import pandas as pd
#from tkinter.filedialog import askopenfilename
import numpy as np
import datetime

from os import path
from inspect import currentframe, getfile

cmd_folder = path.realpath(
    path.abspath(path.split(getfile(currentframe()))[0])) + '/'

class Weather():

    def __init__(self, start_date, end_date):

        #str to datetime, input av typ "2020-03-21"
        self.start_date = pd.to_datetime(start_date, format = '%Y-%m-%d')
        self.end_date = pd.to_datetime(end_date, format = '%Y-%m-%d')

        #self.df = pd.read_csv(askopenfilename())
        self.df = pd.read_csv(cmd_folder + 'austin_weather.csv')
        print(self.df.columns, "\n")

        #Date col from str to datetime obj
        self.df["Date"] = pd.to_datetime(self.df["Date"], format='%Y-%m-%d')

        #delar upp i intervall innan celciusconvertingen
        self.masker = (self.df['Date'] > self.start_date) & (self.df['Date'] <= self.end_date)
        self.df = self.df.loc[self.masker]

    def celcius_conv(self):
        
        f = lambda x: round((x - 32) * (5/9))

        #gör en kopia av date col, applymap strular annars.
        self.df1 = self.df.copy().iloc[:, 0]
        
        #Denna uppgift användar endast max, medel och lägsta temperatur utöver datum. dessa cols indexeras till df2.
        self.df2 = self.df.copy().iloc[:, 1:4]

        #konverterar från fahrenheit till celcius på dessa 3 kolumner i df2.
        self.df2 = self.df2.applymap(f)

        #sätter tillbaka date col
        self.df2["Date"] = self.df1

        self.df = self.df2.reindex(columns=['Date',"TempHighF","TempAvgF","TempLowF"])  
        

    def criterias(self, df, temp, active_time = "day"):

        #är avtagande ju längre ifrån startdatum man kommer, ska representera osäkerhet i väderprognos.
        conf = lambda x: 1-x*0.04

        #dict för att välja vilken temperaturdata som är mest relevant
        link = {"day": "TempHighF", "night": "TempLowF", "all_day": "TempAvgF"}

        #skapar en lista med delta(days) från startdatum.
        test = df.to_numpy()
        storer = []
        for i in range(0, len(test)):
            storer.append(i)

        #applicerar conf
        storer = [*map(conf, storer)]

        #osäkerthetskolumn
        df["acc"] = storer

        #väljer endast då datum i intervallet vars temperatur för datatypen överstiger lägsta accepterade.
        self.suggest = self.df.loc[ self.df[ link[active_time] ] > temp]


        #skapar en "score" kolumn. Ett sätt att vikta osäkerhet med väderprognos. 
        
        self.suggest["score"] = self.suggest[ link[active_time] ] * self.suggest["acc"] * 2


        #sorterar över score för respektive dag
        self.suggest = self.suggest.sort_values(by ='score', ascending = False)


def main():

    if input("Choose Date, (y/n): ").upper() == "Y":
        start_date = input("Startdatum i format '2017-06-21': ")
        end_date = input("Slutdatum: ")
    else:
        start_date = "2016-05-25"
        end_date = "2016-06-20"
    
    temp = int(input("Lägsta temperatur? "))
    

    inspo = Weather(start_date, end_date)

    #Denna borde inte vara en egen metod, tidsbrist...
    inspo.celcius_conv()

    inspo.criterias(inspo.df, temp)

    print(inspo.suggest.to_string(index=False))

    


if __name__ == "__main__":
    main()
