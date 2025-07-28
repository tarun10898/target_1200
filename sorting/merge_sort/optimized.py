def merge_sort_optimized(arr):
    def sort(arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        sort(arr, low, mid)
        sort(arr, mid + 1, high)  # Notice: `mid + 1` here is proper
        sorted_list(arr, low, mid, high)

    def sorted_list(arr, low, mid, high):
        temp = []
        i, j = low, mid + 1
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= high:
            temp.append(arr[j])
            j += 1
        for k in range(len(temp)):
            arr[low + k] = temp[k]

    sort(arr, 0, len(arr) - 1)
    return arr
                          

if __name__ == "__main__":
    n=int(input("enter the values count of the, list"))
    arr =list(map(int,input("enter the values in the list").strip().split()))[:n]
    print(merge_sort_optimized(arr))