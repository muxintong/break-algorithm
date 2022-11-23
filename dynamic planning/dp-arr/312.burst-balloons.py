from typing import List
'''
这个动态规划问题特别之处：
这个问题中我们每戳破一个气球nums[i]，得到的分数和该气球相邻的气球nums[i-1]和nums[i+1]是有相关性的。
运用动态规划算法的一个重要条件：【子问题必须独立】
所以对于这个戳气球问题，如果想用动态规划，必须巧妙地定义dp数组的含义，避免子问题产生相关性，才能推出合理的状态转移方程。
如何定义dp数组呢，这里需要对问题进行一个简单地转化。

题目说果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。 
那么我们先直接把这两个边界加进去，形成一个新的数组points：
现在气球的索引变成了从1到n，points[0]和points[n+1]可以认为是两个「虚拟气球」。

那么我们可以改变问题：在一排气球points中，请你戳破气球0和气球n+1之间的所有气球（不包括0和n+1），
使得最终只剩下气球0和气球n+1两个气球，最多能够得到多少分？

现在可以定义dp数组的含义：
dp[i][j] = x表示，戳破气球i和气球j之间（开区间，不包括i和j）的所有气球，可以获得的最高分数为x。

那么根据这个定义，题目要求的结果就是dp[0][n+1]的值，
而 base case 就是dp[i][j] = 0，其中0 <= i <= n+1, j <= i+1，因为这种情况下，开区间(i, j)中间根本没有气球可以戳。

要根据这个dp数组来推导状态转移方程了，所谓的推导「状态转移方程」，实际上就是在思考怎么「做选择」，也就是这道题目最有技巧的部分：
不就是想求戳破气球i和气球j之间的最高分数吗，如果「正向思考」，就只能写出回溯算法；
int res = Integer.MIN_VALUE;
/* 输入一组气球，返回戳破它们获得的最大分数 */
int maxCoins(int[] nums) {
    backtrack(nums, 0);
    return res;
}
/* 回溯算法的伪码解法 */
void backtrack(int[] nums, int socre) {
    if (nums 为空) {
        res = max(res, score);
        return;
    }
    for (int i = 0; i < nums.length; i++) {
        int point = nums[i-1] * nums[i] * nums[i+1];
        int temp = nums[i];
        // before recursive：做选择
        在 nums 中删除元素 nums[i]
        // recursive
        backtrack(nums, score + point);
        // after recursive：撤销选择
        将 temp 还原到 nums[i]
    }
}
我们需要「反向思考」，想一想气球i和气球j之间最后一个被戳破的气球可能是哪一个？

其实气球i和气球j之间的所有气球都可能是最后被戳破的那一个，不防假设为k。
这里其实已经找到了「状态」和「选择」：i和j就是两个「状态」，最后戳破的那个气球k就是「选择」。

根据刚才对dp数组的定义，如果最后一个戳破气球k，dp[i][j]的值应该为：
dp[i][j] = dp[i][k] + dp[k][j] + points[i]*points[k]*points[j]

你不是要最后戳破气球k吗？那得先把开区间(i, k)的气球都戳破，再把开区间(k, j)的气球都戳破；
最后剩下的气球k，相邻的就是气球i和气球j，这时候戳破k的话得到的分数就是points[i]*points[k]*points[j]。
那么戳破开区间(i, k)和开区间(k, j)的气球最多能得到的分数是多少呢？
就是dp[i][k]和dp[k][j]，这恰好就是我们对dp数组的定义.

dp数组定义：关键点为开区间 => 开区间可做到动规必要条件：子问题之间互相独立；
由于是开区间，dp[i][k]和dp[k][j]不会影响气球k，
而戳破气球k时，旁边相邻的就是气球i和气球j了，
最后还会剩下气球i和气球j，这也恰好满足了dp数组开区间的定义。

那么，对于一组给定的i和j，我们只要穷举i < k < j的所有气球k，选择得分最高的作为dp[i][j]的值即可，这也就是状态转移方程：
// 最后戳破的气球是哪个？
for (int k = i + 1; k < j; k++) {
    // 择优做选择，使得 dp[i][j] 最大
    dp[i][j] = Math.max(
        dp[i][j], 
        dp[i][k] + dp[k][j] + points[i]*points[j]*points[k]
    );
}

写出状态转移方程就完成这道题的一大半了，但是还有问题：对于k的穷举仅仅是在做「选择」，但是应该如何穷举「状态」i和j呢？
for (int i = ...; ; )
    for (int j = ...; ; )
        for (int k = i + 1; k < j; k++) {
            dp[i][j] = Math.max(
                dp[i][j], 
                dp[i][k] + dp[k][j] + points[i]*points[j]*points[k]
            );
return dp[0][n+1];

状态转移关键点：
穷举状态时，状态转移所依赖的状态必须事先被计算出来。
依据【base case】+ 【最终状态：即题目要求结果】进行推导。
做法：把已知的base case以及要求的最终状态在dp table中画出，从已知（base case）-> 未知（最终状态）即为状态遍历路径。

'''

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        points = [1] * (n + 2)
        for i in range(1, n + 1, 1):
            points[i] = nums[i - 1]

        # dp[i][j] = x表示，戳破气球i和气球j之间（开区间，不包括i和j）的所有气球，可以获得的最高分数为x。
        # base case 已经都被初始化为 0
        dp = [[0] * (n + 2) for row in range(n + 2)]

        # 穷举状态i，j:由已知状态【base case】推导【最终状态dp[0][n + 1]】
        # i：自下而上
        for i in range(n, -1, -1):
            # j：自左向右
            for j in range(i + 1, n + 2, 1):
                # 在开区间(i,j)内是否选择一个气球k进行戳破
                # 不戳破：dp[i][j]
                # 戳破：dp[i][k] + dp[k][j] + points[i] * points[k] * points[j]
                for k in range(i + 1, j, 1):
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k] + dp[k][j] + points[i] * points[k] * points[j])

        return dp[0][n + 1]


def main():
    # 输入：nums = [3,1,5,8]
    # 输出：167
    # 解释：
    # nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
    # coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
    solution1 = Solution()
    print(solution1.maxCoins(nums=[3, 1, 5, 8]))

    # 输入：nums = [1,5]
    # 输出：10
    solution2 = Solution()
    print(solution2.maxCoins(nums=[1, 5]))


if __name__ == '__main__':
    main()
