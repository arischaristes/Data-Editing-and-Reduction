import csv
import math
import datetime

trainingSet = []
trainingSetClassCol = []
condensingSet = []
condensingSetClassCol = []

trainingSetName = input("Enter name of normalized csv file ")

with open(trainingSetName + '.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)

    numCols = len(header)
    
    for line in csv_reader:                                                                         # Read csv file line by line
                                                                                                    # Store Attributes
        if not line:                                                                                # Store Class
            break

        row = []
        for i in range(0, numCols-1):
            row.append(float(line[i]))

        trainingSetClassCol.append(line[numCols-1])
        trainingSet.append(row)

print(datetime.datetime.now())

condensingSet.append(trainingSet[0])                                                                # Add 1st instance of Training Set to Condensing Set
condensingSetClassCol.append(trainingSetClassCol[0])                                                # Add 1st instance's Class
trainingSet.remove(trainingSet[0])                                                                  # Remove 1st instance from Training Set
trainingSetClassCol.remove(trainingSetClassCol[0])                                                  # Remove 1st instance's Class
trainingSetSize = len(trainingSet)

for i in range(0, trainingSetSize):
    eDist = []
    for j in range(0, len(condensingSet)):                                                          # Calculate and Store Euclidean Distance and instance's Class
        row = [round(math.dist(trainingSet[i], condensingSet[j]), 8), condensingSetClassCol[j]]
        eDist.append(row)

    eDist.sort(key = lambda dist: dist[0])                                                          # Sort list of Euclidean Distance's in ascending order  
        
    nearest_neighbor = eDist[0][1]                                                                  # Get 1st nearest neighbor
       
    if nearest_neighbor != trainingSetClassCol[i]:                                                  # If nearest neighbor's Class != from current instance's Class
        condensingSet.append(trainingSet[i])                                                        # Add current instance to Condensing Set
        condensingSetClassCol.append(trainingSetClassCol[i])

print(datetime.datetime.now())

for i in range(0, len(condensingSet)):
    condensingSet[i] += [condensingSetClassCol[i]]
        
with open('reduced set ' + trainingSetName + '.csv', 'w', newline='') as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerow(header)
    csv_writer.writerows(condensingSet)