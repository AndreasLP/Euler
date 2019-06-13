def is_palindrome(s):
    if len(s)==0 or len(s)==1:
        return True
    for i in range(0,int(len(s)/2)):
        if s[i]!=s[-(i+1)]:
            return False
    return True    
