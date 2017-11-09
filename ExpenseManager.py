# Sanity Checks:
# 1) The first column should be dish name
# 2) The second column  should be cost of the dish
# 3) The third column should be cost with tax
# 4) The names should be in the first row starting from column 3 onwards
# 5) The end of list should be Total

import csv


f = open('resources/expense.csv')
reader = csv.reader(f)

lineCounter = 0

totalExpenseList = []
tempShareList = []
names = []

for line in reader:
    if line[0] == 'Total':
        continue
    if lineCounter == 0:
        for name in line[3::]:
            names.append(name)
            totalExpenseList.append(0.0)
            tempShareList.append(0)
    else:
        totalDishCost = float(line[2])
        tempShareCounter = 0
        totalShare = 0
        for share in line[3::]:
            if share == '':
                intShare = 0
            else:
                intShare = int(share)
            tempShareList[tempShareCounter] = intShare
            totalShare += intShare
            tempShareCounter += 1
        for i in range(len(tempShareList)):
            totalExpenseList[i] += tempShareList[i] * totalDishCost / totalShare
    lineCounter += 1


totalCost=0
for i in range(len(names)):
    expense=round(totalExpenseList[i],2)
    print names[i] + ": " + str(expense)
    totalCost+=expense

print "Total: "+str(totalCost)
