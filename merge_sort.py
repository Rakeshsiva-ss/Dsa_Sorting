def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

arr = []
size = int(input("Enter the number of elements: "))

print("Enter the elements:")
for _ in range(size):
    arr.append(int(input()))

sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
