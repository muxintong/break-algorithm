from typing import List


class Solution:
    '''
    【子集/组合（元素无重可复选）】
        1.标准的子集/组合问题是如何保证【不重复使用】元素的？
            backtrack 递归时输入的参数 start：
            这个 i 从 start 开始，那么下一层回溯树就是从 【i+1】 开始，从而保证 nums[start] 这个元素不会被重复使用。
        2.那么反过来，如果我想让每个元素被【重复使用】，我只要把 i + 1 改成 【i】 即可：
            这相当于给之前的回溯树添加了一条树枝，在遍历这棵树的过程中，一个元素可以被无限次使用：
            当然，这样这棵回溯树会永远生长下去，所以我们的递归函数需要设置合适的base case以结束算法，即路径和大于 target 时就没必要再遍历下去了。
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        track = []
        track_sum = 0
        start = 0

        def backtrack(start: int, track_sum: int):
            # base case：递归出口1
            if track_sum == target:
                res.append(track.copy())
                return
            # base case：递归出口2
            if track_sum > target:
                return

            for i in range(start, len(candidates), 1):
                if candidates[i] + track_sum > target:
                    continue
                elif candidates[i] + track_sum <= target:
                    track_sum += candidates[i]
                    track.append(candidates[i])

                # keypoint：若元素可重复使用，则递归调用仍从i开始。
                backtrack(i, track_sum)

                track_sum -= candidates[i]
                track.remove(candidates[i])

        backtrack(start, track_sum)
        return res


def main():
    # Input: candidates = [2,3,6,7], target = 7
    # Output: [[2,2,3],[7]]
    # Explanation:
    # 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    # 7 is a candidate, and 7 = 7.
    # These are the only two combinations.
    solution1 = Solution()
    print(solution1.combinationSum(candidates=[2, 3, 6, 7], target=7))

    print('---')

    # Input: candidates = [2,3,5], target = 8
    # Output: [[2,2,2,2],[2,3,3],[3,5]]
    solution2 = Solution()
    print(solution2.combinationSum(candidates = [2,3,5], target = 8))

    print('---')

    # Input: candidates = [2], target = 1
    # Output: []
    solution3 = Solution()
    print(solution3.combinationSum(candidates = [2], target = 1))


if __name__ == '__main__':
    main()
