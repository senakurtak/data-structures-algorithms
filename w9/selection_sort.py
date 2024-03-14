def SelectionSort(array):
    n = len(array)
    for i in range(n):
        min = array[i]
        min_index = i
        for j in range(i, n):
            if array[j]<min:
                min = array[j]
                min_index = j
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp 
    return array