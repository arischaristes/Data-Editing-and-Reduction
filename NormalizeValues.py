import csv
import datetime

trainingSet = []                                                                                        
classCol = []                                                                                           
normalizedSet = []                                                                                      

trainingSetName = input("Enter name of csv file ")                                                      

with open(trainingSetName + '.csv', 'r') as csv_file:                                                   
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)                                                                           

    numCols = len(header)                                                                               
    
    for line in csv_reader:                                                                             # Read csv file line by line
                                                                                                        # Store Attributes
        if not line:                                                                                    # Store Class
            break

        row = []
        for i in range(0, numCols-1):                                                                   
            row.append(float(line[i]))

        classCol.append(line[numCols-1])                                                                
        trainingSet.append(row)                                                                         

trainingSetSize = len(trainingSet)                                                                      # Number of rows
col = []

for j in range(0, numCols-1):                                                                           # Create a list for each Column of the Data Set
    col = []                                                                                            
    for i in range(0, trainingSetSize):
        col.append(trainingSet[i][j])
    normalizedSet.append(col)

print(datetime.datetime.now())

for i in range(0, numCols-1):                                                                           # Normalize all Columns of the Data Set
    minValue = min(normalizedSet[i])
    maxValue = max(normalizedSet[i])
    for j in range(0, trainingSetSize):
        normalizedSet[i][j] = round((normalizedSet[i][j] - minValue) / (maxValue - minValue), 8)

print(datetime.datetime.now())

with open('normalized ' + trainingSetName + '.csv', 'w', newline='') as new_file:                       
    csv_writer = csv.writer(new_file)
    csv_writer.writerow(header)                                                                         

    for i in range(0, trainingSetSize):                                                                 
        row = []
        for j in range(0, numCols-1):
            row.append(normalizedSet[j][i])

        row += [classCol[i]]
        csv_writer.writerow(row)