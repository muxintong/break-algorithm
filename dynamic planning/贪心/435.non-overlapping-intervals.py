from typing import List

"""
python多维list：按特定列排序
二维数组按第一列升序排序：
    ll.sort(key=lambda x:x[0])
    
二维数组按第二列降序排序：
    ll.sort(key=lambda x:-x[1])
    
二维数组按第一列升序排序，若第一列值一样，则按照第二列降序排列：
    ll.sort(key=lambda x:(x[0], -x[1])
    
"""


class Solution:
    def max_overlap_intervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0: return 0

        # 按照end，即二维数组第二列升序排列
        intervals.sort(key=lambda x: x[1])

        # 至少有一个区间不相交
        count = 1
        # 排序后最小的end即为第一个区间，设其为x
        x_end = intervals[0][1]
        for interval in intervals:
            start = interval[0]
            # 边界不算重叠，带等
            if start >= x_end:
                # 找到下一个选择区间
                count += 1
                x_end = interval[1]

        return count

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        return len(intervals) - self.max_overlap_intervals(intervals)


def main():
    # 输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
    # 输出: 1
    # 解释: 移除 [1,3] 后，剩下的区间没有重叠。
    solution1 = Solution()
    print(solution1.eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]))

    # 输入: intervals = [ [1,2], [1,2], [1,2] ]
    # 输出: 2
    # 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
    solution1 = Solution()
    print(solution1.eraseOverlapIntervals(intervals=[[1, 2], [1, 2], [1, 2]]))


if __name__ == '__main__':
    main()
