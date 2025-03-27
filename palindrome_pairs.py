def palindromePairs(words):
    d = {word[::-1]:i for i,word in enumerate(words)}
    ans = []
    for i,word in enumerate(words):
        for j in range(len(word)+1):
            prefix = word[:j]
            postfix = word[j:]

            if prefix in d and d[prefix] != i and postfix == postfix[::-1]:
                ans.append([i,d[prefix]])

            if j>0 and postfix in d and d[postfix] != i and prefix == prefix[::-1]:
                ans.append([d[postfix],i])

    return ans



words = ["abcd","dcba","lls","s","sssll"]

print(palindromePairs(words))