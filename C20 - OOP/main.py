import linkedList
from graph import display

def graph():




def linkedList():

    linkedList.printList()
    # Enter item to search for
    item = int(input("Please enter item to be found: "))
    result = linkedList.find(item)

    if result != -1:
        print(f"Item found at {result + 1}")
    else:
        print("Item not found")

    linkedList.printList()
    linkedList.delete(27) #delete 27 from list
    linkedList.printList()

if __name__ == '__main__':
    linkedList()
