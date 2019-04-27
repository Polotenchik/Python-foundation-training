def isPalindrome(str):
    i = 0
    j = len(str) - 1

    while j - i >= i:
        if str[j - i] == str[i]:
            i = i + 1
        else:
            return 'false'
            break

    return 'true'

print(isPalindrome('radar'))
print(isPalindrome('madam'))
print(isPalindrome('kayaks'))
print(isPalindrome('kayak'))

input()