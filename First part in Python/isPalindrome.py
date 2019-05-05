def isPalindrome(n):
    numb = str(n)
    return test(numb)
def test(s):
    if len(s)<=1: return True
    if s[0]==s[-1]: return test(s[1:-1])
    return False
