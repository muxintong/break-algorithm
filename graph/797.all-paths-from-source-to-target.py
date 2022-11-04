from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = list()
        stk = list()

        def dfs(x: int):
            if x == len(graph) - 1:
                ans.append(stk[:])
                return

            for y in graph[x]:
                stk.append(y)
                dfs(y)
                stk.pop()

        stk.append(0)
        dfs(0)
        return ans

    def allPathsSourceTarget2(self, graph: List[List[int]]) -> List[List[int]]:
        """
        graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。
        """
        res=[]
        path=[]
        def traverse()


def main():
    # 输入：graph = [[1,2],[3],[3],[]]
    # 输出：[[0,1,3],[0,2,3]]
    # 解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3
    solution1 = Solution()
    print(solution1.allPathsSourceTarget(graph=[[1, 2], [3], [3], []]))

    # 输入：graph = [[4,3,1],[3,2,4],[3],[4],[]]
    # 输出：[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    solution2 = Solution()
    print(solution2.allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]))


if __name__ == '__main__':
    main()
