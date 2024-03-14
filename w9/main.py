import random
import time
from buble_sort import BubbleSort

algo = BubbleSort

for i in range(1,5):
    n = 10**i
    arr = [random.randint(0,n) for i in range(n)]
    t = time.time()
    elapsed_time = time.time() - t
    #print(arr)
    bubble_arr = algo(arr)
    #print(bubble_arr)
    print("n =", n, "---t=", elapsed_time )