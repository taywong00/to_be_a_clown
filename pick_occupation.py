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
    #If a random float between 0 and 1 is less than the percentage, then the corresponding occupation is returned 
    rand = random.random()
    for occ in occupation:
        if occupation[occ] > rand:
            return occ

#Testing
for x in range(100):
    print(rand_occ())
