class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        # Note:不能初始化为window=need=dict(),否则二者指向同一对象，即：不同变量分开初始化！
        window = dict()
        need = dict()
        for c in t:
            need.setdefault(c, 0)
            need[c] += 1
        # print(need)

        left = 0
        right = 0
        valid = 0

        min_len = len(s) + 1
        min_str = ""
        # expand window:
        # Note:enumerate只能用于for循环，不能用于while循环
        for right, in_win_char in enumerate(s):
            # right：右窗口指针，右移扩大窗口
            # win_in_char：移入窗口中的字符

            # update window
            if in_win_char in need.keys():
                window.setdefault(in_win_char, 0)
                # print("window[%c]:%d\n" % (in_win_char,window[in_win_char]))
                window[in_win_char] += 1
                # print("window[%c]:%d\n" % (in_win_char,window[in_win_char]))

                if window[in_win_char] == need[in_win_char]:
                    valid += 1
                    # print("window[%c]:%d\n" % (in_win_char,window[in_win_char]))
                    # print("need[%c]:%d\n" % (in_win_char,need[in_win_char]))
                    # print("valid:%d\n" % valid)

            # debug position
            # print("window:[%d, %d)\n" % (left, right))

            # shrink window:找到可行解时，通过收缩窗口这一动作优化可行解，使其向最优解收缩
            while (valid == len(need)):
                # update answer
                if right - left < min_len:
                    min_len = right - left
                    min_str = s[left:right + 1]

                # out_win_char：移出窗口中的字符
                out_win_char = s[left]
                # left：左窗口指针，右移缩小窗口
                left += 1
                if out_win_char in need.keys():
                    if window[out_win_char] == need[out_win_char]:
                        valid -= 1
                    window[out_win_char] -= 1

        return min_str


def main():
    # 输入：s = "ADOBECODEBANC", t = "ABC"
    # 输出："BANC"
    solution1=Solution()
    print(solution1.minWindow("ADOBECODEBANC", "ABC"))
    print('---')

    # 输入：s = "a", t = "a"
    # 输出："a"
    solution2=Solution()
    print(solution2.minWindow("a", "a"))
    print('---')

    # 输入: s = "a", t = "aa"
    # 输出: ""
    # 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
    # 因此没有符合条件的子字符串，返回空字符串。
    solution3=Solution()
    print(solution3.minWindow("a", "aa"))
    print('---')

    # wrong answer
    # i:aa
    # o:a
    # e:aa
    # wrong reason：初始化为window=need=dict(),二者指向同一对象。
    solution2=Solution()
    print(solution2.minWindow("aa", "aa"))

if __name__ == '__main__':
    main()
