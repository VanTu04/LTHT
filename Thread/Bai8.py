import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        counter += 1
        print(f"Counter: {counter}")

threads = [threading.Thread(target=increment) for _ in range(10)]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
