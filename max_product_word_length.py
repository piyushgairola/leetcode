import itertools

def maxProduct(words):
    n = len(words)
    bit_map = [0]*n

    for i in range(n):
        for c in words[i]:
            bit_map[i] |= 1<<(ord(c)-ord('a'))

    ans = 0

    for i in range(n):
        for j in range(i+1,n):
            if bit_map[i] & bit_map[j] == 0:
                ans = max(ans, len(words[i]) * len(words[j]))

    return ans



    print(keys)
if __name__ == "__main__":
    words = ['abcw',"baz","foo","bar","xtfn"]
    print(maxProduct(words))