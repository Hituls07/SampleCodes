
def mult(a,b):
    if a == 1:
        return a
    else:
        return a + a * (b-1)


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


print(factorial(10))



'''
Example 2
'''

def isPalindrome(s):

    def tochar(s):
        ans = ''
        for char in s.lower():
            if char in 'abcdefghijklmnopqrstuvwxyz':
                ans += char

        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(tochar(s))


print(isPalindrome('Was it a car or a cat I saw'))

