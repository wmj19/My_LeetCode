# 2011 执行操作后的数

from typing import List

def finalValueAfterOperations(operations: List[str]) -> int:
    return sum(1 if s[1] == '+' else -1 for s in operations)

if __name__ == '__main__':
    operations = ["X++", "--X", "X++", "X++"]
    operations_list = [1 if s[1] == '+' else -1 for s in operations]
    print(operations_list)
    print(sum(operations_list))
    print(finalValueAfterOperations(operations))