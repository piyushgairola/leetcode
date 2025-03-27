def removeDuplicates(s: str) -> str:
    temp = "#"
    for i in s:
        if i == temp[-1]:
            temp = temp[:-1]
        else:
            temp += i
            
    return temp[1:]
