def partition(arr, low, high):
    i =(low-1)
    pivot=arr[high]

    for j in range(low, high):
        if arr[j]>=pivot:
            i=i+1
            arr[i],arr[j]=arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    if low < high:#Se busca el indice no el valor
        partitionIndex = partition(arr,low,high)
        quickSort(arr, low, partitionIndex-1)
        quickSort(arr, partitionIndex+1, high)

my_list = [1,4,5,6,9,13,19,21]
odd = list(filter(lambda x: x%2 !=0, my_list))

n= len(odd)
quickSort(odd, 0, n-1)
print("Array ordenado:")
for i in range(n):
    print("%d" %odd[i])