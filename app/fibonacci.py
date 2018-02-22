
class Fibonacci:

    def __init__(self):
        pass

    def fibonacci(self, n):
        valid_input, msg = self.check_input(n)
        if not valid_input:
            raise ValueError("invalid input: {0}".format(msg))

        fib_list = []
        a,b = 0,1
        fib_list.append(a)
        for i in range(n-1):
            a,b = b,a+b
            fib_list.append(a)
        return fib_list


    def check_input(self, n):
        valid_value = True
        msg = "valid input"

        if not isinstance(n, int):
            msg = "not an integer"
            valid_value = False
        elif n < 0 or n > 10000:
            msg = "out of range"
            valid_value = False

        return valid_value, msg


if __name__ == '__main__':
    fib = Fibonacci()
    print(fib.fibonacci(5))

