def insertion_sort(array):
    for i in range(1, len(array)):
        n = array[i]
        j = i - 1

        while j >= 0 and array[j] > n:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = n
    return array

def insertion_sort_decreasing(array):
    for i in range(1, len(array)):
        n = array[i]
        j = i - 1

        while j >= 0 and array[j] < n:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = n
    return array