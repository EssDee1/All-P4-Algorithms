thisArray = [2, 4, 7, 9, 10, 14, 20]

def BinarySearch(toSearch):
    global thisArray

    upper = len(thisArray) - 1
    lower = 0
    isFound = False
    index = -1

    while isFound == False and upper >= lower:
        mid = int((upper + lower) / 2)

        if thisArray[mid] == toSearch:
            index = mid
            isFound = True
        elif toSearch < thisArray[mid]:
            upper = mid - 1
        else:
            lower = mid + 1

    return index

print(BinarySearch(13))


def RecursiveBinarySearch(toSearch, upper, lower):
    global thisArray

    if upper >= lower:
        mid = int((upper+lower)/2)

        if toSearch == thisArray[mid]:
            return mid

        elif toSearch < thisArray[mid]:
            return RecursiveBinarySearch(toSearch, mid -1, lower)

        else:
            return RecursiveBinarySearch(toSearch, upper, mid + 1)

    return -1

upper = len(thisArray) - 1
lower = 0

print(RecursiveBinarySearch(14, upper, lower))


