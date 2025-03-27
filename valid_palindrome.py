import re


def isPalindrome(s):
    s = re.findall("[a-zA-Z0-9]", s)
    s = "".join(s)
    if s.lower() == s[::-1].lower():
        return True
    return False


if __name__ == '__main__':
    test = "A man, a plan, a canal: Panama"
    print(isPalindrome(test))
