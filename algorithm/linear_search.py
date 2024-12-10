
def linear_search(arr,target):

    for index,value in enumerate(arr):
        if value == target:
            return index
        
    return -1


print(linear_search([3,1,2,4,12,5,15], 15))


# best order --> o(1)

# avrage and worst order --> o(n)