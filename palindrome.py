def checkPalindrome(s):
    l = 0
    r = len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return False

        l+=1
        r-=1

    return True

n = str(input("Enter String to check for Palindrome: "))
if checkPalindrome(n):
    print("String is Palindrome.")
else:
    print("String is not Palindrome.")