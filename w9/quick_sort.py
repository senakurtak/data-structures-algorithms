def Partition(array): 
    p = array[-1]
    left = []
    right = []
    for element in array [:-1]:
        if element<p:
            left.append(element)
        else:
            right.append(element)
    return p, left, right

def QuickSort(array):
    if len(array)<2:
        return array
    pivot, left_array, right_array = Partition(array)
    left_array = QuickSort(left_array)
    right_array = QuickSort(right_array)
    return left_array + [pivot] + right_array