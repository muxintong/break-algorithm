from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 按起点值升序排列，若起点值相同按终点值降序排列
        intervals.sort(key=lambda x: (x[0], -x[1]))

        # 记录合并区间的起点和终点
        start = intervals[0][0]
        end = intervals[0][1]

        res = 0
        for interval in intervals:
            # 1.覆盖区间，覆盖结果值加1
            if start <= interval[0] and end >= interval[1]:
                res += 1
            # 2.相交区间，合并
            elif end >= interval[0] and end <= interval[1]:
                end = interval[1]
            # 3.不相交区间，更新起点和终点值
            elif end < interval[0]:
                start = interval[0]
                end = interval[1]

        # 对于初始区间在循环内多算了一次覆盖res值
        return len(intervals) - res + 1


def main():
    # 输入：intervals = [[1,4],[3,6],[2,8]]
    # 输出：2
    # 解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。
    solution1 = Solution()
    print(solution1.removeCoveredIntervals(intervals=[[1, 4], [3, 6], [2, 8]]))


if __name__ == '__main__':
    main()
