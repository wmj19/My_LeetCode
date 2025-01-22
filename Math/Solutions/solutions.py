import collections
from typing import *


class Solutions:

    # 2427.共因子的数量
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        min_num = min(a, b)
        for i in range(1, min_num + 1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count

    # 728.自除数
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            if isSelfDividingNumber(i):
                res.append(i)
        return res

    # 2119.反转两次的数字
    def isSameAfterReversals(self, num: int) -> bool:
        # reverse_once = reverseNumber(num)
        # # print(reverse_once)
        # reverse_twice = reverseNumber(reverse_once)
        # # print(reverse_twice)
        # if reverse_twice == num:
        #     return True
        # else:
        #     return False
        # 这个数字只要以0为结尾反转两次后一定不是和原数字相同的，只要不以0为结尾就一定是相同的
        return num % 10 > 0 or num == 0

def isSelfDividingNumber(num: int) -> bool:
    temp = num
    while temp:
        digit = temp % 10
        if digit == 0 or num % digit != 0:
            return False
        temp = temp // 10
    return True

def reverseNumber(num: int) -> int:
    stack = collections.deque()
    res = 0
    while num:
        stack.append(num % 10)
        num = num // 10
    while stack:
        num = stack.popleft()
        if num == 0 and res == 0:
            continue
        res = res * 10 + num
    return res

if __name__ == '__main__':
    print("公共因子数量".center(20, '='))
    print(Solutions().commonFactors(25, 30))
    print("自除数".center(20, '='))
    print(Solutions().selfDividingNumbers(47, 85))
    print("反转两次的数字".center(20, '='))
    print(Solutions().isSameAfterReversals(12300))
