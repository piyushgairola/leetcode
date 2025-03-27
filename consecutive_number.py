def consecutive(N,K):
    res = []
    for i in range(1,10):
        if i<K and K+i <10 or i>=K and K-i<10:
            num = 0
            j=N-1
            if N%2==0:
                while(j>0):
                    num += i*(10**j)
                    if (i<K):
                        num += (K+i)*(10**(j-1))
                    else:
                        num += (K-i)*(10**(j-1))
                    j -= 2
            else:
                while (j > 0):
                    num += i * (10 ** j)
                    if (i < K):
                        num += (K + i) * (10 ** (j - 1))
                    else:
                        num += (K - i) * (10 ** (j - 1))
                    j -= 2

                num += i*(10**j)

            res.append(num)

    return res


if __name__ == '__main__':
    print(consecutive(3,7))

