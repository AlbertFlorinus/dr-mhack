import pandas as pd
df = pd.DataFrame({"here": [1,2,4], "now": [2,5,7], "for": [3,9,10]})
print(df)

a = df.iloc[:, 1:4]
print(a)
f = lambda x: round((x - 32) * (5/9))
a.iloc[:,1:] = a.applymap(f)
#a = a.applymap(f)
#df2[[df2["TempHighF"]].applymap(lambda x: x*2)]
print("\n")
print(a)