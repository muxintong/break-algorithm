from typing import List


class Solution:
    '''
    给你一个由数字和运算符组成的字符串 expression ，按不同优先级组合数字和运算符，
    计算并返回所有可能组合的结果。你可以 按任意顺序 返回答案。
    '''

    memory = dict()

    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        # before recursive: find in memory
        if self.memory.get(expression) is not None:
            return self.memory[expression]

        for i in range(len(expression)):
            c = expression[i]
            if c == "+" or c == "-" or c == "*":
                # 【分】：以运算符为中心，分割成两组字符串，分别递归处理
                left = self.diffWaysToCompute(expression[0:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                # 【治】：通过子问题结果合并成原问题结果
                for l in left:
                    for r in right:
                        if c == "+":
                            res.append(l + r)
                        elif c == "-":
                            res.append(l - r)
                        else:
                            res.append(l * r)

        # base case：如果res为空，则说明表达式为单个数字，没有运算符，为递归出口条件
        if len(res) == 0: res.append(int(expression))

        # after recursive: write in memory
        self.memory[expression] = res

        return res


def main():
    # 输入：expression = "2-1-1"
    # 输出：[0,2]
    # 解释：
    # ((2-1)-1) = 0
    # (2-(1-1)) = 2
    solution1 = Solution()
    print(solution1.diffWaysToCompute(expression="2-1-1"))

    # 输入：expression = "2*3-4*5"
    # 输出：[-34,-14,-10,-10,10]
    # 解释：
    # (2*(3-(4*5))) = -34
    # ((2*3)-(4*5)) = -14
    # ((2*(3-4))*5) = -10
    # (2*((3-4)*5)) = -10
    # (((2*3)-4)*5) = 10
    solution2 = Solution()
    print(solution2.diffWaysToCompute(expression="2*3-4*5"))


if __name__ == '__main__':
    main()
