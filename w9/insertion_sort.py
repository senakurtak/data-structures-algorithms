def InsertionSort(array):
    n = len(array)
    for i in range(1,n):
        for j in range(i,0 , -1):
            if array[j]<array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
            else:
                break
    return array