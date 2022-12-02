import bisect
from collections import defaultdict


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # NOTE:工厂方法defaultdict内需用list初始化，否则出现keyError
        # pos = defaultdict()
        pos = defaultdict(list)
        for i, v in enumerate(t):
            pos[v].append(i)
        p = -1
        for c in s:
            ps = pos[c]
            j = bisect.bisect_right(ps, p)
            if j == len(ps):
                return False
            p = ps[j]

        return True


def main():
    # 输入：s = "abc", t = "ahbgdc"
    # 输出：true
    solution1 = Solution()
    print(solution1.isSubsequence(s="abc", t="ahbgdc"))

    # 输入：s = "axc", t = "ahbgdc"
    # 输出：false
    solution2 = Solution()
    print(solution2.isSubsequence(s="axc", t="ahbgdc"))

    # 输入
    # "acb"
    # "ahbgdc"
    # 输出 true
    # 预期结果 false
    solution3 = Solution()
    print(solution3.isSubsequence(s="axc", t="ahbgdc"))


if __name__ == '__main__':
    main()
