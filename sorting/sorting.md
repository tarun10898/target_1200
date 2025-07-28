

## 🔁 1. Bubble Sort

### 🐌 Brute Force
Compare every adjacent pair; swap if out of order.

```python
def bubble_sort_brute(arr):
    n = len(arr)
    for _ in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

### ⚡ Optimized
Skip further passes if no swaps happen.

```python
def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
```

📊 Time: O(n²) worst, O(n) best  
📦 Space: O(1)

---

## ✋ 2. Selection Sort

### 🐌 Brute Force
Find minimum in unsorted part and place it in the right spot.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

✅ Optimized by reducing swaps and tracking index.

📊 Time: O(n²)  
📦 Space: O(1)

---

## 🧩 3. Insertion Sort

### 🐌 Brute Force
Insert current element into sorted left half.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr
```

✅ Optimized version uses binary search for position (with extra code).

📊 Time: O(n²) worst, O(n) best  
📦 Space: O(1)

---

## 🌊 4. Merge Sort

### 🐌 Brute Force & Optimized (same structure)

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:] + right[j:])
    return result
```

📊 Time: O(n log n)  
📦 Space: O(n)

---

## ⚔️ 5. Quick Sort

### 🐌 Brute Force
Partition around pivot recursively.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
```

✅ Optimized: Use median-of-three, in-place partitioning.

📊 Time: O(n²) worst, O(n log n) best  
📦 Space: O(log n)

---

## 📊 6. Counting Sort

Best for small integer ranges

```python
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr
```

📊 Time: O(n + k)  
📦 Space: O(k)

---

## 🔢 7. Radix Sort

Used for sorting large numbers based on digits.

```python
def counting_sort_for_radix(arr, exp):
    count = [0] * 10
    output = [0] * len(arr)
    for num in arr:
        count[(num // exp) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in reversed(range(len(arr))):
        num = arr[i]
        index = (num // exp) % 10
        output[count[index] - 1] = num
        count[index] -= 1
    return output

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr
```

📊 Time: O(d(n + k))  
📦 Space: O(n + k)

---

## 🪣 8. Bucket Sort

```python
def bucket_sort(arr):
    bucket_count = 10
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = int(bucket_count * num)
        buckets[index].append(num)
    for i in range(bucket_count):
        buckets[i] = sorted(buckets[i])  # You could use insertion_sort here
    return [num for bucket in buckets for num in bucket]
```

📊 Time: O(n + k)  
📦 Space: O(n + k)

---

## 🔄 9. Cyclic Sort

Suited for values from 1 to N

```python
def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        correct_index = arr[i] - 1
        if arr[i] != arr[correct_index]:
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            i += 1
    return arr
```

📊 Time: O(n)  
📦 Space: O(1)

---

## 🧠 10. Custom Sort (Use `key` param in Python)

```python
arr = ["apple", "banana", "cherry"]
sorted_arr = sorted(arr, key=lambda x: len(x))
```

📊 Time: Depends on inner logic (usually O(n log n))  
📦 Space: O(n)

---
