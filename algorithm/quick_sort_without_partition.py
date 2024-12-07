

def q_sort(arr):

    left = []
    right = []

    if len(arr) <= 1:
        return arr
    
    pivot = len(arr) // 2

    left = [x for x in arr if x < arr[pivot]]

    # for x in arr:
    #     if x < arr[pivot]:
    #         left.append(x)


    right = [x for x in arr if x > arr[pivot]]

    # for x in arr:
    #     if x > arr[pivot]:
    #         right.append(x)


    return q_sort(left) +[arr[pivot]]+ q_sort(right)



print(q_sort([3,1,5,7,4,2,10]))


# best and average order : o(nlogn)
# worst order : o(n^2)