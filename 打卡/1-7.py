import threading
import time

def sleep_sort(lst):
    res = []
    def az(i):
        time.sleep(i)
        res.append(i)
    threads = []
    for i in range(len(lst)):
        threads.append(threading.Thread(target=lambda: az(lst[i])))
        threads[i].start()
    time.sleep(max(lst))
    return res
        
lst = [1,3,2]
print(sleep_sort(lst))