def fib():
    n = int(input('Please input the number - '))
    a = 1
    b = 1
    for count in range(0, n - 1):
        a, b = b, a + b
        print(b)


if __name__ == '__main__':
    fib()
