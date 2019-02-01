import math

def merge(a1, a2):
    i = 0
    j = 0
    a = []

    while i < len(a1) or j < len(a2):
        if i >= len(a1):
            a.append(a2[j])
            j += 1
            continue
        elif j >= len(a2):
            a.append(a1[i])
            i += 1
            continue

        if (a1[i] <= a2[j]):
            a.append(a1[i])
            i += 1
        else:
            a.append(a2[j])
            j += 1
    
    return a

def merge_decreasing(a1, a2):
    i = 0
    j = 0
    a = []

    while i < len(a1) or j < len(a2):
        if i >= len(a1):
            a.append(a2[j])
            j += 1
            continue
        elif j >= len(a2):
            a.append(a1[i])
            i += 1
            continue

        if (a1[i] >= a2[j]):
            a.append(a1[i])
            i += 1
        else:
            a.append(a2[j])
            j += 1
    
    return a

def merge_sort_recursive(array, startIndex, endIndex, decreasing = False):
    if endIndex == startIndex:
        if startIndex < len(array):
            return [array[startIndex]]
        else:
            return []

    middleIndex = startIndex + math.floor((endIndex - startIndex) / 2)
    
    a1 = merge_sort_recursive(array, startIndex, middleIndex, decreasing)
    a2 = merge_sort_recursive(array, middleIndex + 1, endIndex, decreasing)
    
    return merge_decreasing(a1, a2) if decreasing else merge(a1, a2)

def merge_sort(array):
    return merge_sort_recursive(array, 0, len(array))

def merge_sort_decreasing(array):
    return merge_sort_recursive(array, 0, len(array), True)