thisStack = [0 for i in range(10)]
base = 0
top = -1
noOfItem = 0

def Push(item):
    global noOfItem,thisStack, base, top
    
    if noOfItem == len(thisStack):
        print("Stack Full")
    else:
        top = top + 1
        thisStack[top] = item
        noOfItem = noOfItem + 1

def Pop():
    global thisStack, base, top, noOfItem

    if noOfItem == 0:
        print("No items to pop")
    else:
        item = thisStack[top]
        thisStack[top] = 0
        top = top - 1
        noOfItem = noOfItem - 1
        return item


Pop()
Pop()
Pop()
Pop()

print(thisStack)


