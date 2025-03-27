def solution(s):
    result = [s[0]]
    max_length = 0

    for i in range(1, len(s)):
        if s[i] in result:
            max_length = max(max_length, len(result))
            result.append(s[i])
            result.pop(0)
        else:
            result.append(s[i])

    return max(max_length, len(result))


s= "pwwkew"

print(solution(s))