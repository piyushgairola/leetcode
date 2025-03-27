def to_goat_latin(s):
    res = []
    vowels = ['A','a','E','e','I','i','O','o','U','u']
    for i,val in enumerate(s.split()):
        if val[0] in vowels:
            temp = val + "ma" + ("a"* (i+1))
        else:
            temp = val[1:] + val[0] + "ma" + ("a"*(i+1))

        res.append(temp)

    res = " ".join(res)

    return res


if __name__ == '__main__':
    print(to_goat_latin("I Love You"))