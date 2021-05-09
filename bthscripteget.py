import pandas as pd
import io
import requests
import urllib.request
from tkinter.filedialog import askopenfilename
from io import StringIO
import ast
import json
print("starting")

"""
web_url = "https://cloud.timeedit.net/bth/web/sched1/ri1wbXXQ54ZZ9ZQmY20727Y7yQY9657Yn98QX61Q9Y74X3y.csv"
schema = requests.get(web_url).content
#print(schema)
print("NU RAD\n")
web_url = "https://cloud.timeedit.net/bth/web/sched1/ri1w7XXQ54ZZ9YQmY20727Y7y3Y9657Y498QX61Q9.csv"
schema = requests.get(web_url).content

    #print(json_file)
    #print(text[511171:542390])
    #print(text.find("var program_terms"))
    #print(where)
    #print(text[513042-10000:513042+1000])

"""

def bth_data():
    web_url = "https://www.bth.se/utbildning/program/"
    page = urllib.request.urlopen(web_url)
    text = page.read().decode("utf8")
    start = text.find("var program_json")
    end = text.find("var program_terms")
    json_file = text[start:end]
    list_start = json_file.find("[{")
    list_end = json_file.find("}]")
    json_file_trim = json_file[list_start:list_end+2]
    return json_file_trim

def make_dict(data):
    res = json.loads(data)
    return res

def search_for_identifier(identifier, container):
    if identifier not in container:
        print(-1)
        return 0
    else:
        st = identifier.find(container)
        print(st)
        return st

def sub_search(identifier, container):
    checker = 0
    for index, item in enumerate(container):
        if checker == 0:    
            print(index)
            print(container[index])
            print(type(container))
            if identifier in container[index]:
                print("here! index: ", index)
                print(item)
                checker += 1
                return index
    print("done")


def main():
    json_file_one = bth_data()
    print(json_file_one)
    print(type(json_file_one))
    json_listed = make_dict(json_file_one)
    #print(json_listed)
    a = sub_search("AI", json_listed)
    print("FIN")
    print(a)
    print("FINA")
    print(json_listed[a])
    #a = search_for_identifier("maskinteknik", json_listed)
main()
    #web_url = f"https://edu.bth.se/utbildning/utb_program.asp?PtKod={prog_id}h&lang=sv"
    #kurserna = requests.get(web_url)
    #search_for_identifier(target, json_file_one)

    #json_file_one = bth_data


#json_file_one = bth_data()
        

#web_url = "https://www.bth.se/utbildning/program/"
#web_url = "https://edu.bth.se/utbildning/utb_program.asp?PtKod=DVAMI20h&lang=sv"
#web_url = "https://www.bth.se/utbildning/program/dvami/?val=DVAMI20h"
#web_url = "https://www.bth.se/kurser/BA6YP/20211/"
#page = urllib.request.urlopen(web_url)
#text = page.read().decode("utf8")
#search_for("Programvaruutveckling", text)
#DAJ = search_for_identifier("maskininlärning", text)
#print(text[DAJ-100:DAJ+100])


"""
print(json_file_one[22596-100:22596+100])

print(type(json_file_one))
data_full = make_dict(json_file_one)
print(type(data_full))
print(len(data_full))
"""
#print(data_full[0])
#data_full = make_dict(json_file_one)
#data_full = make_dict(bth_data())
#print(data_full)
#print(type(data_full))
#target = input("ditt program (case sensitive): ")
#data_file = bth_data(target)
#print(data_file)


#know = data_to_list(data_file)
#print(len(know))
#print("hi")
def make_dict2(data):
    res = ast.literal_eval(data)
    return res


    
"""
a = str([{"ID":435,"skola":"BTH","level":"Grundnivå"},{"ID":827,"skola":"KTH","level":"Avancerad"}])
print(type(a))

haj = make_dict(a)
print(haj)
print(type(haj))
print(len(haj))

search_for("}", a)
print(a[1:50])
a = eval(a[1:50])
print(type(a))
print(a)
"""
def input_vec():
    #Formatterar till en lista [x, y, z]
    vec = input("Skriv din vektor på (x,y,z) på formen: x y z: ")
    vec = [dict(i) for i in vec.split()]
    return vec

#bth_data("maskininlärning")

"""

prog_id = input("Din programkod (ABCDE20h): ")
web_url = f"https://www.bth.se/utbildning/program/{prog_id[0:5].lower()}/?val={prog_id}"
kurserna = requests.get(web_url)
#kurslista = kurserna.find("hösttermin")
print(kurserna.headers)
a = urllib.request.urlopen(web_url)
b = a.read().decode("utf8")
c = b.find("Hösttermin 2024")
print(c)
print(b[550697-5000:550697+5000])
"""
#print(kurserna)
#print(kurserna.text)
#print(kurslista)

def read_calender(file_name):
    """Reads TimeEdit csv file"""
    df = pd.read_csv(file_name, header = 2, sep = ',')
    return df

def clean_calender(dataframe,program):
    """Remove some unused columns""" #Currently hardcoded
    dataframe = dataframe.drop(['Grupp','URL','Mitt namn','Kurs/program '], axis = 1)
    for row in dataframe['Text']:
        if program not in row:
            dataframe = dataframe[dataframe.Text != row]
    dataframe.fillna('', inplace=True)
    return dataframe

def creator():
    schemat = askopenfilename()
    df = read_calender(schemat)
    df = clean_calender(df, "DVAMI20h")
    print(df)