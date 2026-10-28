# 퀵 정렬
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]

    left = []
    right = []

    for i in range(1,len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [7, 3, 5, 2, 9, 1, 4, 8]
print(quick_sort(arr))

# 퀵 정렬 2
def quick_sort(arr,start,end):
    if start >= end:
        return
    
    pivot = start
    i = start + 1
    j = end

    while i <= j:
        while i <= end and arr[i] <= arr[pivot]:
            i += 1
        
        while j > start and arr[j] >= arr[pivot]:
            j -= 1

        if i>j:
            arr[j], arr[pivot] = arr[pivot], arr[j]

        else:
            arr[i],arr[j] = arr[j], arr[i]

    quick_sort(arr, start, j-1)
    quick_sort(arr, j+1, end)

arr = [5,3,8,4,2,7,1,6]
quick_sort(arr,0,len(arr) - 1)
print(arr)

#  병합 정렬
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

def merge(left,right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        
    result.extend(left[i:])
    result.extend(left[j:])

    return result

arr = [27,10,12,20,25,13,15,22]

print(merge_sort(arr))

