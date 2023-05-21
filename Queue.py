thisQueue = [0 for i in range(10)]
itemCount = 0
front = 0
end = -1

def enqueue(item):
    global thisQueue, itemCount, front, end
    
    if itemCount == len(thisQueue):
        print("Queue Full")
    else:
        end = end + 1
        if end < len(thisQueue):
            thisQueue[end] = item
        else:
            end = 0
            thisQueue[end] = item
        itemCount = itemCount + 1

def dequeue():
    global thisQueue, itemCount, front, end

    if itemCount == 0:
        print("No Items To Dequeue")
    else:
        item = thisQueue[front]
        print(item)
        thisQueue[front] = 0
        itemCount -= 1
        front = front + 1
        if front >= len(thisQueue):
            front = 0

enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)
enqueue(6)
enqueue(7)
enqueue(8)
enqueue(9)
enqueue(10)

dequeue()
dequeue()
dequeue()
dequeue()
dequeue()

enqueue(11)
enqueue(12)

dequeue()

print(thisQueue)
    
