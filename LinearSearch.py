global ThisArray
ThisArray = [4,5,2,8,7,1]

def LinearSearch(item):
    found = False
    index = 0
    while found == False and index < len(ThisArray):
        if item == ThisArray[index]:
            return index
        index += 1

print(LinearSearch(7))
