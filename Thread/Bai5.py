import threading

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_primes(result, start, end):
    result.append(sum(i for i in range(start, end + 1) if is_prime(i)))

limit = 50
result = []
threads = []
step = 10

for i in range(0, limit, step):
    thread = threading.Thread(target=sum_primes, args=(result, i, min(i + step, limit)))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Sum of primes:", sum(result))
