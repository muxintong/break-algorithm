from typing import List


class Solution:
    def merge_sort(self, nums, l, r):
        # 递归出口
        if l == r: return

        # recursive
        mid = (l + r) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid + 1, r)

        # postorder：归并排序等价于二叉树的后序遍历
        tmp = []
        i, j = l, mid + 1
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l: r + 1] = tmp

    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums


class Solution2:
    def __init__(self):
        self.temp = []

    def sortArray(self, nums: List[int]) -> List[int]:
        self.sorted(nums)
        return nums

    def sorted(self, nums: List[int]):
        self.temp = [0] * len(nums)
        self.sort(nums, 0, len(nums) - 1)

    def sort(self, nums: List[int], lo: int, hi: int):
        if lo == hi: return
        mid = (lo + hi) // 2
        self.sort(nums, lo, mid)
        self.sort(nums, mid + 1, hi)

        # postorder
        self.merge(nums, lo, mid, hi)

    def merge(self, nums: List[int], lo: int, mid: int, hi: int):
        self.temp = nums.copy()

        i = lo
        j = mid + 1
        for p in range(lo, hi + 1, 1):
            if i == mid + 1:
                nums[p] = self.temp[j]
                j += 1
            elif j == hi + 1:
                nums[p] = self.temp[i]
                i += 1
            elif self.temp[i] > self.temp[j]:
                nums[p] = self.temp[j]
                j += 1
            else:
                nums[p] = self.temp[i]
                i += 1


def main():
    # 输入：nums = [5,2,3,1]
    # 输出：[1,2,3,5]
    solution1 = Solution()
    print(solution1.sortArray(nums=[5, 2, 3, 1]))

    # 输入：nums = [5,1,1,2,0,0]
    # 输出：[0,0,1,1,2,5]
    solution1 = Solution()
    print(solution1.sortArray(nums=[5, 1, 1, 2, 0, 0]))


if __name__ == '__main__':
    main()
