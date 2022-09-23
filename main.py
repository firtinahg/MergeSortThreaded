#thread module to implement concurrency
from threading import Thread, current_thread

#decorator for thread operation
def run_in_thread(fn):
    def run(*k, **kw):
        t = Thread(target=fn, args=k, kwargs=kw)
        print(t.name,"started")
        t.start()
        t.join()
        
    return run

#array(list) to be merge sorted
list_of_num = [3304,8221,26849,14038,1509,6367,7856,21362]

#merge sort algorithm with thread decorator
@run_in_thread
def mergeSort(arr):
   
    if len(arr) > 1:
        
         # Finding the mid of the array
        mid = len(arr)//2

        #print("mid=",mid)
        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half

        mergeSort(L)

        # Sorting the second half
        
        mergeSort(R)

        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        #after finishing the operation, the thread will be finish also
    print(current_thread().name," finished: ", arr)
        

def main():
    mergeSort(list_of_num)

if __name__ == "__main__":
    main()

