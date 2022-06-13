from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        res = [0] * length
        stack = []
        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
        return res


def main():
    # 输入: temperatures = [73,74,75,71,69,72,76,73]
    # 输出: [1,1,4,2,1,1,0,0]
    solution1 = Solution()
    print(solution1.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))

    print('---')

    # 输入: temperatures = [30,40,50,60]
    # 输出: [1,1,1,0]
    solution2 = Solution()
    print(solution2.dailyTemperatures(temperatures=[30, 40, 50, 60]))

    print('---')

    # 输入: temperatures = [30,60,90]
    # 输出: [1,1,0]
    solution3 = Solution()
    print(solution3.dailyTemperatures(temperatures=[30, 60, 90]))


if __name__ == '__main__':
    main()
