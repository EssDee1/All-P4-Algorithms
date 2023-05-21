thisArray = [1,2,3,5,6,7,8,9,10,-1] #len9
inputNumber = 4                 #4

def InsertElement(inputNumber):
    global thisArray
    
    upper = len(thisArray) - 1
    thisArray[upper] = inputNumber
    current = upper - 1

    while current > -1 and inputNumber < thisArray[current]:
        thisArray[current + 1] = thisArray[current]
        current = current - 1
    
    thisArray[current + 1] = inputNumber

InsertElement(inputNumber)
print(thisArray)



