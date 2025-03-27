def title_to_number(s):
    l = len(s)
    res = 0
    for j in range(l):
        x = 26 ** (l-1-j)
        y = ord(s[j]) - ord('A') + 1
        res += x*y

    return res


if __name__ == '__main__':
    print(title_to_number('ZY'))

