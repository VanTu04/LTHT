import threading

lock = threading.Lock()

def access_resource(thread_id):
    with lock:
        print(f"Thread {thread_id} accessing shared resource")

threads = [threading.Thread(target=access_resource, args=(i,)) for i in range(5)]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
