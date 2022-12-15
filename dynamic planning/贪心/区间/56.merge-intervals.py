from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 按区间的start升序排列
        intervals.sort(key=lambda x: x[0])

        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            curr = intervals[i]
            # res中最后一个元素的索引
            last = res[-1]
            if curr[0] <= last[1]:
                # 找到最大的end
                last[1] = max(last[1], curr[1])
            else:
                # 处理下一个带合并区间
                res.append(curr)
        return res


def main():
    # 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
    # 输出：[[1,6],[8,10],[15,18]]
    # 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
    solution1 = Solution()
    print(solution1.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))

    # 输入：intervals = [[1,4],[4,5]]
    # 输出：[[1,5]]
    # 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
    solution1 = Solution()
    print(solution1.merge(intervals=[[1, 4], [4, 5]]))


if __name__ == '__main__':
    main()
