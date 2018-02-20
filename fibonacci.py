
class fibonacci():

    def fibonacci(n):
        fib_list = [0]
        a,b = 1,1
        fib_list.append(a)
        for i in range(n-2):
            a,b = b,a+b
            fib_list.append(a)
            #print(a)
        return fib_list
