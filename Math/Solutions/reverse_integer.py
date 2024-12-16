def reverse(x: int) -> int:
    flag = 1
    if x < 0:
        flag = 0
        x = x * -1
    num = []
    while (x >= 10):
        temp = x % 10
        # print(temp)
        num.append(temp)
        x = x // 10
    num.append(x)
    res = 0
    for i in num:
        # print(i)
        res += i
        res *= 10
    res = int(res / 10)
    if flag == 0:
        res = res * -1
    return res if -2147483648 < res < 2147483647 else 0

if __name__ == "__main__":
    res01 = reverse(-123)
    res02 = reverse(-1289593023)
    res03 = reverse(20020419)
    res04 = reverse(20021024)
    print(f"res01 = {res01}")
    print(f"res02 = {res02}")
    print(f"res03 = {res03}")
    print(f"res04 = {res04}")
