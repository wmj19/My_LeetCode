# 我的
def isPalindrome(s: str) -> bool:
    str = ""
    for i in s:
        if i.isalpha() or i.isdigit():
            str += i
    str = str.lower()
    if len(str) % 2 == 0:
        left = str[:len(str) // 2]
        right = str[len(str) // 2:][::-1]
    else:
        left = str[:len(str) // 2]
        right = str[len(str) // 2 + 1:][::-1]
    if len(str) == 1:
        return True
    if left == right:
        return True
    else:
        return False

# 别人的
def otherIsPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    s1 = "A man, a plan, a canal: Panama"
    print(isPalindrome(s1))
    print(otherIsPalindrome(s1))
    s2 = "0P"
    print(isPalindrome(s2))
    print(otherIsPalindrome(s2))