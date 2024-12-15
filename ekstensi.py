import random
import time
import matplotlib.pyplot as plt

def is_unique(array):
    seen = set()
    for num in array:
        if num in seen:
            return False
        seen.add(num)
    return True

def calculate_cases(n, max_value, trials=10):
    random.seed(42)  
    worst_time = 0
    total_time = 0

    for _ in range(trials):
        array = [random.randint(1, max_value) for _ in range(n)]

        start_time = time.time()
        is_unique(array)
        elapsed_time = time.time() - start_time

        total_time += elapsed_time
        worst_time = max(worst_time, elapsed_time)

    avg_time = total_time / trials
    return worst_time, avg_time

n_values = [100, 150, 200, 250, 300, 350, 400, 500]
max_value = 250 - 123  # Misalnya, 3 digit terakhir stambuk = 123

results = []
worst_cases = []
avg_cases = []

for n in n_values:
    worst, avg = calculate_cases(n, max_value)
    results.append((n, worst, avg))
    worst_cases.append(worst)
    avg_cases.append(avg)

with open("worst_avg.txt", "w") as f:
    f.write("n\tWorst Case\tAverage Case\n")
    for n, worst, avg in results:
        f.write(f"{n}\t{worst:.6f}\t{avg:.6f}\n")

plt.figure(figsize=(10, 6))
plt.plot(n_values, worst_cases, label="Worst Case", marker="o")
plt.plot(n_values, avg_cases, label="Average Case", marker="s")
plt.title("Performance Analysis")
plt.xlabel("Array Size (n)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid()
plt.savefig("performance_plot.jpg")
plt.show()
