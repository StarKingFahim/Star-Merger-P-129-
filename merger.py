import csv
import pandas as pd

file1 = 'bright.csv'
file2 = 'bdwarf_stars.csv'

d1 = []
d2 = []
with open(file1,'r') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        d1.append(i)
        
with open(file2,'r') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]

planet_data1 = d1[1:]
planet_data2 = d2[1:]

h = h1+h2

planet_data =[]

for i in planet_data1:
    planet_data.append(i)
for j in planet_data2:
    planet_data.append(j)
with open("total_stars.csv",'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(planet_data)
    
df = pd.read_csv('total_stars.csv')