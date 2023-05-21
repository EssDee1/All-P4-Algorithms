thisArray = [4, 7, 2, 9, 0, 6, 1]

def BubbleSort():
    global thisArray

    boundary = len(thisArray) - 1
    isSorted = False
    while isSorted == False and boundary > 0:
        isSorted = True
        for i in range(boundary):
            if thisArray[i] > thisArray[i + 1]:
                temp = thisArray[i + 1]
                thisArray[i + 1] = thisArray[i]
                thisArray[i] = temp
                isSorted = False
        boundary = boundary - 1

BubbleSort()
print(thisArray)

def InsertionSort():
    global thisArray

    size = len(thisArray)
    for pointer in range(1, size):
        toSort = thisArray[pointer]
        current = pointer - 1

        while current > -1 and toSort < thisArray[current]:
            thisArray[current + 1] = thisArray[current]
            current = current -1

        position = current + 1
        thisArray[position] = toSort

InsertionSort()
print(thisArray)