"""
重叠子问题判定：如何判断暴力穷举解法中是否包含重叠子问题
1.画递归树：看是否有重复节点
2.仅抽象出算法的递归框架部分代码：
  判断不同状态下的状态转移路径有几条：
    若路径不唯一，则说明存在重叠子问题，需使用某一数据结构的备忘录记录子问题。
    若路径唯一，则说明不存在重叠子问题。

  本题递归框架：
  def dp(self, s: str, i: int, p: str, j: int) -> bool:
    dp(s, i, p, j + 2);     // #1
    dp(s, i + 1, p, j);     // #2
    dp(s, i + 1, p, j + 1); // #3
    dp(s, i, p, j + 2);     // #4

  从状态(i,j)转移到(i+2,j+2)的路径有：
    (i, j) -> #3 -> #3
    (i, j) -> #2 -> #2 -> #4
  路径不唯一，说明存在重叠子问题，需要使用备忘录进行优化。

"""


# 全局变量memory，在类内使用时需使用global关键字声明：global memory
# memory = dict()
class Solution:
    # 动归：递归+备忘录去重
    # 类变量memory,在使用时为Solution.memory
    memory = dict()

    # 成员变量memory，使用时为：self.memory
    # def __init__(self, memory: dict):
    #     self.memory = memory

    def isMatch(self, s: str, p: str) -> bool:
        # dp(s,i,p,j)返回True表示s[i:len(s)]匹配p[j:len(p)]
        # dp(s,i,p,j)返回False表示s[i:len(s)]不匹配p[j:len(p)]
        # NOTE：是从pointer->end是否匹配，而非从0->pointer是否匹配，
        #       【4.结束条件】故最终结果为i=0，j=0时dp方法的返回值。
        res = self.dp(s, 0, p, 0)
        return res

    def dp(self, s: str, i: int, p: str, j: int) -> bool:
        # 【1.base case】
        # i,j指针不移动时的递归出口
        if i == len(s) - 1:
            if j == len(p) - 1:
                return True
            elif j != len(p) - 1:
                if len(p) - j % 2 == 1: return False
                while j + 1 < len(p):
                    if p[j + 1] != '*': return False
                    j += 2
                return True
        if j == len(p) - 1:
            if i == len(s): return True
            if i != len(s): return False

        # i,j指针移动时的递归出口
        if i == len(s):
            if j == len(p):
                return True
            if j != len(p):
                if len(p) - j % 2 == 1: return False
                while j + 1 < len(p):
                    if p[j + 1] != '*': return False
                    j += 2
            return True
        if j == len(p):
            if i == len(s): return True
            if i != len(s): return False

        """
        【2.状态】：原问题和子问题中会变化的变量。
                   本题为状态为：i，j两个位置指针。
        【3.选择】：选择是导致状态发生变化的行为。
                   本题选择为：两个指针i，j依据不同匹配条件选择移动的步数。
        => 关键穷举 => 关键状态转移方程式 => 优化：去重
        1.递归：[自顶向下n->1] + [备忘录去重] *keypoint*:dp方法含义
        2.迭代（递推）：[自底向上，从1->n] + [dp数组] *keypoint*:dp数组含义
        """

        # 记录状态i，j消除重叠子问题
        key = (i, j)
        # 全局变量memory：global memory
        #               全局变量memory应置于类外。
        #               首先应声明memory是一个全局变量，然后才可使用该变量，若无全局性声明，则认为该变量是一个局部变量。
        # 成员变量memory：self.memory
        #               成员变量应置于类的__init__(self, ...)方法中。
        # 类变量memory：Solution.memory
        #               类变量应置于类内，类方法外。
        if Solution.memory.get(key): return Solution.memory[key]

        res = False

        # recursive：
        # 本题依据是否匹配进行穷举：
        # 1.s[i] p[j]: match
        if s[i] == p[j] or p[j] == '.':
            # NOTE:移动指针前需先进行越界判断
            if j < len(p) - 1 and p[j + 1] != '*':
                res = self.dp(s, i + 1, p, j + 1)
            elif j < len(p) - 1 and p[j + 1] == '*':
                res = (self.dp(s, i, p, j + 2) or self.dp(s, i + 1, p, j))
        # 2.s[i] p[j]: unmatch
        else:
            if j < len(p) - 1 and p[j + 1] != '*':
                res = False
            elif j < len(p) - 1 and p[j + 1] == '*':
                res = self.dp(s, i, p, j + 2)

        # 将当前结果记入备忘录
        Solution.memory[key] = res

        return res


def main():
    # Input: s = "aa", p = "a"
    # Output: false
    # Explanation: "a" does not match the entire string "aa".
    solution1 = Solution()
    print(solution1.isMatch(s="aa", p="a"))

    # Input: s = "aa", p = "a*"
    # Output: true
    # Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
    solution2 = Solution()
    print(solution2.isMatch(s="aa", p="a*"))

    # Input: s = "ab", p = ".*"
    # Output: true
    # Explanation: ".*" means "zero or more (*) of any character (.)".
    solution3 = Solution()
    print(solution3.isMatch(s="ab", p=".*"))

    # "aab" "c*a*b"
    # 输出：false
    # 预期结果：true
    solution4 = Solution()
    print(solution4.isMatch(s="aab", p="c*a*b"))


if __name__ == '__main__':
    main()
