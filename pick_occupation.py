#Team to_be_a_clown

import csv
import random

occupation = { }
#Reads the given csv file and closes when finished
with open('occupations.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        #Building dictionary
        try:
            #Don't want Total to be an option occupation
            if row[0] != "Total": 
                occupation[row[0]] = float(row[1])
        #Do nothing to strings that can not be turned to float (e.g. 'Percentage')
        except:
            pass

#Returns a random occupation based on percentages        
def rand_occ():
    while True:
        for occ in occupation:
            #If a random float between 0 and 1 is less than the percentage, then the corresponding occupation is returned 
            if random.random() < (occupation[occ]*0.01):
                return occ

#Testing
x = 100
while x >1:
    print randocc()
    x -=1
