

### 🔍 Core Idea Behind Selection Sort

- You start with the **first element** and try to find the **smallest element** in the rest of the array.
- Then you **swap** that smallest element with the current one.
- You keep doing this, moving forward one element at a time.

---

### 🥊 Brute Force Walkthrough (Multiple Swaps per Pass)

```python
def selection_sort_brute(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]  # Swap immediately
```

Let’s take:  
`arr = [64, 25, 12, 22, 11]`

**Pass 1 (i = 0)**  
- Compare `64` with `25` → Swap → `[25, 64, 12, 22, 11]`  
- Compare `25` with `12` → Swap → `[12, 64, 25, 22, 11]`  
- Compare `12` with `22` → No swap  
- Compare `12` with `11` → Swap → `[11, 64, 25, 22, 12]`

👉 You can see how many swaps happened _in just one pass._

---

### 🚀 Optimized Walkthrough (Only One Swap per Pass)

```python
def selection_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

Now with the same array:  
`arr = [64, 25, 12, 22, 11]`

**Pass 1 (i = 0)**  
- Find index of minimum → `11` at index `4`  
- Swap `64` and `11` → `[11, 25, 12, 22, 64]`  

Only **one swap** here.

---

### 🔬 Summary of Difference

| 🔧 Feature                | Brute Force                          | Optimized                        |
|--------------------------|--------------------------------------|----------------------------------|
| 🔁 Swap Frequency         | Multiple times per pass              | One swap per pass                |
| ⚡ Efficiency             | More memory writes                   | Fewer writes (better for EEPROM) |
| 🧠 Usefulness             | Illustrates basic concept            | Better for actual use cases      |

---
