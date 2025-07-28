
## ⚔️ What Is Quick Sort?

Quick Sort is a **divide-and-conquer** algorithm that selects a **pivot** and partitions the array so that:
- All items **less than the pivot** go to the left
- All items **greater than the pivot** go to the right  
Then it recursively sorts both halves. It’s lightning-fast in practice due to **in-place sorting** and **good cache behavior**.

---

## 🐌 Brute Force Quick Sort

### 🔍 Description
- Naively selects the first element as the pivot.
- Creates new arrays for left and right partitions.
- Not memory efficient, but easy to follow.

### ✅ Code
```python
def quick_sort_brute(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort_brute(left) + [pivot] + quick_sort_brute(right)

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter the elements: ").strip().split()))[:n]
    print("Brute Force Quick Sort:", quick_sort_brute(arr))
```

---

## ⚡ Optimized In-place Quick Sort

### 🚀 Description
- Uses **in-place partitioning** for better memory use.
- Reduces slice overhead.
- Pivot can be randomized to improve performance in worst-case inputs.

### ✅ Code
```python
def quick_sort_optimized(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_optimized(arr, low, pi - 1)
        quick_sort_optimized(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Last element as pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter the elements: ").strip().split()))[:n]
    quick_sort_optimized(arr, 0, n - 1)
    print("Optimized Quick Sort:", arr)
```

---

## 📊 Time & Space Complexity

| Case      | Time       | Explanation                              |
|-----------|------------|------------------------------------------|
| Best      | O(n log n) | Balanced partitioning                    |
| Average   | O(n log n) | Most cases with random or middle pivot   |
| Worst     | O(n²)      | Unbalanced pivot (e.g., sorted array)    |
| Space     | O(log n)   | For recursion stack (in-place sorting)   |
| Stability | ❌ Unstable | May rearrange equal elements             |

---

## 🧠 When to Use Quick Sort?

| Scenario                         | Use Quick Sort? | Why                                 |
|----------------------------------|------------------|--------------------------------------|
| Large unsorted arrays            | ✅ Yes           | Fast and memory efficient            |
| Need stable sort                 | ❌ No            | Use Merge Sort instead               |
| Linked lists or limited memory   | ❌ No            | Use Merge or Insertion Sort          |
| Randomized or varied inputs      | ✅ Yes           | Performs great with varied data      |

---

Quick Sort is like a samurai—fast, precise, but needs to pick its battles wisely (i.e., pivot strategy). ⚔️
