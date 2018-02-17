def fib(n):
    fib_list = [0]
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
        fib_list.append(a)
        #print(a)
    return fib_list

if __name__ == '__main__':
    print(fib(5))
