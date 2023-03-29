class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m = len(ring)
        n = len(key)

        memory = [[0] * n for row in range(m)]
        char_indexs = {}
        for i in range(m):
            char_indexs.setdefault(ring[i], [i])
            char_indexs[ring[i]].append(i)

        # dp方法含义：
        # 当圆盘指针指向 ring[i] 时，输入字符串 key[j..] 至少需要 dp(ring, i, key, j) 次操作。
        def dp(i: int, j: int) -> int:
            # base case
            if j == n: return 0

            # before recursive:find in memory
            if memory[i][j] != 0: return memory[i][j]

            # recursive
            res = 99999
            for k in char_indexs.get(key[j]):
                # 拨动指针的次数
                counts = abs(k - i)
                # 顺时针 or 逆时针
                counts = min(counts, m - counts)
                # 将指针拨到ring[k]，继续输入key[j+1:]
                subproblem = dp(k, j + 1)
                # 选择整体操作数最少的，因按动按钮也是一次操作故加1
                res = min(res, counts + subproblem + 1)

            # after recursive:write in memory
            memory[i][j] = res

            return res

        return dp(0, 0)


def main():
    # 输入: ring = "godding", key = "gd"
    # 输出: 4
    # 解释:
    #  对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。
    #  对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。
    #  当然, 我们还需要1步进行拼写。
    #  因此最终的输出是 4
    solution1 = Solution()
    print(solution1.findRotateSteps(ring="godding", key="gd"))

    # 输入: ring = "godding", key = "godding"
    # 输出: 13
    solution2 = Solution()
    print(solution2.findRotateSteps(ring="godding", key="godding"))


if __name__ == '__main__':
    main()
