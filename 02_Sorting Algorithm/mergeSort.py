def mergeSort(array):
    if len(array) > 1:

        mid = len(array)//2
        leftHalf = array[:mid]
        rightHalf = array[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i=j=k=0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                array[k] = leftHalf[i]
                i += 1

            else:
                array[k] = rightHalf[j]
                j += 1

            k += 1

        while i < len(leftHalf):
                array[k] = leftHalf[i]
                i += 1
                k += 1

        while j < len(rightHalf):
                array[k] = rightHalf[j]
                j += 1
                k += 1

data = [38,27,43,3,9,82,10]
print("Unsorted Array:", data)

mergeSort(data)

print("Sorted Array:",data)
