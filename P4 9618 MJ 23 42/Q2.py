class SaleData():
    def __init__(self, ID, Quantity):
        self.ID = ID
        self.Quantity = Quantity

# Global queue and pointers
CircularQueue = [SaleData("", -1) for i in range(5)]
Head = 0
Tail = 0
NumberOfItems = 0

def Enqueue(Record):
    global Head, Tail, NumberOfItems
    if NumberOfItems == 5:
        return -1
    else:
        CircularQueue[Tail] = Record
        Tail = (Tail + 1) % 5
        NumberOfItems += 1
        return 1

def Dequeue():
    global Head, Tail, NumberOfItems
    if NumberOfItems != 0:
        RecordRemove = CircularQueue[Head]
        CircularQueue[Head] = SaleData("", -1)  # Optional: clear slot
        Head = (Head + 1) % 5
        NumberOfItems -= 1
        return RecordRemove
    else:
        return None

def EnterRecord():
    Sales = []
    for i in range(0, 6):
        inputID = input("Enter ID: ")
        inputQuantity = int(input("Enter quantity: "))
        Sales.append([inputID, inputQuantity])
        result = Enqueue(SaleData(inputID, inputQuantity))
        if result == -1:
            print("Queue is full, dequeueing one element...")
            Dequeue()
            Enqueue(SaleData(inputID, inputQuantity))
        print(f"Current queue size: {NumberOfItems}")
    print("Sales entered:", Sales)
    print("Queue contents:")
    for i in range(5):
        print(f"Slot {i}: ID={CircularQueue[i].ID}, Quantity={CircularQueue[i].Quantity}")

EnterRecord()
