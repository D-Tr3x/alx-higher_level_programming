#!/usr/bin/python3
import time
import random
find_peak = __import__('6-peak').find_peak

def measure_time(func, data):
    start = time.time()
    func(data)
    return time.time() - start

sizes = [10, 100, 1000, 10000, 100000]
times = [measure_time(find_peak, random.sample(range(1000000), size)) for size in sizes]

# Print results instead of plotting
for size, t in zip(sizes, times):
    print(f"Input Size: {size}, Execution Time: {t:.6f} seconds")
