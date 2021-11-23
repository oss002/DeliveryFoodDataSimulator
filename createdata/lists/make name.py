from bs4 import BeautifulSoup
import json
import random

html = open('namestats.html','r',encoding="UTF-8")
soup = BeautifulSoup(html,'html.parser')
nameList = soup.find_all('a')

firstname=[]
lastname = ["김","이","박","최","정","강","조","윤","장","임","한","오","서","신","권"]

names=[]

for row in nameList:
    name = row.get_text()
    if(len(name) < 3 and len(name) > 0) :
        firstname.append(name)
    
for i in range(0,len(firstname)) :
    for j in range(0,len(lastname)):
        names.append(lastname[j]+firstname[i])

random.shuffle(names)
outputFile = open("namelist.txt",'w');
for i in range(0,len(names)):
    outputFile.write(names[i]+"\n")
outputFile.close()

print("finished")
