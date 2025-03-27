def compareVersion(version1: str, version2: str) -> int:
    l1 = list(map(int, version1.split('.')))
    l2 = list(map(int, version2.split('.')))

    l1_len = len(l1)
    l2_len = len(l2)

    if l1_len < l2_len:
        l1 += [0] * (l2_len - l1_len)
    if l1_len > l2_len:
        l2 += [0] * (l1_len - l2_len)

    n = len(l1)

    for i in range(n):
        if l1[i] > l2[i]:
            return 1
        if l1[i] < l2[i]:
            return -1

    return 0


if __name__ == '__main__':
    print(compareVersion("1","1.1"))