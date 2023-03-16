class Solution:
    """
    对于某些非负整数 k ，如果交换 s1 中两个字母的位置恰好 k 次，能够使结果字符串等于 s2 ，则认为字符串 s1 和 s2 的 相似度为 k 。
    给你两个字母异位词 s1 和 s2 ，返回 s1 和 s2 的相似度 k 的最小值。
    """

    def kSimilarity(self, s1: str, s2: str) -> int:


def main():
    # 输入：s1 = "ab", s2 = "ba"
    # 输出：1
    solution1 = Solution()
    print(solution1.kSimilarity())

    # 输入：s1 = "abc", s2 = "bca"
    # 输出：2
    solution2 = Solution()
    print(solution2.kSimilarity())


if __name__ == '__main__':
    main()
