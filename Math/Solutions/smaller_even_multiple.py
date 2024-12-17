# 2413 最小整数倍
def smallestEvenMultiple(n: int) -> int:
    max_num = max(n, 2)
    temp = max_num
    while True:
        if (temp % max_num == 0) and (temp % 2 == 0):
            break
        temp += 1
    return temp

if __name__ == '__main__':
    print(smallestEvenMultiple(5))