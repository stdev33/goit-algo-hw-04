# goit-algo-hw-02

Homework 2. Basic Algorithms and Data Structures at GoIT Neoversity

# Sorting Algorithms Comparison

## Description
In this task, we compare three sorting algorithms: Merge Sort, Insertion Sort, and Timsort, which is the built-in sorting algorithm in Python. We measured the execution time of each algorithm on different datasets.

## Algorithms
1. **Merge Sort**: A recursive algorithm that splits the array into smaller parts and merges them back in sorted order.
2. **Insertion Sort**: An algorithm that sequentially inserts each element into the sorted part of the array.
3. **Timsort**: The built-in sorting algorithm in Python that combines Merge Sort and Insertion Sort.

## Results

### Small Dataset (100 elements)

- **Merge Sort**: `0.000134` seconds
- **Insertion Sort**: `0.000165` seconds
- **Timsort**: `0.000009` seconds

### Medium Dataset (1000 elements)

- **Merge Sort**: `0.001578` seconds
- **Insertion Sort**: `0.017779` seconds
- **Timsort**: `0.000077` seconds

### Large Dataset (10000 elements)

- **Merge Sort**: `0.019691` seconds
- **Insertion Sort**: `1.901867` seconds
- **Timsort**: `0.000948` seconds

## Test Environment
The results were obtained on a MacBook Pro 2021 with an Apple M1 Pro processor.

## Conclusions

Our results show that Timsort is significantly more efficient compared to Merge Sort and Insertion Sort. This is due to Timsort combining the advantages of both algorithms, making it faster for most cases.

Programmers often use built-in algorithms like Timsort because of their efficiency and optimization for a wide range of input data. Writing custom sorting algorithms can be educational, but for practical use in real projects, built-in algorithms are more efficient and reliable.