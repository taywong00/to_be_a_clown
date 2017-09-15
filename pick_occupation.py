import csv
import random

occupation = { }
#Reads the given csv file
with open('occupations.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        #Building dictionary
        try:
            occupation[row[0]] = float(row[1])
        #Do nothing to strings that can not be turned to float (e.g. 'Percentage')
        except:
            pass

def rand_occ():
    while True:
        for occ in occupation:
        #print random.random()
        #print occupation[occ]*0.01
            if random.random() < (occupation[occ]*0.01):
                return occ
    


print rand_occ()
