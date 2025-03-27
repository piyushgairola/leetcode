def integerToRoman(num):
    divList = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    romanList = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    return getResult(divList,romanList,num)

def getResult(divList,romanList,num):
    if num ==0:
        return ""

    idx = getIndex(divList,num)

    return romanList[idx]+getResult(divList,romanList,(num-divList[idx]))



def getIndex(divList,num):
    l = len(divList)
    for i in range(l):
        if num//divList[i] != 0:
            return i
        
    return -1

if __name__ == "__main__":
    print(integerToRoman(3894))

