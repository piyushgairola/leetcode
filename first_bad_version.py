def first_bad_version(n):
    start = 1
    end = n
    while start < end:
        mid = (start + end) // 2
        if isBadVersion(mid):
            end = mid
        else:
            start = mid + 1

    return start


