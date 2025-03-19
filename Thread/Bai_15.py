import threading

def print_even_numbers(start, end):
    """Hàm in số chẵn"""
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(f"{threading.current_thread().name}: Chẵn {num}")

def print_odd_numbers(start, end):
    """Hàm in số lẻ"""
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(f"{threading.current_thread().name}: Lẻ {num}")

# Tạo hai luồng: một luồng in số chẵn, một luồng in số lẻ
thread_even = threading.Thread(target=print_even_numbers, args=(30, 50), name="Thread-Chẵn")
thread_odd = threading.Thread(target=print_odd_numbers, args=(30, 50), name="Thread-Lẻ")

# Khởi động hai luồng
thread_even.start()
thread_odd.start()

# Chờ cả hai luồng hoàn thành
thread_even.join()
thread_odd.join()