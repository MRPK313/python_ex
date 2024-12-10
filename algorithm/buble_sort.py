
def buble_sort(arr):

    n = len(arr)

    for i in range(n):

        swaped = False

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaped = True

            
        if not swaped:
            break

    
    return arr



print(buble_sort([64, 34, 25, 12, 22, 11, 90]))


# best order : o(n)

# worst and avrage order : o(n^2)