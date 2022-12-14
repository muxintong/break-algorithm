from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0: return 0

        # 按points二维list第二列值升序排列
        points.sort(key=lambda x: x[1])

        # 最少射一箭
        arrows = 1
        # 排序后最小的end即为数组第一个元素，设其为x
        x_end = points[0][1]
        for point in points:
            start = point[0]
            # 边界算重叠，不带等，若满足此条件则找到下一个选择区间
            if start > x_end:
                arrows += 1
                x_end = point[1]
        return arrows


def main():
    # 输入：points = [[10,16],[2,8],[1,6],[7,12]]
    # 输出：2
    # 解释：气球可以用2支箭来爆破:
    # -在x = 6处射出箭，击破气球[2,8]和[1,6]。
    # -在x = 11处发射箭，击破气球[10,16]和[7,12]。
    solution1 = Solution()
    print(solution1.findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))

    # 输入：points = [[1,2],[3,4],[5,6],[7,8]]
    # 输出：4
    # 解释：每个气球需要射出一支箭，总共需要4支箭。
    solution1 = Solution()
    print(solution1.findMinArrowShots(points=[[1, 2], [3, 4], [5, 6], [7, 8]]))


if __name__ == '__main__':
    main()
