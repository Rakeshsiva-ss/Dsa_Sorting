def selection_sort(arr):
    for i in range(len(arr)):
        min_val = arr[i]
        minj = i
        for j in range(i+1,len(arr)):
            if arr[j] < min_val:
                minj = j
                min_val = arr[j]
        arr[minj],arr[i] = arr[i],arr[minj]

arr = [5,9,32,4,8,1]
print(arr)
selection_sort(arr)
print(arr)
