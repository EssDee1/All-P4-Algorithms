ThisArray = [2,3,5,7,8,9]


def BinarySearch(item):
    location = -1
    lowerIndex = 0
    upperIndex = len(ThisArray)-1
    found = False
    while found == False and upperIndex >= lowerIndex:
        midIndex = int((lowerIndex + upperIndex)/2)
        if item == ThisArray[midIndex]:
            location = midIndex
            found = True
        if item < ThisArray[midIndex]:
            upperIndex = midIndex - 1
        if item > ThisArray[midIndex]:
            lowerIndex = midIndex + 1

    return location

print(BinarySearch(9))


    
        
