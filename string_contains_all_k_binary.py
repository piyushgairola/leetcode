def hasAllCodes(s,k):
    l = 2**k
    for i in range(l):
        binary = bin(i)[2:]
        if binary not in s:
            return False
    
    return True


if __name__ == "__main__":
    print(hasAllCodes("0110",2))
    