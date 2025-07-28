def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j]< arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
            else:
                break
    return arr            

if __name__ == "__main__":
    n= int(input("enter the number"))
    arr = list(map(int,input("enter the values").strip().split()))
    print(insertion_sort(arr))

