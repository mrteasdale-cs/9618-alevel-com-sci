#Question 3
QueueArray = [None for i in range(0,10)]
HeadPointer = 0
TailPointer = 0
NumberItems = 0

def enQueue(QueueArray, HeadPointer, TailPointer, NumberItems, DataToAdd):
  if NumberItems >= 10:
    return False, QueueArray, HeadPointer, TailPointer, NumberItems
  QueueArray[TailPointer] = DataToAdd
  if TailPointer >= 9:
    TailPointer = 0
  else:
    TailPointer = TailPointer + 1
  NumberItems = NumberItems + 1

  return True, QueueArray, HeadPointer, TailPointer, NumberItems

for i in range(0,11):
  inputStr = input("Enter a string: ")

  returnVal, QueueArray, HeadPointer, TailPointer, NumberItems \
    = enQueue(QueueArray, HeadPointer, TailPointer, NumberItems, inputStr)

  if returnVal == True:
    print("Successful")
  else:
    print("Failed")

  returnVal, QueueArray, HeadPointer, TailPointer, NumberItems \
    = deQueue(QueueArray, HeadPointer, TailPointer, NumberItems, inputStr)
print(QueueArray)

