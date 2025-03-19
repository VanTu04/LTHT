import threading

def multiply_row(result, A, B, row):
    for j in range(len(B[0])):
        result[row][j] = sum(A[row][k] * B[k][j] for k in range(len(B)))

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]

threads = []
for i in range(len(A)):
    thread = threading.Thread(target=multiply_row, args=(result, A, B, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Result matrix:", result)
