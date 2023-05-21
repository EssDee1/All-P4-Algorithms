thisArray = [3,6,2,9,1,4]

def InsertionSort():
    global thisArray
    lowerBound = 0
    upperBound = len(thisArray) - 1

    for i in range(lowerBound + 1, upperBound + 1): #because python doesn't take the last index
        toSort = i
        while thisArray[toSort] < thisArray[toSort-1] and toSort > lowerBound:
                thisArray[toSort], thisArray[toSort-1] = thisArray[toSort-1], thisArray[toSort]
                toSort -= 1


print(thisArray)


def BookKoInsertionSort():
    global thisArray
    for pointer in range(1, len(thisArray)):
        ItemToInsert = thisArray[pointer]
        current = pointer - 1

        while ItemToInsert < thisArray[current] and current > -1:
            thisArray[current + 1] = thisArray[current]
            current = current - 1

        thisArray[current + 1] = ItemToInsert

BookKoInsertionSort()
print(thisArray)

                
