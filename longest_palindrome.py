def longest_palindrome(s):
    map = {}
    for c in s:
        if c in map:
            map[c] += 1
        else:
            map[c] = 1

    res = odd_flag =0
    for val in map.values():
        if val%2 == 1:
            odd_flag = 1
        res += val//2 * 2
    return res+1 if odd_flag else res


if __name__ == '__main__':
    print(longest_palindrome('abcc'))

