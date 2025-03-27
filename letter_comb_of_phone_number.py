def letterCombinations(digits):
    map = {
        2:['a','b','c'],
        3:['d','e','f'],
        4:['g','h','i'],
        5:['j','k','l'],
        6:['m','n','o'],
        7:['p','q','r','s'],
        8:['t','u','v'],
        9:['w','x','y','z']
    }
    
    if len(digits)==0:
        return []
    if len(digits)==1:
        return map[int(digits[0])]
    
    l1 = letterCombinations(digits[:-1])
    l2 = map[int(digits[-1])]
    
    return [p + q for p in l1 for q in l2]


if __name__=='__main__':

    print(letterCombinations("2"))