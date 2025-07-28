def optimised_arr(arr):
    n=len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key 
    return arr        
if __name__ == "__main__":
    n=int(input("enter the number of the values to be entred in the array"))
    arr = list (map(int, input("enter the number of the vaules ").strip().split()))[:n]
    print(optimised_arr(arr))