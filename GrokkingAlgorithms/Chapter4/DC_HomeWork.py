arr = [1,5,6,2,4,7,0]
def sum(arr):
    total = 0
    while arr:
        ele = arr.pop()
        total = ele + sum(arr)
    return total

def numbers(arr):
    size = 0
    while arr:
        arr.pop()
        size +=1
    return size

def findMax(arr):
    maxIndex = 0
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
            maxIndex = i
    return max

def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
