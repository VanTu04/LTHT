import threading
import queue

buffer = queue.Queue(maxsize=5)

def producer():
    for i in range(10):
        with buffer.mutex:
            buffer.put(i)
            print(f"Produced: {i}")
            buffer.not_empty.notify()

def consumer():
    for _ in range(10):
        with buffer.mutex:
            while buffer.empty():
                buffer.not_empty.wait()
            item = buffer.get()
            print(f"Consumed: {item}")

prod_thread = threading.Thread(target=producer)
cons_thread = threading.Thread(target=consumer)

prod_thread.start()
cons_thread.start()

prod_thread.join()
cons_thread.join()
