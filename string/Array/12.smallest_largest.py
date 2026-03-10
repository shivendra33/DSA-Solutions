arr = [1,2,4,7,7,5]

arr = list(set(arr))
arr.sort()

if len(arr) < 2:
    print(-1)
else:
    print("Second Smallest:",arr[1])
    print("Second Largest:",arr[-2])