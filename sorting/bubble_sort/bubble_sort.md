
---

## 🔁 Bubble Sort — Brute Force Version

### 💡 Concept:
Bubble Sort compares adjacent elements and **swaps them** if they’re in the wrong order. With each pass, the largest unsorted element “bubbles up” to its correct position — like foam rising to the surface.

---

### 🧠 Step-by-Step Algorithm:
1. Start from the first element.
2. Compare every pair of adjacent items.
3. Swap if the left item is greater than the right.
4. After each pass, the **largest unsorted item is placed correctly** at the end.
5. Repeat `n` times for an array of `n` elements.

---

### 🧪 Code — Basic Bubble Sort (Multiple Passes, No Optimization)

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):  # Don't re-check sorted part
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

### 📊 Example Walkthrough:
Input: `[5, 1, 4, 2, 8]`

- Pass 1 → `[1, 4, 2, 5, 8]`
- Pass 2 → `[1, 2, 4, 5, 8]`
- Pass 3 → `[1, 2, 4, 5, 8]` (no swaps needed)
- Pass 4 → early exit possible, but this version continues

---

## ⚡ Optimized Bubble Sort — Smarter Approach

### 🔧 What's Better?
Add a **`swapped` flag** to detect whether any swaps happened during a pass. If no swaps → array is sorted → exit early.

```python
def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # No swaps = array sorted early
    return arr
```

This avoids wasting time on already sorted or nearly sorted arrays — an edge that makes a real difference when scaling!

---

## 📊 Time & Space Complexity

| Scenario        | Time Complexity | Description                                  |
|-----------------|-----------------|----------------------------------------------|
| **Best Case**   | O(n)            | If array is already sorted (with `swapped`)  |
| **Average Case**| O(n²)           | Many out-of-order pairs                      |
| **Worst Case**  | O(n²)           | Completely reversed array                    |
| **Space**       | O(1)            | In-place sorting, no extra memory needed     |

---

