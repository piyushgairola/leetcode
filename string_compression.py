def solution(chars):
    i = 0
    res = 0 # this will denote the length of result

    while(i<len(chars)):
        group_len = 1

        while(i + group_len < len(chars) and chars[i+group_len] == chars[i]):
            group_len += 1
        
        chars[res] = chars[i]
        res += 1

        if group_len > 1:
            str_group_len = str(group_len)
            chars[res : res + len(str_group_len)] = list(str_group_len)

            res += len(str_group_len)

        i += group_len

    return res
if __name__ == "__main__":
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    # chars = ["a"]
    print(solution(chars))