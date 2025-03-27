
def add_digits(num):
    # my method
    # sum = 0
    # while num % 10:
    #     sum += num % 10
    #     num = num // 10
    #
    # if sum // 10 > 0:
    #     return add_digits(sum)
    # else:
    #     return sum

    # fast method
    if num in range(0, 10):
        return num
    if (num % 9 == 0):
        return 9
    return num % 9


if __name__ == '__main__':
    print(add_digits(134567))