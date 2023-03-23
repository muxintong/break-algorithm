from typing import List


class Solution:
    """
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for temp in zip(*strs):
            if (len(set(temp)) == 1):
                res += temp[0]
            else:
                break
        return res


def main():
    # 输入：strs = ["flower","flow","flight"]
    # 输出："fl"
    solution1 = Solution()
    print(solution1.longestCommonPrefix(strs=["flower", "flow", "flight"]))

    # 输入：strs = ["dog","racecar","car"]
    # 输出：""
    # 解释：输入不存在公共前缀。
    solution2 = Solution()
    print(solution2.longestCommonPrefix(strs=["dog", "racecar", "car"]))


if __name__ == '__main__':
    main()
