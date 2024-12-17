def numberOfMatches(n: int) -> int:
    remain = n
    count = 0
    while remain != 1:
        if remain % 2 == 0:
            count += remain / 2
            remain = remain / 2
        else:
            count += (remain - 1) / 2
            remain = (remain - 1) / 2 + 1

    return int(count)

if __name__ == '__main__':
    print(numberOfMatches(10))