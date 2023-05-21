size = 5
thisArray = [None for i in range(size)]
first = 0
last = -1
numberOfItems = 0

def Enqueue(item):
    global size, thisArray, first, last, numberOfItems

    if numberOfItems == size:
        print("Queue Full")
    else:
        last = last + 1
        if last == size:
            last = 0
        thisArray[last]  = item
        print("Item Added")
        numberOfItems = numberOfItems + 1

def Deuque():
    global size, thisArray, first, last, numberOfItems

    if numberOfItems == 0:
        print("No Items to Dequeue")

    else:
        item = thisArray[first]
        thisArray[first] = None
        print("Item Dequeued:", item)
        numberOfItems = numberOfItems - 1

        first = first + 1
        if first == size:
            first = 0

print(thisArray)
Enqueue('A')
Enqueue('B')
Enqueue('C')
Enqueue('D')
Enqueue('E')
print(thisArray)
Deuque()
Deuque()
Deuque()
print(thisArray)
Enqueue('F')
Enqueue('G')
print(thisArray)
Deuque()
Deuque()
Deuque()

print(thisArray)







