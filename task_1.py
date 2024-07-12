import timeit
import random
from sorters import merge_sort, insertion_sort, tim_sort


small_dataset = [random.randint(0, 100) for _ in range(100)]
medium_dataset = [random.randint(0, 1000) for _ in range(1000)]
large_dataset = [random.randint(0, 10000) for _ in range(10000)]


datasets = {
    'small': small_dataset[:],
    'medium': medium_dataset[:],
    'large': large_dataset[:]
}


def measure_time(func, data):
    return timeit.timeit(lambda: func(data[:]), number=1)


results = {
    'merge_sort': {},
    'insertion_sort': {},
    'tim_sort': {}
}

for size in datasets:
    print(f"Measuring time for {size} dataset")
    results['merge_sort'][size] = measure_time(merge_sort, datasets[size])
    results['insertion_sort'][size] = measure_time(insertion_sort, datasets[size])
    results['tim_sort'][size] = measure_time(tim_sort, datasets[size])


for alg in results:
    print(f"\nResults for {alg}:")
    for size in results[alg]:
        print(f"{size}: {results[alg][size]:.6f} seconds")