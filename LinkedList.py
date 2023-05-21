class Node:
    def __init__(self):
        self.Data = ''
        self.Pointer = None

FreePointer = 0
StartPointer = 0
size = 10

def Initialise():
    global FreePointer, StartPointer, List

    FreePointer = 0
    StartPointer = None
    
    
    List = [Node() for i in range(size)]

    for i in range(size - 1):
        List[i].Pointer = i +1
        
    List[size-1].Pointer = None
            
def InsertNode(item):
    global List, FreePointer, StartPointer

    #check if space
    
    if FreePointer is not None:
        NewNodePointer = FreePointer
        List[NewNodePointer].Data = item
        FreePointer = List[NewNodePointer].Pointer

        #insertion:

        ThisPointer = StartPointer
        PrevPointer = None

        #update ThisPointer and Remeber PreviousPointer
        while ThisPointer != None and List[ThisPointer].Data < item:
            PrevPointer = ThisPointer
            ThisPointer = List[ThisPointer].Pointer

        #start Pointer ma value rakhne ho bhane
        if ThisPointer == StartPointer:
            List[NewNodePointer].Pointer = StartPointer
            StartPointer = NewNodePointer

        #put value between previousNodePointer and NewNodePointer
        else:
            List[NewNodePointer].Pointer = List[PrevPointer].Pointer
            List[PrevPointer].Pointer = NewNodePointer
            
def FindItem(item):
    global List, FreePointer, StartPointer

    ThisPointer = StartPointer

    while ThisPointer is not None and List[ThisPointer].Data != item:
        ThisPointer = List[ThisPointer].Pointer

    return ThisPointer

def DeleteNode(item):
    global List, FreePointer, StartPointer

    #start from the startPointer
    ThisPointer = StartPointer
    PrevPointer = None

    #updata ThisPointer and remember Prev Pointer
    while ThisPointer is not None and List[ThisPointer].Data != item:
        PrevPointer = ThisPointer
        ThisPointer = List[ThisPointer].Pointer

    #if not the end of the list 
    if ThisPointer is not None:

        #if First Value
        if ThisPointer  == StartPointer:
            StartPointer = List[StartPointer].Pointer
        else:
            List[PrevPointer].Pointer = List[ThisPointer].Pointer

        #Exclude the data from the List and Update FreeList
        List[ThisPointer].Pointer = FreePointer
        FreePointer = ThisPointer

        

def Display():
    global FreePointer, StartPoiner, List
    for i in range(size):
        print(f"{i} || {List[i].Data} || {List[i].Pointer}")



Initialise()
Display()
InsertNode('B')
InsertNode('D')
InsertNode('C')
InsertNode('A')
print(FreePointer)
print(StartPointer)
Display()

DeleteNode('C')
DeleteNode('A')
print(FreePointer)
print(StartPointer)
Display()
print(FindItem('D'))



    
