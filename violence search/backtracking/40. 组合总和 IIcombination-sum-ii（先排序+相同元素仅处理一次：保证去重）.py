from typing import List


class Solution:
    '''
    （先排序+相同元素仅处理一次：保证去重）
    先对输入列表排序，在回溯算法的递归调用中通过对相同元素只处理一次的方法进行去重
    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 最终结果集res：存储各个track
        res = []
        # 路径列表track：存储符合题意的选择i对应的值candidates[i]
        track = []
        track_sum = 0
        # 组合|子集类问题：
        # 使用起始位start保证元素顺序=>从而保证结果子集与元素顺序无关，为组合型问题，而非排列型问题。
        start = 0

        # 去重保证：1.排序
        candidates.sort()

        def backtrack(start: int, track_sum: int):
            # 1 递归出口
            if track_sum == target:
                res.append(track.copy())
                # return

            for i in range(start, len(candidates), 1):
                # 去重保证：2.排序后，针对相同元素仅处理一次
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                # 2.1 选择判断：是否符合题意
                # 若不符合：
                if candidates[i] + track_sum > target:
                    continue
                # 若符合：
                elif candidates[i] + track_sum <= target:
                    track_sum += candidates[i]
                    track.append(candidates[i])

                # 2.2 递归
                backtrack(i + 1, track_sum)

                # 2.3 递归后撤销符合题意的选择
                track.remove(candidates[i])
                track_sum -= candidates[i]

        backtrack(start, track_sum)
        return res
    
    def combinationSum2_TimeLimitError(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        track = []
        track_sum = 0
        start = 0

        def backtrack(start: int, track_sum: int):
            # 1.递归出口
            if track_sum == target:
                res.append(track.copy())
                return

                # 2.组合|子集类问题使用起始位start保证元素顺序
            for i in range(start, len(candidates), 1):
                # 2.1 判断选择i是否符合题意
                # 若不符合
                if track_sum + candidates[i] > target:
                    continue
                # 若符合:做选择
                else:
                    track.append(candidates[i])
                    track_sum += candidates[i]
                # 2.2 递归
                backtrack(i + 1, track_sum)
                # 2.3 递归后撤销选择
                track.remove(candidates[i])
                track_sum -= candidates[i]

        backtrack(start, track_sum)
        # 针对res去重
        res = [sorted(i) for i in res]
        res_tup_nodup = list(set([tuple(i) for i in res]))
        res_list_nodup = [list(i) for i in res_tup_nodup]
        return res_list_nodup


def main():
    # Input: candidates = [10,1,2,7,6,1,5], target = 8
    # Output:
    # [
    # [1,1,6],
    # [1,2,5],
    # [1,7],
    # [2,6]
    # ]
    solution1 = Solution()
    print(solution1.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))

    print('---')

    # Input: candidates = [2,5,2,1,2], target = 5
    # Output:
    # [
    # [1,2,2],
    # [5]
    # ]
    solution2 = Solution()
    print(solution2.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))


if __name__ == '__main__':
    main()
