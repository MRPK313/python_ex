

def partition(arr):



    pivot = arr[0]
    i,j = 1 , len(arr) - 1

    while i < j :

        while i < j and arr[i] <= pivot:
            i += 1

        
        while i < j and arr[j] > pivot :
            j -= 1

        
        if i < j: 
            arr[i], arr[j] = arr[j], arr[i]



    arr[j],arr[0] = arr[0],arr[j]

    return arr , j




print(partition([3,1,2,4,12,5,15]))


print(partition([3,1,4,2,12,5,15])) # i , j change


print(partition([3,1,2,0])) # remove index exception with  while i<j in line 12, 16


print(partition([3,3,1,2,4]))


print(partition([3,3,3]))

