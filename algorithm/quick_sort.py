from partition_al import partition




def q_sort(arr):

    if len(arr) <= 1:
        return arr
    
    p_arr, p = partition(arr)

    left = p_arr[:p]
    right = p_arr[p+1:]

    return q_sort(left) + [p_arr[p]] + q_sort(right)


arr = [5, 2, 8, 1, 7, 3, 6, 4]

print(q_sort(arr))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# best and average order : o(nlogn)
# worst order : o(n^2)