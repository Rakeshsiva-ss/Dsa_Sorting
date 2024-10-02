def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]  
    middle = [x for x in arr if x == pivot]  
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


arr = []
n = int(input("Enter the number of elements: "))

print("Input the elements:")
for i in range(n):
    element = int(input())
    arr.append(element)

sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
