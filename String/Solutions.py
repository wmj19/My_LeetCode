from typing import *

class Solutions:
    # 14.最长公共前缀
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        :param strs:
        :return:
        思路：
        把它看成一个二维数组！
        '''
        res = strs[0]
        for i, char in enumerate(res):
            for s in strs:
                if s[i] != char or i == len(res):
                    return res[:i]
        return res

    # 58.最后一个单词的长度
    def lengthOfLastWord(self, s: str) -> int:
        # length_of_last_word = 0
        # s = s.strip()
        # for c in s:
        #     if 'a'<= c <= 'z' or 'A' <= c <= 'Z':
        #         length_of_last_word += 1
        #     else:
        #         length_of_last_word = 0
        # return length_of_last_word
        last_word_end = len(s) - 1
        while s[last_word_end] == ' ':
            last_word_end -= 1

        last_word_start = last_word_end
        while last_word_start >= 0 and s[last_word_start] != ' ':
            last_word_start -= 1

        return last_word_end - last_word_start



if __name__ == '__main__':
    print(Solutions().longestCommonPrefix(["flower","flow","flight"]))
    print(Solutions().lengthOfLastWord("a"))