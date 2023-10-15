def palindrome(w):
    if w[::-1] == w:
        return True
    else:
        return False
w = palindrome(input())
print(w)