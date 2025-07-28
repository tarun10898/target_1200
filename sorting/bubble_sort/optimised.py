def bubble_sort(arr,n):
    swapped = False
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            print("nothing to swap")
            break
    return arr   


if __name__== "__main__":
    n = int(input("enter the no of elements"))
    arr = list(map(int,input("enter the number of elements of the list: ").strip().split()))[:n]
    print(bubble_sort(arr,n))
