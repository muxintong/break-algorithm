from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        if time == 0: return 0
        # 对clips区间进行排序：按照起点升序排列，若起点相同则按终点降序排序
        clips.sort(key=lambda x: (x[0], -x[1]))

        # 记录选择的短视频个数
        res = 0
        curEnd = 0
        nextEnd = 0

        i = 0
        n = len(clips)
        while i < n and clips[i][0] <= curEnd:
            # 在第res个视频的区间内基于贪心规则选择下一个视频
            while i < n and clips[i][0] <= curEnd:
                nextEnd = max(nextEnd, clips[i][1])
                i += 1
            # 找到下一个视频，更新curEnd
            res += 1
            curEnd = nextEnd
            if curEnd >= time:
                # 已经可以拼凑出[0, time]，返回i结果
                return res
        # 无法拼凑出区间[0, time]
        return -1


def main():
    # 输入：clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
    # 输出：3
    # 解释：
    # 选中 [0,2], [8,10], [1,9] 这三个片段。
    # 然后，按下面的方案重制比赛片段：
    # 将 [1,9] 再剪辑为 [1,2] + [2,8] + [8,9] 。
    # 现在手上的片段为 [0,2] + [2,8] + [8,10]，而这些覆盖了整场比赛 [0, 10]。
    solution1 = Solution()
    print(solution1.videoStitching(clips=[[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], time=10))

    # 输入：clips = [[0,1],[1,2]], time = 5
    # 输出：-1
    # 解释：
    # 无法只用 [0,1] 和 [1,2] 覆盖 [0,5] 的整个过程。
    solution1 = Solution()
    print(solution1.videoStitching(clips=[[0, 1], [1, 2]], time=5))

    # 输入：clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9
    # 输出：3
    # 解释： 
    # 选取片段 [0,4], [4,7] 和 [6,9] 。
    solution1 = Solution()
    print(solution1.videoStitching(
        clips=[[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4],
               [4, 5], [5, 7], [6, 9]], time=9))


if __name__ == '__main__':
    main()
