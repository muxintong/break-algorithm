from collections import deque
from typing import List


class Solution2:
    """
    暴力法：2层循环，O(n*k)

    优化：单调队列，使用一个队列充当不断滑动的窗口，每次记录其中的最大值。
    在O(1)时间内计算最大值：使用单调队列。
    添加方法push依然向队尾添加元素，但是要把前面比自己小的元素都删除掉，
    直到遇到比自己大的元素才停止删除。
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MonotonicQueue([])
        res = []

        for i in range(len(nums)):
            # 先填满窗口的前k-1
            if i < k - 1:
                window.push(nums[i])
            # 维持一个大小为k的窗口不断向前滑动
            else:
                # 窗口向前滑动，加入新数字
                window.push(nums[i])
                # 记录当前窗口中的最大值
                res.append(window.max())
                # 移除左边界的旧数字
                window.pop(nums[i - k + 1])

        return res


class MonotonicQueue:
    def __init__(self, queue: list):
        self.q = queue

    def push(self, n: int):
        # 将小于n的元素全部删除
        while len(self.q) != 0 and self.q[-1] < n:
            self.q.pop()
        # 将n加入队尾
        self.q.append(n)

    def max(self):
        return self.q[0]

    def pop(self, n: int):
        if n == self.q[0]:
            self.q.pop(0)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(k - 1):
            while q and q[-1] < nums[i]: q.pop()
            q.append(nums[i])
            # print(q)
        # print("=========")
        for pop, push in zip(nums, nums[k - 1:]):
            while q and q[-1] < push: q.pop()
            q.append(push)
            res.append(q[0])
            if pop == q[0]:
                q.popleft()
            # print(q)
        return res


def main():
    # 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
    # 输出：[3,3,5,5,6,7]
    # 解释：
    # 滑动窗口的位置                最大值
    # ---------------               -----
    # [1  3  -1] -3  5  3  6  7       3
    #  1 [3  -1  -3] 5  3  6  7       3
    #  1  3 [-1  -3  5] 3  6  7       5
    #  1  3  -1 [-3  5  3] 6  7       5
    #  1  3  -1  -3 [5  3  6] 7       6
    #  1  3  -1  -3  5 [3  6  7]      7
    solution1 = Solution()
    print(solution1.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))

    # 输入：nums = [1], k = 1
    # 输出：[1]
    solution2 = Solution()
    print(solution2.maxSlidingWindow(nums=[1], k=1))


if __name__ == '__main__':
    main()
