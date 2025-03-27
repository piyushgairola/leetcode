import time


def is_subsequence(s, t):  # my solution
    i = 0
    j = 0
    while i < len(t) and j < len(s):
        if s[j] == t[i]:
            j += 1
            i += 1
        else:
            i += 1

    if j == (len(s)):
        return True
    else:
        return False


def isSubsequence(s, t):  # Better and faster code
    i, j = 0, 0
    len_s = len(s)
    len_t = len(t)
    while i < len_t and j < len_s:
        if s[j] == t[i]:
            j += 1
        i += 1

    return j == len_s


if __name__ == '__main__':
    s = 'abc'
    t = 'ahbgdc'
    t0 = time.time()
    print(is_subsequence(s, t), end=' ')
    print(time.time() - t0)

    t1 = time.time()
    print(isSubsequence(s, t), end=' ')
    print(time.time() - t1)
