import re
def vowel_spellchecker(wordlist,queries):
    words = {w:w for w in wordlist}
    cap = {w.lower():w for w in wordlist[::-1]}
    vowel = {re.sub("[aeiou]","#",w.lower()): w for w in wordlist[::-1] }

    return [ words.get(w) or cap.get(w.lower()) or vowel.get(re.sub("[aeiou]","#", w.lower()), "")  for w in queries]


if __name__ == "__main__":
    wordlist = ["KiTe","kite","hare","Hare"]
    queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]

    print(vowel_spellchecker(wordlist,queries))