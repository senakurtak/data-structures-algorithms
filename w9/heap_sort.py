def children(i):
    return 2*i+1, 2*i+2

def heapify(array, i = 0):
    l,r = children(i)
    if l<len(array):
        heapify(array, l)
    if r<len(array):
        heapify(array, r)
    min_index = i
    min = array[i]
    if l<len(array):
        if array[l]<min:
            min_index = l
            min = array[l]
    if r<len(array):
        if array[r]<min:
            min_index = r
    if min_index!=i:
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
        
def HeapSort(array):
    sorted = []
    while len(array):
        heapify(array)
        sorted.append(array.pop(0))
    return sorted
        