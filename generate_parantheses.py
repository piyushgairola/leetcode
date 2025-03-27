def generatePara(n):
    ans = []

    def generate(s,l,r):
        if len(s) == 2*n:
            ans.append("".join(s))
            return

        if l<n:
            s.append("(")
            generate(s,l+1,r)
            s.pop()

        if r<l:
            s.append(")")
            generate(s,l,r+1)
            s.pop()


    generate([],0,0)

    return ans


print(generatePara(3))