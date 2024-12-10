
def merge(left, right):

    # all orders : o(n)

    sorted_arr = []

    i,j = 0,0

    for _ in range(len(left)+ len(right)):

        # all orders : o(n log n)
        
        if i >= len(left):
            sorted_arr.extend(right[j:])
            break

        elif j >= len(right):
            sorted_arr.extend(left[i:])
            break

        elif left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    return sorted_arr



def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    

    mid = len(arr) // 2

    left_sort = merge_sort(arr[:mid])
    right_sort = merge_sort(arr[mid:])

    return merge(left_sort, right_sort)




print(merge_sort([3,1,5,7,4,2,10]))


# all orders : o(n log n)