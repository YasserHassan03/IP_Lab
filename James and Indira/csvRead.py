import csv

with open ('data.csv') as dat:
    next(dat)
    read=csv.reader(dat)  
    for row in read:
        print(row)

dat.close()