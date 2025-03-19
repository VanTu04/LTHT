import threading

def factorial_partial(start, end, result, index):
    #Tính giai thừa một phần từ start đến end và lưu vào result[index]
    partical_result = 1
    for i in range(start, end + 1):
        partical_result *= i
    result[index] = partical_result

def factorial(n, number_thread):
    if n == 0 or n == 1:
        return 1

    step = n // number_thread
    threads = []
    results = [1] * number_thread

    for i in range(number_thread):
        start = i * step + 1
        end = (i + 1) * step if i != number_thread - 1 else n
        thread = threading.Thread(target=factorial_partial, args=(start, end, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_result = 1
    for i in results:
        final_result *= i

    return final_result

# main
n = int(input("Nhập số nguyên n: "))
number_thread = int(input("Nhập số lượng thread muốn sử dụng:"))

result = factorial(n, number_thread)
print(f"{n}! = {result}")