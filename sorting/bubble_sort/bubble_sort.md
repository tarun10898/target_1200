
---

### 🔁 Bubble Sort — Brute Force Approach

#### 💭 Concept:
It repeatedly compares adjacent elements and swaps them if they’re in the wrong order. Like bubbles rising, the largest element “bubbles” to the end in each pass.

#### 🧠 Algorithm:
- Loop through the array multiple times.
- In each pass, compare adjacent elements.
- Swap them if they’re out of order.
- Repeat until the array is sorted.

#### 🐢 Code Example (Python):
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

#### ⏱️ Time Complexity:
- Worst and Average: O(n²)
- Best Case (already sorted): O(n) with an optimization

---

### ⚡ Optimized Bubble Sort

We improve it by adding a flag to detect if the array is already sorted during a pass.

```python
def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # No swaps means the array is sorted
            break
    return arr
```

🧠 This small tweak avoids unnecessary passes — a good mindset when stepping into optimization territory.

---

