from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # 两个集合的索引指针p1、p2
        p1 = 0
        p2 = 0

        res = []
        while p1 < len(firstList) and p2 < len(secondList):
            left1, right1 = firstList[p1][0], firstList[p1][1]
            left2, right2 = secondList[p2][0], secondList[p2][1]
            # 两个区间存在交集的条件
            if left1 <= right2 and right1 >= left2:
                # 计算出交集加入到结果集
                res.append([max(left1, left2), min(right1, right2)])
            # 指针前移：右侧边界值小的指针前移
            if right2 < right1:
                p2 += 1
            elif right1 < right2:
                p1 += 1

        return res


def main():
    # 输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
    # 输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    solution1 = Solution()
    print(solution1.intervalIntersection(firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
                                         secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]))

    # 输入：firstList = [[1,3],[5,9]], secondList = []
    # 输出：[]
    solution1 = Solution()
    print(solution1.intervalIntersection(firstList=[[1, 3], [5, 9]], secondList=[]))

    # 输入：firstList = [], secondList = [[4,8],[10,12]]
    # 输出：[]
    solution1 = Solution()
    print(solution1.intervalIntersection(firstList=[], secondList=[[4, 8], [10, 12]]))

    # 输入：firstList = [[1,7]], secondList = [[3,10]]
    # 输出：[[3,7]]
    solution1 = Solution()
    print(solution1.intervalIntersection(firstList=[[1, 7]], secondList=[[3, 10]]))


if __name__ == '__main__':
    main()
