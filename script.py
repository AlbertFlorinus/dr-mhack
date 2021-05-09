import pandas as pd
import numpy as np
df = pd.DataFrame({"here": [1,2,4], "now": [2,5,7], "for": [3,9,10]})
#print(df)

#a = df.iloc[:, 1:4]
#print(a)
#f = lambda x: round((x - 32) * (5/9))
#a.iloc[:,1:] = a.applymap(f)

#self.masker = (self.df['Date'] > self.start_date) & (self.df['Date'] <= self.end_date)
def krav(df):
    df = df.loc[df['here'] == 2]


start_date = pd.to_datetime("2016-05-25", format = '%Y-%m-%d')
end_date = pd.to_datetime("2016-06-2", format = '%Y-%m-%d')

p = end_date-start_date

#q = np.timedelta64(1,"D")

for i in range(1, 4):
    print(i)

#print(int(p/q))