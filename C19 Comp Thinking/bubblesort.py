# efficient sort using while loop O(n) efficiency
def bubbleEfficient(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swapped = True
    return arr

# double for loop sort 0(n2) efficiency
def bubbleForLoop(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

numbers = [97,65,34,78,99,1,23,21,5,8,100]
print(f" Using an efficient while loop - O(n): {bubbleEfficient(numbers)}")
print(f" Using a double for loop - O(n2): {bubbleForLoop(numbers)}")