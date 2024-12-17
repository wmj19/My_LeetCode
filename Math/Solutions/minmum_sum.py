# 2160 拆分数位后四位数字的最小和
def minimumSum(num: int) -> int:
    num_list = []
    while True:
        num_list.append(num % 10)
        num = num // 10
        if num < 10:
            num_list.append(num)
            break
    sorted_num = sorted(num_list)
    return (sorted_num[0] * 10 + sorted_num[2]) + (sorted_num[1] * 10 + sorted_num[3])

if __name__ == '__main__':
    print(minimumSum(4684))