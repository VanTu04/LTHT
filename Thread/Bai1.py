import threading

def print_hello():
    print("Hello, World!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
