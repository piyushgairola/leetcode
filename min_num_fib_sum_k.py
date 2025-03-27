def findMinFibonacciNumbers(k):
    count = 0
    a = b = 1
    while b <= k:
        a, b = b, a + b

    while b > 0:
        if k < 2:
            count += 1
            return count
        if k < b:
            k = k - b
            count += 1
        a, b = b - a, b


if __name__ == '__main__':
    print(findMinFibonacciNumbers(19))