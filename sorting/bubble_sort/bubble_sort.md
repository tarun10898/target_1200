

## 🔁 What Is Bubble Sort?

Bubble Sort is a simple **comparison-based** algorithm where adjacent elements are repeatedly swapped if they’re in the wrong order. It “bubbles” the largest unsorted element to its correct position in each pass.

---

## 🐌 Brute Force Bubble Sort

### 🔍 Description
- Compares every pair in every iteration.
- No checks for early stopping—even if the array is already sorted.

### 🧾 Code
```python
def bubble_sort_brute(arr, n):
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").strip().split()))[:n]
    print("Brute Force:", bubble_sort_brute(arr, n))
```

### 📊 Time & Space
- Time: O(n²) — always compares all pairs
- Space: O(1) — no extra storage
- ❌ No shortcut for sorted inputs

---

## ⚡ Optimized Bubble Sort with Early Stop

### 🔍 Description
- Adds a `swapped` flag.
- Stops early if no swaps occur—great for nearly sorted arrays.

### ✅ Code (Your Improved Version)
```python
def bubble_sort(arr, n):
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            print("Nothing to swap. Already sorted.")
            break
    return arr

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").strip().split()))[:n]
    print("Optimized:", bubble_sort(arr, n))
```

### 📊 Time & Space
| Case      | Time Complexity |
|-----------|------------------|
| Best (Sorted) | O(n)            |
| Worst        | O(n²)           |
| Average      | O(n²)           |

- Space: O(1)
- ✅ Much better for sorted or nearly sorted arrays

---

## 📌 Which to Use?

| Situation                   | Use This Sort        | Reason                             |
|-----------------------------|----------------------|------------------------------------|
| Learning basics             | Bubble (Brute Force) | Easy to understand                 |
| Slightly shuffled array     | Optimized Bubble     | Early stopping saves time          |
| Large datasets              | ❌ Avoid Bubble Sort  | Prefer Quick or Merge sort         |

---

