import random
import time
from buble_sort import BubbleSort
from selection_sort import SelectionSort
from insertion_sort import InsertionSort
from merge_sort import MergeSort
from quick_sort import QuickSort

test = False
algo = QuickSort

if test:
    n = 10
    arr = [random.randint(0,n) for i in range(n)]
    print(arr)
    sorted_arr = algo(arr)
    print(sorted_arr)
    exit()
for i in range(1,5):
    n = 10**i
    arr = [random.randint(0,n) for i in range(n)]
    t = time.time()
    elapsed_time = time.time() - t
    #print(arr)
    bubble_arr = algo(arr)
    #print(bubble_arr)
    print("n =", n, "---t=", elapsed_time )