import time
import math


def is_power_of_two(n):  # My solution
    while n > 0:
        if n == 1:
            return True
        elif n % 2 == 0:
            n = n // 2
        else:
            return False


def _isPowerOfTwo(n: int) -> bool:  # Better coding version of my code
    if n == 0:
        return False

    while n % 2 == 0:
        n = n / 2
    return n == 1


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


def isPowerOfTwo(n: int) -> bool:   # Fastest code
    if n <= 0:
        return False
    rem, _ = math.modf(truncate(math.log(n, 2), 14))
    return rem == 0


def fastest(num):
    while num <= 0:
        return False
    val = math.log(num, 2)
    return val.is_integer()


if __name__ == '__main__':
    num = 1546

    t0 = time.time()
    print(is_power_of_two(num), )
    print(time.time() - t0, end='\n\n')

    t1 = time.time()
    print(isPowerOfTwo(num), )
    print(time.time() - t1, end='\n\n')

    t2 = time.time()
    print(_isPowerOfTwo(num))
    print(time.time() - t2, end='\n\n')

    t2 = time.time()
    print(test(num))
    print(time.time() - t2, end='\n\n')
