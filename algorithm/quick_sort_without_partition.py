

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

    middle = [x for x in arr if x == arr[pivot]]

    # for x in arr:
    #     if x == arr[pivot]:
    #         left.append(x)


    right = [x for x in arr if x > arr[pivot]]

    # for x in arr:
    #     if x > arr[pivot]:
    #         right.append(x)


    return q_sort(left) +middle+ q_sort(right)


if __name__ == '__main__':
    print(q_sort([3,1,5,7,4,2,10]))
    print(q_sort([3,3,3]))


# best and average order : o(nlogn)
# worst order : o(n^2)