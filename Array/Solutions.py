import math
from typing import *

class Solutions:
    # 2574.左右元素和的差值
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # leftSum = []
        # rightSum = []
        # for i in range(len(nums)):
        #     leftSum.append(sum_of_array('left', i, nums))
        #     rightSum.append(sum_of_array('right', i, nums))
        # return [abs(leftSum[i] - rightSum[i]) for i in range(len(nums))]
        left_sum, right_sum = 0, sum(nums)
        for i, x in enumerate(nums):
            right_sum -= x
            nums[i] = abs(left_sum - right_sum)
            left_sum += x
        return nums
    # 作者：灵茶山艾府
    # 链接：https: // leetcode.cn / problems / left - and -right - sum - differences / solutions / 2134217 / mo - ni - jian - ji - xie - fa - by - endlesscheng - utdr /
    # 来源：力扣（LeetCode）

    # LCP01.猜数字
    def game(self, guess: List[int], answer: List[int]) -> int:
        # right = 0
        # for i in range(len(guess)):
        #     if guess[i] == answer[i]:
        #         right += 1
        # return right
        return sum([guess[i] == answer[i] for i in range(len(guess))])

    # LCP06.拿硬币
    def minCount(self, coins: List[int]) -> int:
        # math.ceil()向上取整函数
        return sum([math.ceil(item/2) for item in coins])


def sum_of_array(pos, index, array) -> int:
    sum = 0
    if pos == 'left':
        if index == 0:
            return 0
        for i in range(0, index):
            sum += array[i]
    elif pos == 'right':
        if index == len(array)-1:
            return 0
        for i in range(index+1, len(array)):
            sum += array[i]
    return sum

if __name__ == '__main__':
    print(Solutions().leftRightDifference([1]))
    print(Solutions().game([3, 2, 1], [1, 2, 3]))
    print(Solutions().minCount([2, 3, 10]))