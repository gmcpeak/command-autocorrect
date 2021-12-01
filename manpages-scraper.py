import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://manpages.ubuntu.com/manpages/focal/man1/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

links_pre = soup.find_all('pre')
full_links = []
for pre in links_pre:
    a = pre.find_all('a')
    full_links.append(a)
full_links = full_links[0]

clean_links = []
for l in full_links:
    temp = str(l).split("\"")
    idx = 0
    for element in temp:
        if 'href' in element:
            idx+=1
            break
        idx+=1
    clean_links.append(temp[idx])
#print(clean_links)

df = {'command': [], 'description': [], 'flags': []}
df = pd.DataFrame(data=df)

for link in clean_links:
    print(link)
    temp_url = url+link
    page = requests.get(temp_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    tableWrappers = soup.find("div", {"id" : "tableWrapper"})
    #print(tableWrappers)
    idx = 0
    try:
        children = tableWrappers.findChildren()
        found = False
        description = ''
        options = ''
        for child in children:
            if "DESCRIPTION" in child:
                found = True
                #print(description)
                decription = children[idx+1]
            if "OPTIONS" in child:
                options = children[idx+1]
                #print(options)
            idx+=1
        if found:
            df = df.append({'command': link, 'description': description, 'options': options}, ignore_index = True) 
    except:
        print("EXCEPTION!")
print(df)
df.to_csv('manpages-db.csv', index=False)