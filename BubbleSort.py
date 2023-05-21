thisArray = [54,12,78,34,16,93]

def BubbleSort():
    Swap = True
    boundary = len(thisArray) -1 
    while Swap == True and boundary > 0:
        Swap = False
        for i in range(boundary):
            if thisArray[i] > thisArray[i+1]:
                temp = thisArray[i]
                thisArray[i] = thisArray[i+1]
                thisArray[i+1] = temp
                swap = True
        boundary -= 1

BubbleSort()
print(thisArray)
