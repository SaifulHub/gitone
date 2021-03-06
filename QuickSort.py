def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)
def quickSort(arr,low,high):
    if(low<high):
        pi=partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

arr=[23,0,9,-8]

quickSort(arr,0,len(arr)-1)
print("Sorter Array is :\n")
for i in range(len(arr)):
    print(arr[i])