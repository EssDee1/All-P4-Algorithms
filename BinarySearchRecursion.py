SearchArray = [2,3,5,7,9,15]
itemSearch = int(input("Enter item to be searched: "))
Upper = len(SearchArray) - 1
Lower = 0

def BinarySearch(Upper, Lower):
    global SearchArray, itemSearch

    if Upper >= Lower:
        Mid = (Upper + Lower) // 2

        if SearchArray[Mid] == itemSearch:
            return Mid
        
        elif itemSearch < SearchArray[Mid]:
            return BinarySearch(Mid - 1, Lower)

        else:
            return BinarySearch(Upper, Mid + 1)

    return -1

print(BinarySearch(Upper, Lower))


