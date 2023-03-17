from typing import List

"""
core mind:
滑动窗口问题：
给出一段数字，要求找出包含2个不同数字的最大区间长度。
该区间内只能包含这两个数字，这两个数字可以重复，但不能包含其他数字。
"""


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = {}
        left = 0
        right = 0
        res = 0

        for right, f in enumerate(fruits):
            window.setdefault(f, 0)
            window[f] += 1

            while len(window.keys()) > 2:
                window[fruits[left]] -= 1
                # NOTE：当左值减为0时，需从滑窗中移除该0值对应的key
                if window[fruits[left]] == 0: window.pop(fruits[left])
                left += 1

            res = max(res, right - left + 1)

        return res


def main():
    # 输入：fruits = [1,2,1]
    # 输出：3
    # 解释：可以采摘全部 3 棵树。
    solution1 = Solution()
    print(solution1.totalFruit(fruits=[1, 2, 1]))

    # 输入：fruits = [0,1,2,2]
    # 输出：3
    # 解释：可以采摘 [1,2,2] 这三棵树。
    # 如果从第一棵树开始采摘，则只能采摘 [0,1] 这两棵树。
    solution2 = Solution()
    print(solution2.totalFruit(fruits=[0, 1, 2, 2]))

    # 输入：fruits = [1,2,3,2,2]
    # 输出：4
    # 解释：可以采摘 [2,3,2,2] 这四棵树。
    # 如果从第一棵树开始采摘，则只能采摘 [1,2] 这两棵树。
    solution3 = Solution()
    print(solution3.totalFruit(fruits=[1, 2, 3, 2, 2]))

    # 输入：fruits = [3,3,3,1,2,1,1,2,3,3,4]
    # 输出：5
    # 解释：可以采摘 [1,2,1,1,2] 这五棵树。
    solution4 = Solution()
    print(solution4.totalFruit(fruits=[3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))


if __name__ == '__main__':
    main()
