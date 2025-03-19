import threading

def print_even():
    print("Even numbers:", [i for i in range(1, 21) if i % 2 == 0])

def print_odd():
    print("Odd numbers:", [i for i in range(1, 21) if i % 2 != 0])

even_thread = threading.Thread(target=print_even)
odd_thread = threading.Thread(target=print_odd)

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()
