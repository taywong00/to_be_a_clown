#Team to_be_a_clown

import csv
import random

occupation = { }
#Reads the given csv file and closes when finished
with open('occupations.csv', 'r') as f:
    reader = csv.reader(f)
    previous = 0
    for row in reader:
        #Building dictionary
        try:
            #Removes Total as an option occupation
            if row[0] != "Total":
                occupation[row[0]] = float(row[1]) + previous
                previous = occupation[row[0]]
        #Do nothing to strings that can not be turned to float (e.g. 'Percentage')
        except:
            pass
    #Reassurance against a non-100 total by resizing all percentages to make the total 100
    for occ in occupation:
        occupation[occ] /= previous

#Returns a random occupation based on percentages        
def rand_occ():
    rand = random.random()
    smallest = 1.1 #smallest occupation percentage bigger than rand
    desired = None
    #Finds the smallest percentage larger than the random number generated
    for occ in occupation:
        if rand < occupation[occ] < smallest:
            desired = occ
            smallest = occupation[occ]
    return desired

#Testing x100
for x in range(100):
    print rand_occ()
