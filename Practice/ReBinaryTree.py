class BinaryNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

freePointer = None
rootPointer = None
thisTree = []
size = 10

def CreateTree():
    global freePointer,rootPointer, thisTree, size

    thisTree = [BinaryNode() for i in range(size)]
    freePointer = 0
    rootPointer = None

    for i in range(size - 1):
        thisTree[i].left = i + 1

    thisTree[size - 1].left = None

def AddItem(thisItem):
    global freePointer, rootPointer, thisTree, size
    isTurnedLeft = True

    if freePointer is not None:
        newNodePointer = freePointer
        thisTree[newNodePointer].data = thisItem
        freePointer = thisTree[freePointer].left
        thisTree[newNodePointer].left = None
        thisTree[newNodePointer].right = None


        if rootPointer is None:
            rootPointer = newNodePointer

        else:
            thisPointer = rootPointer
            prevPointer = None

            while thisPointer is not None:
                prevPointer = thisPointer
                if thisItem < thisTree[thisPointer].data:
                    isTurnedLeft = True
                    thisPointer = thisTree[thisPointer].left
                else:
                    isTurnedLeft = False
                    thisPointer = thisTree[thisPointer].right

            if isTurnedLeft:
                thisTree[prevPointer].left = newNodePointer
            else:
                thisTree[prevPointer].right = newNodePointer

def TraverseTree(startNode):
    global thisTree, freePointer, rootPointer, size

    if thisTree[startNode].left is not None:
        TraverseTree(thisTree[startNode].left)
    print(str(thisTree[startNode].data))
    if thisTree[startNode].right is not None:
        TraverseTree(thisTree[startNode].right)


def PrintDetails():
    global rootPointer, freePointer, thisTree, size

    print("Root Pointer", rootPointer)
    print("Free Pointer", freePointer)
    print("Index", "Left", "Data", "Right")

    for index in range(size):
        print(index, thisTree[index].left, thisTree[index].data, thisTree[index].right)

CreateTree()
PrintDetails()
AddItem('L')
AddItem('Z')
AddItem('D')
AddItem('B')
AddItem('P')
AddItem('M')
AddItem('R')
PrintDetails()
TraverseTree(rootPointer)