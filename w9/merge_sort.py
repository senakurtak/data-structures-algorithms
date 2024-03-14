def merge(arr1, arr2):
    i = 0
    j = 0
    a = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            a.append(arr1[i])
            i += 1
        else:
            a.append(arr2[j])
            j += 1
    while i<len(arr1):
        a.append(arr1[i])
        i+=1
    while j<len(arr2):
        a.append(arr2[j])        
        j+=1
    return a
            
            
def MergeSort(array):
    n = len(array)
    if n>1:
        ar1 = MergeSort(array[:n//2])
        ar2 = MergeSort(array[n//2:])
        return merge(ar1,ar2)
    else:
        return array    