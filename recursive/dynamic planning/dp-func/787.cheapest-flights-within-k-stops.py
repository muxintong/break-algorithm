from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        indegree = {}  # to:[from,price]
        k += 1  # 将中转站个数转化为边的条数
        for f in flights:
            start = f[0]
            to = f[1]
            price = f[2]
            if indegree.get(to):
                indegree.get(to).append([start, price])
            else:
                indegree.setdefault(to, [[start, price]])

        memory = [[0] * (k + 1) for row in range(n)]

        # dp含义：从src出发，k步之内到达s的最短路径权重
        def dp(s, k):
            if s == src: return 0
            if k == 0: return -1

            # before recursive:find in memory
            if memory[s][k] != 0: return memory[s][k]
            # recursive
            res = 99999
            if indegree.get(s):
                for v in indegree.get(s):
                    start = v[0]
                    price = v[1]
                    sub_problem = dp(start, k - 1)
                    if sub_problem != -1:
                        res = min(res, sub_problem + price)
            # after recursive:write in memory
            if res == 99999:
                memory[s][k] = -1
            else:
                memory[s][k] = res

            return memory[s][k]

        return dp(dst, k)


def main():
    # 输入:
    # n = 3, flights=[[0,1,100],[1,2,100],[0,2,500]],src = 0, dst = 2, k = 1
    # 输出: 200
    solution1 = Solution()
    print(solution1.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1))

    # n = 3,flights=[[0,1,100],[1,2,100],[0,2,500]],src = 0, dst = 2, k = 0
    # 输出: 500
    solution2 = Solution()
    print(solution2.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0))


if __name__ == '__main__':
    main()
