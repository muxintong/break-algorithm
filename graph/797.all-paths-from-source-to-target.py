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
        给你一个有 n 个节点的 有向无环图（DAG），
        请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）
        graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。
        """
        res = []
        path = []
        n = len(graph)

        def traverse(s: int) -> None:
            # 递归出口：
            # if s == n - 1:
            if s == n - 1:
                res.append(path.copy())
                return
            # 递归前：做选择
            path.append(s)
            # recursive:递归每个相邻节点
            for v in graph[s]:
                traverse(v)
            # 递归后：撤销选择
            path.remove(s)

        traverse(0)
        return res


def main():
    # 输入：graph = [[1,2],[3],[3],[]]
    # 输出：[[0,1,3],[0,2,3]]
    # 解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3
    solution1 = Solution()
    print(solution1.allPathsSourceTarget2(graph=[[1, 2], [3], [3], []]))

    # 输入：graph = [[4,3,1],[3,2,4],[3],[4],[]]
    # 输出：[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    solution2 = Solution()
    print(solution2.allPathsSourceTarget2(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]))


if __name__ == '__main__':
    main()
