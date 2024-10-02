def bubble_sort(arr):
    length = len(arr)
    
    for i in range(length):
        swapped = False
        
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
            
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break

arr = []
size = int(input("Enter the number of elements: "))

print("Input the elements:")
for i in range(size):
    num = int(input())
    arr.append(num)

bubble_sort(arr)
print("Sorted array:", arr)
