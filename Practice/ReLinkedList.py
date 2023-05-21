class Node:
    def __init__(self):
        self.data = None
        self.pointer = None


freePointer = None
startPointer = None
size = 10
thisList = []


def CreateLinkedList():
    global freePointer, startPointer, size, thisList

    thisList = [Node() for i in range(size)]
    freePointer = 0
    startPointer = None

    for i in range(size - 1):
        thisList[i].pointer = i + 1

    thisList[size - 1].pointer = None


def AddItem(thisItem):
    global freePointer, startPointer, size, thisList

    if freePointer is not None:
        newNodePointer = freePointer
        freePointer = thisList[freePointer].pointer
        thisList[newNodePointer].data = thisItem

        thisPointer = startPointer
        prevPointer = None

        while thisPointer is not None and thisList[thisPointer].data < thisItem:
            prevPointer = thisPointer
            thisPointer = thisList[thisPointer].pointer

        if thisPointer == startPointer:
            thisList[newNodePointer].pointer = startPointer
            startPointer = newNodePointer

        else:
            thisList[newNodePointer].pointer = thisList[prevPointer].pointer
            thisList[prevPointer].pointer = newNodePointer

def DeleteItem(thisItem):
    global freePointer, startPointer, size, thisList

    thisPointer = startPointer
    prevPointer = None

    while thisPointer is not None and thisList[thisPointer].data != thisItem:
        prevPointer = thisPointer
        thisPointer = thisList[thisPointer].pointer

    if thisPointer == startPointer:
        startPointer = thisList[thisPointer].pointer
    else:
        thisList[prevPointer].pointer = thisList[thisPointer].pointer

    thisList[thisPointer].data = None
    thisList[thisPointer].pointer = freePointer
    freePointer = thisPointer


def PrintDetails():
    global freePointer, startPointer, thisList, size

    print("Free Pointer", freePointer)
    print("Start Pointer", startPointer)
    print("Index", "Data", "Pointer")
    for i in range(size):
        print(i, thisList[i].data, thisList[i].pointer)

CreateLinkedList()
PrintDetails()
AddItem('B')
AddItem('D')
AddItem('C')
AddItem('A')
PrintDetails()
DeleteItem('C')
PrintDetails()
