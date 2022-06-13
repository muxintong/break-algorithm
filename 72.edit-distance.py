class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memory = dict()

        def dp(i: int, j: int) -> int:
            # base case
            if i == -1:
                res = j + 1
                return res
            if j == -1:
                res = i + 1
                return res

            # pre recursive:查memory
            if memory.get((i, j)): return memory[(i, j)]

            # recursive：结果写入memory
            # 1.指针i，j所指字符相等时：
            #                        i，j均前移一位，操作数（insert，delete，replace）不变
            if word1[i] == word2[j]:
                memory[(i, j)] = dp(i - 1, j - 1)
            # 2.指针i，j所指字符不等时：
            #                        操作数加一，指针移动位数依照具体的操作
            #                        dp(i, j - 1) + 1,  # insert
            #                        dp(i - 1, j) + 1,  # delete
            #                        dp(i - 1, j - 1) + 1  # replace
            else:
                memory[(i, j)] = min(
                    dp(i, j - 1) + 1,
                    dp(i - 1, j) + 1,
                    dp(i - 1, j - 1) + 1
                )
            # post recusive：返回memory[(i, j)]
            return memory[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)


def main():
    # Input: word1 = "horse", word2 = "ros"
    # Output: 3
    # Explanation:
    # horse -> rorse (replace 'h' with 'r')
    # rorse -> rose (remove 'r')
    # rose -> ros (remove 'e')
    solution1 = Solution()
    print(solution1.minDistance(word1="horse", word2="ros"))

    # Input: word1 = "intention", word2 = "execution"
    # Output: 5
    # Explanation:
    # intention -> inention (remove 't')
    # inention -> enention (replace 'i' with 'e')
    # enention -> exention (replace 'n' with 'x')
    # exention -> exection (replace 'n' with 'c')
    # exection -> execution (insert 'u')
    solution2 = Solution()
    print(solution2.minDistance(word1="intention", word2="execution"))


if __name__ == '__main__':
    main()
