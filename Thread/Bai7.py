import threading

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited {amount}, Balance: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}, Balance: {self.balance}")
            else:
                print("Insufficient funds!")

account = BankAccount()
threads = []

for _ in range(5):
    t1 = threading.Thread(target=account.deposit, args=(100,))
    t2 = threading.Thread(target=account.withdraw, args=(50,))
    threads.extend([t1, t2])
    t1.start()
    t2.start()

for thread in threads:
    thread.join()
