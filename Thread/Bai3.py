import threading

def sort_array(array):
    array.sort()
    print("Sorted array:", array)

array = [12, 4, 5, 3, 8, 7]
sort_thread = threading.Thread(target=sort_array, args=(array,))
sort_thread.start()
sort_thread.join()
