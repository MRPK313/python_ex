

def fibo(n):

    # order : o(n)

    if n <= 1:
        return 1

    a , b = 0,1

    for _ in range(2,n):

        a,b = b, a+b

    return b



def fibo_recursive(n):

    # order : o(2^n)
    
    if n <= 1:
        return 1
    
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)





print(fibo_recursive(3))


print(fibo(150))