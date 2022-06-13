from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        res = [0] * m
        for i in range(m):
            j = nums2.index(nums1[i])
            k = j + 1
            while k < n and nums2[k] < nums2[j]:
                k += 1
            res[i] = nums2[k] if k < n else -1
        return res


def main():
    # 输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
    # 输出：[-1,3,-1]
    # 解释：nums1 中每个值的下一个更大元素如下所述：
    # - 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
    # - 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
    # - 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
    solution1 = Solution()
    print(solution1.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))

    print('---')

    # 输入：nums1 = [2,4], nums2 = [1,2,3,4].
    # 输出：[3,-1]
    # 解释：nums1 中每个值的下一个更大元素如下所述：
    # - 2 ，用加粗斜体标识，nums2 = [1,2,3,4]。下一个更大元素是 3 。
    # - 4 ，用加粗斜体标识，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1 。
    solution2 = Solution()
    print(solution2.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))


if __name__ == '__main__':
    main()
