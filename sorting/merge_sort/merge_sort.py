def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge_brute(left,right)

def merge_brute(left,right):
    merged = []
    i=j=0
    while i <len(left) and j<len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1 
    merged.extend(left[i:])        
    merged.extend(right[j:])

    return merged


if __name__ == "__main__":
    n= int(input("enter the values in the array"))
    arr = list(map(int,input("enter the values of the list").strip().split()))[:n]
    print(merge_sort(arr))
