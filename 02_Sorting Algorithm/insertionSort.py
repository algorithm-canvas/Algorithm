def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j>= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1

        array[j + 1] = key


data = [9,5,1,4,3]

print("Unsorted Array:")
print(data)

insertionSort(data)

print("Sorted Array:")
print(data)