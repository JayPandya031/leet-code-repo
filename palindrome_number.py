def isPalindrome(x: int) -> bool:
    x = str(x)
    length = len(x)
    for i in range(length):
        if x[i] != x[length - i - 1]:
            return False
        
    return True

ret = isPalindrome(121)
print(ret)