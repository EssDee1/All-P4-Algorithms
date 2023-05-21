#initialisation
size = 10
HashTable = [None for i in range(10)]

##class Record:
##    def __init__(self, Key, Data = None):
##        self.Key = Key
##        self.Data = Data        
        

#Hashing Function 
def Hash(Key):
    Address = Key%size
    return Address


def Insert(NewRecord):
    global HashTable, size
    
    #find where to put the record
    
    Index = Hash(NewRecord)

    #if space already occupied
    while HashTable[Index] is not None:
        Index = Index + 1
        if Index == size: #wrap around
            Index = 0

    #if some space finally found
    HashTable[Index] = NewRecord


def FindRecord(SearchKey):
    Index = Hash(SearchKey)

    while HashTable[Index] != SearchKey and HashTable[Index] is not None:
        Index = Index + 1
        if Index == size:
            Index = 0

    if HashTable[Index] is not None:
        return Index
    

 
Insert(423)
Insert(342)
Insert(2112)


print(HashTable)
print()

print(FindRecord(342))








    
