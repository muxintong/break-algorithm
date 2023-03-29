from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 最终结果集result：存储board
        res = []

        # 符合题意的选择列表指针集：存储符合题意的选择列表指针row 对应的值
        # board存储的数据结构[".Q..","...Q","Q...","..Q."]
        board = [['.'] * n for i in range(n)]

        def isValid(board: List, row: int, column: int) -> bool:
            # 1.该格所在的整列不能有Q
            for i in range(n):
                if board[i][column] == 'Q':
                    return False
            # 2.该格左上连线不能有Q
            i = row - 1
            j = column - 1
            while i >= 0 and j >= 0:  # NOTE:边界条件取值范围，是否带等
                if board[i][j] == 'Q':
                    return False
                else:
                    i -= 1
                    j -= 1
            # 3.该格右上连线不能有Q
            i = row - 1
            j = column + 1
            while i >= 0 and j <= n - 1:
                if board[i][j] == 'Q':
                    return False
                else:
                    i -= 1
                    j += 1
            return True

        def backtrack(board: List, row: int):
            # 1.回溯出口：找到一个满足条件的board
            if row == len(board):
                board_str = [''.join(list_i) for list_i in board]
                res.append(board_str)
                return

            for column in range(n):
                # 1. 选择判断：不符合 or 符合 题意
                # 1.1 针对不符合题意的选择：
                if isValid(board, row, column) == False:
                    continue
                # 1.2 针对符合题意的选择：记录在board中
                board[row][column] = 'Q'

                # 2. 核心递归过程：进入下一层决策树,即在下一行放皇后Q
                backtrack(board, row + 1)

                # 3.递归后：撤销选择，将针对符合题意的选择从board中移除
                board[row][column] = '.'

        # 选择列表 行指针row 从0向下一次移动
        backtrack(board, 0)
        return res


def main():
    # Input: n = 4
    # Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    # Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
    solution1 = Solution()
    print(solution1.solveNQueens(n=4))

    # Input: n = 1
    # Output: [["Q"]]
    solution2 = Solution()
    print(solution2.solveNQueens(n=1))


if __name__ == '__main__':
    main()
