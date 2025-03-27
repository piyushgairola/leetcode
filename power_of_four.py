import math
import time


# Optimized sol.
def is_power_of_four(num):
    while num <= 0:
        return False
    val = math.log(num, 4)
    return val.is_integer()



def isPowerOfFour(num):
    if num <= 0:
        return False

    while num > 1:
        if num % 4 != 0:
            return False
        num = num // 4

    return True


if __name__ == '__main__':
    i = int(input())
    start = time.time()
    print(isPowerOfFour(i))
    print(time.time() - start)

    start = time.time()
    print(is_power_of_four(i))
    print(time.time() - start)

    start = time.time()
    print(is_power_of_four(i))
    print(time.time() - start)
