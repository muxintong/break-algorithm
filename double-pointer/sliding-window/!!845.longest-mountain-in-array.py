from typing import List


class Solution:
    """
    把符合下列属性的数组 arr 称为 山脉数组 ：

    arr.length >= 3
    存在下标 i（0 < i < arr.length - 1），满足
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
    给出一个整数数组 arr，返回最长山脉子数组的长度。如果不存在山脉子数组，返回 0 。
    """
    def longestMountain(self, arr: List[int]) -> int:


def main():
    # 输入：arr = [2,1,4,7,3,2,5]
    # 输出：5
    # 解释：最长的山脉子数组是 [1,4,7,3,2]，长度为 5。
    solution1 = Solution()
    print(solution1.longestMountain(arr=[2, 1, 4, 7, 3, 2, 5]))
    # 输入：arr = [2,2,2]
    # 输出：0
    # 解释：不存在山脉子数组。
    solution2 = Solution()
    print(solution2.longestMountain(arr=[2, 2, 2]))


if __name__ == '__main__':
    main()
