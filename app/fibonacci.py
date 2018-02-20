


def fibonacci(n):
    fib_list = []
    a,b = 0,1
    fib_list.append(a)
    for i in range(n-1):
        a,b = b,a+b
        fib_list.append(a)
        #print(a)
    return fib_list
