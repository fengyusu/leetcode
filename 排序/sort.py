import math

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i] > arr[j]):
                arr[i],arr[j] = arr[j],arr[i]

def insertSort0(arr):
    for i in range(1,len(arr)):
        tmp = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j] <= tmp:
                arr[j+1] = tmp
                break
            else:
                arr[j+1] = arr[j]
                if j == 0:
                    arr[0] = tmp


def insertSort(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        pre = i-1
        while pre >= 0 and arr[pre] > current:
            arr[pre+1] = arr[pre]
            pre -= 1
        arr[pre+1] = current
    return arr

def shellSort(arr):
    d = len(arr)//2
    while d >= 1:
        for i in range(d, len(arr)):
            pre = i-d
            current = arr[i]
            while pre >= 0 and arr[pre] > current:
                arr[pre+d] = arr[pre]
                pre -= d
            arr[pre+d] = current
        d //= 2
    return arr

def selectSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if(min_index != i):
            arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr


def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]

def heapify(arr, i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < arr_len and arr[left] > arr[largest]:
        largest = left
    if right < arr_len and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        swap(arr, largest, i)
        heapify(arr, largest)

def buildMaxHeap(arr):
    for i in range(arr_len // 2, -1, -1):
        heapify(arr, i)

def heapSort(arr):
    global arr_len
    arr_len = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1, 0, -1):
        swap(arr, 0, i)
        arr_len -= 1
        heapify(arr, 0)
    return arr


def merge(left,right):
    result = []
    while left and right:
        if(left[0] <= right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

def mergeSort(arr):
    if(len(arr) < 2):
        return arr
    middle = len(arr) // 2
    left,right = arr[0:middle],arr[middle:]
    return merge(mergeSort(left),mergeSort(right))

def partition(arr, left, right):
    pivot = arr[left]
    while left < right:
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]
    arr[left] = pivot
    return left

def quickSort(arr, left = None, right = None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr)-1 if not isinstance(right, (int, float)) else right

    if(left < right):
        pivot = partition(arr, left, right)
        quickSort(arr, left, pivot-1)
        quickSort(arr, pivot+1, right)
    return arr





def test():
    arr = [3,5,1,8,0,2,9,6,7,4]
    print(arr)
    bubbleSort(arr)
    print(arr)

if __name__ == '__main__':
    test()
