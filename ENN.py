import csv
import math
from statistics import mode
import datetime

trainingSet = []
trainingSetClassCol = []
editedSet = []

trainingSetName = input("Enter name of normalized csv file ")                                               
k = input("Enter k ")
k = int(k)

with open(trainingSetName + '.csv', 'r') as csv_file:                                                       
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)                                                                               

    numCols = len(header)                                                                                   
    
    for line in csv_reader:                                                                             # Read csv file line by line
                                                                                                        # Store Attributes
        if not line:                                                                                    # Store Class
            break                                                                                       # Store Attributes and Class in Edited Set

        row = []
        for i in range(0, numCols-1):
            row.append(float(line[i]))

        trainingSetClassCol.append(line[numCols-1])
        trainingSet.append(row)
        new = row + [line[numCols-1]]
        editedSet.append(new)

trainingSetSize = len(trainingSet)

print(datetime.datetime.now())

for i in range(0, trainingSetSize):
    eDist = []
    nearest_neighbors = []
    for j in range(0, trainingSetSize):
        if i == j:                                                                                      # Case where instance is compared with itself
            continue
        else:                                                                                           # Calculate and Store Euclidean Distance and instance's Class
            row = [round(math.dist(trainingSet[i], trainingSet[j]), 8), trainingSetClassCol[j]]
            eDist.append(row)

    eDist.sort(key = lambda dist: dist[0])                                                              # Sort list of Euclidean Distance's in ascending order
        
    for m in range(0, k):                                                                               # Add first k nearest neighbors
        nearest_neighbors.append(eDist[m][1])

    major_class = mode(nearest_neighbors)                                                               # Get most common Class between k nearest neighbors

    if major_class != trainingSetClassCol[i]:                                                           # If most common Class != from current instance's Class
        value = trainingSet[i] + [trainingSetClassCol[i]]                                               # Remove current instance from Edited Set
        editedSet.remove(value)

print(datetime.datetime.now())
        
with open('edited set ' + trainingSetName +" k=" + str(k) + '.csv', 'w', newline='') as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerow(header)
    csv_writer.writerows(editedSet)