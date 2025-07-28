def selection_sort(arr,n):
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i],arr[min_index] = arr[min_index], arr[i]
    return arr               
if __name__ == "__main__":
    n=int(input("enter the count of the elements: "))
    arr = list(map(int,input("enter the elements in the array: ").strip().split()))[:n]
    print(selection_sort(arr,n))