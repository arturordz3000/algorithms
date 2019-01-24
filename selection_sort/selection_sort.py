def selection_sort(array):
    for i in range(0, len(array) - 1):
        pivotIndex = i

        for j in range(i + 1, len(array)):
            if (array[j] < array[pivotIndex]):
                pivotIndex = j
        
        temp = array[i]
        array[i] = array[pivotIndex]
        array[pivotIndex] = temp

    return array

def selection_sort_decreasing(array):
    for i in range(0, len(array) - 1):
        pivotIndex = i

        for j in range(i + 1, len(array)):
            if (array[j] > array[pivotIndex]):
                pivotIndex = j
        
        temp = array[i]
        array[i] = array[pivotIndex]
        array[pivotIndex] = temp

    return array