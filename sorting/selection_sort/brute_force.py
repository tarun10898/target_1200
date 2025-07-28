def selection_sort(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr            

if __name__ == "__main__":
    n = int(input("enter the count of the emlemnts: "))
    arr = list(map(int,input("enter the elemtns of the array: ").strip().split()))[:n]
    print(selection_sort(arr,n))

