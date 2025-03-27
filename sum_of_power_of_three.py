def checkPowerOfThree(n):
    while(n>0):
        if n%3==2:
            return False
        else:
            n = n//3

    return True



if __name__ == "__main__":
    print(checkPowerOfThree(91))