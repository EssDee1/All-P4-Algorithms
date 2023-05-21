thisArray = [None for i in range(10)]
base = 0
top = -1
numberOfItems = 0
size = len(thisArray)

def Push(thisItem):
    global thisArray, base, top, size, numberOfItems

    if numberOfItems == size:
        print("Stack is Full")

    else:
        top = top + 1
        thisArray[top] = thisItem
        numberOfItems = numberOfItems + 1
        print("Added")

def Pop():
    global thisArray, top, base, size, numberOfItems

    if numberOfItems == 0:
        print("No Items to Pop")

    else:
        item = thisArray[top]
        thisArray[top] = None
        numberOfItems = numberOfItems - 1
        top = top - 1
        print("Item Popped:", item)


print(thisArray)
Push('A')
Push('B')
Push('D')
Push('F')
Push('F')
Push('F')
Push('F')
Push('F')
print(thisArray)
Pop()
Pop()
Pop()
Pop()
Pop()
Pop()
Pop()


print(thisArray)


