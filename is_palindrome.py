def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    x_str = str(x)
    for i in range(len(x_str)):
        if x_str[i] != x_str[-1-i]:
            return False
    return True
