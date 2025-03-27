def minimumLengthEncoding(words):
    s = set(words)  # to remove the duplicate

    for word in words:
        for j in range(1,len(word)):    # remove suffice for the word from set 
            s.discard(word[j:])

    return sum(len(w)+1 for w in s)     # +1 for # after each word.


if __name__ == '__main__':
    words = ["time","me","bell"]

    print(minimumLengthEncoding(words))