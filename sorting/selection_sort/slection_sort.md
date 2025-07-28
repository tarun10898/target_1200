

# 🎯 What Is Selection Sort?

Selection Sort divides the array into two parts: **sorted** and **unsorted**. It repeatedly selects the minimum (or maximum) from the unsorted part and swaps it with the first unsorted element—like finding the winner of every round in a slow tournament.

---

## 🐌 Brute Force Selection Sort

### 🔍 Description
- Scans entire unsorted portion to find the minimum.
- Always does \(n-i-1\) comparisons for pass \(i\).
- No early stopping, even if the array is sorted.

### ✅ Code
```python
def selection_sort_brute(arr, n):
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").strip().split()))[:n]
    print("Brute Force Selection Sort:", selection_sort_brute(arr, n))
```

---

## ⚡ Slight Optimization Insight

Selection Sort’s structure doesn’t benefit from early termination like Bubble Sort. But you *can* add logging or checks to understand its process better.

### 🧪 Insightful Version with Logging
```python
def selection_sort_with_logs(arr, n):
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            print(f"Swapping {arr[i]} and {arr[min_idx]}")
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").strip().split()))[:n]
    print("Selection Sort with logs:", selection_sort_with_logs(arr, n))
```

---

## 📊 Time & Space Complexity

| Case      | Time Complexity | Explanation                   |
|-----------|------------------|-------------------------------|
| Best      | O(n²)            | Still loops through each pair |
| Average   | O(n²)            | Fixed pattern of comparisons  |
| Worst     | O(n²)            | No adaptive behavior          |

- Space: O(1) – no extra arrays
- Stability: ❌ Not stable (swaps can disrupt order of equal elements)

---

## 🆚 Bubble Sort vs Selection Sort

| Feature          | Bubble Sort           | Selection Sort         |
|------------------|-----------------------|------------------------|
| Early Stop       | ✅ Optimized version   | ❌ Not possible         |
| Swap Frequency   | Many in each pass     | Only 1 per pass        |
| Best Case        | O(n) (Optimized)      | O(n²)                  |
| Use Case         | Simple sorting tasks  | Small fixed datasets   |

