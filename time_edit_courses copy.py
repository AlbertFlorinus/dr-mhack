import urllib.request
import requests
from tkinter.filedialog import askopenfilename
import json
from bs4 import BeautifulSoup

print("starting...\n")

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

def sub_search2(identifier, start_year, container):
    for index, item in enumerate(container):
        if identifier in item["title"] and start_year[2:] in item["term"]:
            print("here! index: ", index)
            return item

def sub_search(identifier, start_year, container):
    for item in container:
        if identifier in item["title"] and start_year[2:] in item["term"]:
            return item


def main3():
    json_file_one = bth_data()
    json_listed = make_dict(json_file_one)
    
    json_found = sub_search("maskininlärning", "2020", json_listed)
    prog_codeid_locate = json_found["url"].index("?val=")
    print(prog_codeid_locate)

    prog_id = json_found["url"][prog_codeid_locate+5:prog_codeid_locate+13]
    print(prog_id)
    web_url_next = f"https://edu.bth.se/utbildning/utb_program.asp?PtKod={prog_id}&lang=sv"
    #print(web_url_next)
    kurserna = requests.get(web_url_next)

    soup = BeautifulSoup(kurserna.content, "html.parser")
    kurs_fix = []
    for header in soup.find_all('div', class_ = 'utb_dragspel_kurser_content'):
        test = header.find('a', class_= 'arrowlink')['href']
        kurs_fix.append(test)
        print(test)
        print(type(test))
    print("NEXT LEVEL NOW \n")
    k = 0
    for i in kurs_fix:
        if k < 4:
            r = requests.get(f"https://edu.bth.se/utbildning/{i}")
            soup = BeautifulSoup(r.content, "html.parser")
            k += 1
            for header in soup.find_all('div', class_ = 'utb_faktaspalt_text'):
                test = header.find('a', class_= 'newwindow')['href']
                print(test)       
#main()


def sub_search8(identifier, container):
    for item in container:
        if identifier in item["title"]:
            return item

def main():
    json_file_one = bth_data()
    #print(json_file_one)
    json_listed = make_dict(json_file_one)
    json_found = sub_search8("maskininlärning", json_listed)
    #print(json_found)
    prog_codeid_locate = json_found["url"].index("?val=")
    #print(prog_codeid_locate)

    prog_id = json_found["url"][prog_codeid_locate+5:prog_codeid_locate+10]
    start_year = "2020"
    prog_id += start_year[2:]+"h"
    print(prog_id)
    web_url_next = f"https://edu.bth.se/utbildning/utb_program.asp?PtKod={prog_id}&lang=sv"
    print(web_url_next)
    #kurserna = requests.get(web_url_next)
    kurserna = requests.get(web_url_next)

    soup = BeautifulSoup(kurserna.content, "html.parser")
    kurs_fix = []
    for header in soup.find_all('div', class_ = 'utb_dragspel_kurser_content'):
        test = header.find('a', class_= 'arrowlink')['href']
        #test = header.find("a", class_="arrowlink", href=True)
        kurs_fix.append(test)
        print(test)
        print(type(test))
    print("NEXT LEVEL NOW \n")
    k = 0
    all_kurs = []
    #33 34 35
    print(kurs_fix,"\n")
    print(len(kurs_fix))
    for i in kurs_fix:
        
        if k < 50:
            r = requests.get(f"https://edu.bth.se/utbildning/{i}")
            soup = BeautifulSoup(r.content, "html.parser")
            k += 1
            for header in soup.find_all('div', class_ = 'utb_faktaspalt_text'):
                #test = header.find('a', class_= 'newwindow', href = True)
                test = header.find('a', class_= 'newwindow')
                if test != None:
                    all_kurs.append(test)
    #print(all_kurs)
    uniques = set(all_kurs)
    print(uniques)
    print(len(uniques))
    for i in uniques:
        print(i)
    
#main()

#https://edu.bth.se/utbildningsplaner/DVAMI_ht-20.pdf

def bth_data3():
    #kurslista = kurserna.find("hösttermin")
    #print(kurserna.text)
    kurserna = requests.get("https://edu.bth.se/utbildningsplaner/DVAMI_ht-20.pdf")
    #location = kurserna.text.index("vårterminen 2021")
    #print(location)
    #print(kurserna.text[13539:13539+300])
    ContentUrl = json.dumps(kurserna.text)
    print("TYP\n")
    print(type(ContentUrl))
    print(ContentUrl)
    contenta = json.loads(ContentUrl)
    print("NU\n")
    print(type(contenta))
    print(contenta)

def bth_data2():
    web_url = "https://edu.bth.se/utbildningsplaner/DVAMI_ht-20.pdf"
    page = urllib.request.urlopen(web_url)
    text = page.read().decode("utf8")
    print(text)
    """
    start = text.find("var program_json")
    end = text.find("var program_terms")
    json_file = text[start:end]
    list_start = json_file.find("[{")
    list_end = json_file.find("}]")
    json_file_trim = json_file[list_start:list_end+2]
    return json_file_trim"""
# bth_data3()


"""
fd = open("latest.pdf","rb")
viewer = SimplePDFViewer(fd)
viewer.navigate(12)
viewer.render()
markdown = viewer.canvas.text_content
"""
"""
#web_url = requests.get("https://edu.bth.se/utbildning/utb_kurstillfalle.asp?KtTermin=20211&KtAnmKod=BNJ67&lang=sv&parentPtKod=DVAMI20h")
web_url = requests.get("https://edu.bth.se/utbildning/utb_kurstillfalle.asp?KtTermin=20202&KtAnmKod=B7643&lang=sv&parentPtKod=DVADS19h")
soup = BeautifulSoup(web_url.content, "html.parser")
#print(soup)
kurs_fix = []
for header in soup.find_all("div", class_ = "utb_faktaspalt_text"):
    #print(header)
    test = header.find("a", class_="newwindow", href = True)
    if test != None:
        kurs_fix.append(test)
#print(row)
hurt = str(kurs_fix[0])
print(type(hurt))
print(hurt)
print(hurt.index("kurskod"))
print(hurt[hurt.index("kurskod")+8:hurt.index("kurskod")+1])
#FOUNDED = kurs_fix[0].index("KURSKOD")
"""