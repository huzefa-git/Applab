import sys
arr=[1,4,2,3,6,5,9,7,1]

for i in range(len(arr)):
    min_idx=i
    for j in range(i+1,len(arr)):
        if arr[min_idx]>arr[j]:
            min_idx=j
    arr[min_idx],arr[i] = arr[i],arr[min_idx]

print("Sorted array")
for i in range(len(arr)):
    print("%d" %arr[i],end=" , ")