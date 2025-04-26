# Python program for finding an item in a linked list
# Populating the linked list

myLinkedList = [27, 19, 36, 42, 16, None, None, None]
myLinkedListPointers = [-1, 0, 1, 2, 3, 6, 7, 8, 9, -1]
startPointer = 4
heapStartPointer = 5
nullPointer = -1

# Defining the find function
def find(itemSearch):
    found = False
    itemPointer = startPointer

    while itemPointer != nullPointer and not found:
        if myLinkedList[itemPointer] == itemSearch:
            found = True
        else:
            itemPointer = myLinkedListPointers[itemPointer]

    return itemPointer


def insert(itemToAdd):
  global startPointer
  global heapStartPointer
  if heapStartPointer == nullPointer:#-1
    print("List is full")
  else:
    tempP = startPointer
    startPointer = heapStartPointer
    heapStartPointer = myLinkedListPointers[heapStartPointer]
    myLinkedList[startPointer] = itemToAdd
    myLinkedListPointers[startPointer] = tempP

def delete(itemDelete):
    global startPointer, heapStartPointer
    if startPointer == nullPointer:
        print("Linked List empty")
    else:
        index = startPointer

    while myLinkedList[index] != itemDelete and index != nullPointer:
        oldindex = index
        index = myLinkedListPointers[index]

    if index == nullPointer:
        print("Item ", itemDelete, " not found")
    else:
        myLinkedList[index] = None
        tempPointer = myLinkedListPointers[index]
        myLinkedListPointers[index] = heapStartPointer
        heapStartPointer = index
        myLinkedListPointers[oldindex] = tempPointer

def printList():
  for item in myLinkedList:
    print(item)