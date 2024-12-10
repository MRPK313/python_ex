
def binary_search(arr,target):

    left,right = 0,len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        
        elif target > arr[mid]:
            left = mid + 1

        else:
            right = mid - 1

    return -1



print(binary_search([1,4,6,8,9,19,84],9))

print(binary_search([1,4,6,8,9,19,84],484))


# best order : o(1)

# average and worst order : o(logn)