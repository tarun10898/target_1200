
---

## ⚙️ Brute Force — Standard Insertion Sort

```python
def insertion_sort_brute(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr
```

- Direct shifting of elements to place each `key` in its correct position.

---

## 🚀 Optimized Insertion Sort (with Binary Search)

We reduce comparisons by using binary search to find the correct position for insertion — but shifting still takes linear time.

```python
def binary_search(arr, key, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return start  # Correct position to insert key

def insertion_sort_optimized(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        insert_pos = binary_search(arr, key, 0, i - 1)
        
        # Shift elements to the right
        arr = arr[:insert_pos] + [key] + arr[insert_pos:i] + arr[i + 1:]
    return arr
```

- 🧠 Uses binary search to reduce comparisons from O(n) to O(log n) per insertion.
- 📦 Still O(n²) overall due to shifting elements, but better performance on comparison-heavy workloads.

---

## 📊 Time & Space Complexity Comparison

| Variant                 | Best Case | Average Case | Worst Case | Space Complexity |
|------------------------|-----------|--------------|------------|------------------|
| Brute Force            | O(n)      | O(n²)        | O(n²)      | O(1)             |
| Optimized (Binary Search)| O(n log n) | O(n²)      | O(n²)      | O(1)             |

- **Best case:** Already sorted → very few shifts or comparisons.
- **Optimized variant** reduces **comparisons** but not **shifts**.

---
