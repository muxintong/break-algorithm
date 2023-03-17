from typing import List


class Solution:
    """
    给定数组 people 。people[i]表示第 i 个人的体重 ，船的数量不限，
    每艘船可以承载的最大重量为 limit。
    每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
    返回 承载所有人所需的最小船数 。
    class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 0:
            return 0
        people.sort()
        i = 0
        j = len(people) - 1
        res = 0
        while (i <= j):
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            res += 1
        return res
    """

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 0: return 0
        people.sort()
        l = 0
        r = len(people) - 1
        res = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            elif people[l] + people[r] > limit:
                r -= 1
            res += 1
        return res


def main():
    # 输入：people = [1,2], limit = 3
    # 输出：1
    # 解释：1 艘船载 (1, 2)
    solution1 = Solution()
    print(solution1.numRescueBoats(people=[1, 2], limit=3))

    # 输入：people = [3,2,2,1], limit = 3
    # 输出：3
    # 解释：3 艘船分别载 (1, 2), (2) 和 (3)
    solution2 = Solution()
    print(solution2.numRescueBoats(people=[3, 2, 2, 1], limit=3))

    # 输入：people = [3,5,3,4], limit = 5
    # 输出：4
    # 解释：4 艘船分别载 (3), (3), (4), (5)
    solution3 = Solution()
    print(solution3.numRescueBoats(people=[3, 5, 3, 4], limit=5))


if __name__ == '__main__':
    main()
