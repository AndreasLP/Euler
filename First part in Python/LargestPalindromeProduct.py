import isPalindrome
def LPP(n):
    palindromes =[]
    for i in range(10**(n-1),10**n):
        for j in range(10**(n-1),10**n):
            ij = i*j
            if isPalindrome.isPalindrome(ij): palindromes.append(ij)
    return max(palindromes)
