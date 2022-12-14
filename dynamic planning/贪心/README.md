# [贪心](https://labuladong.github.io/algo/3/29/99/)
</br>贪心可认为是动规算法的特例，相比动规，贪心需满足更多的条件（贪心选择性质），但效率比动规更高。
</br>使用暴力：指数级时间。
</br>使用动规：消除重叠子问题，可降低到多项式级别的时间。
</br>若满足贪心选择性质：可进一步降低时间复制度，达到线性级别。
</br>
</br>贪心选择性质：每一步都做出一个局部最优选择，最终的结果就是全局最优。
</br>NOTE：该性质特殊，只有部分问题拥有这个性质，大部分问题不具有贪心选择性质。
</br>

---

## 最多有几个区间不会重叠问题

</br>给你多个形如[start,end]的闭区间，算出这些区间中最多有几个互不相交的区间。
```java
 int intervalSchedule(int[][] intvs);
```
</br>例：intvs = [[1,3], [2,4], [3,6]]， 这些区间最多有 2 个区间互不相交，即 [[1,3], [3,6]]， 你的算法应该返回 2。
</br>**注意边界相同并不算相交。**
</br>
</br>这个问题在生活中的应用广泛，比如你今天有好几个活动，每个活动都可以用区间 [start, end] 表示开始和结束的时间，请问你今天最多能参加几个活动？
</br>显然你一个人不能同时参加两个活动，所以说这个问题就是求这些时间区间的最大不相交子集。
</br>
</br>这个问题有许多看起来不错的贪心思路，却都不能得到正确答案。比如说：
</br>也许我们可以每次选择可选区间中开始最早的那个？但是可能存在某些区间开始很早，但是很长，使得我们错误地错过了一些短的区间。
</br>或者我们每次选择可选区间中最短的那个？
</br>或者选择出现冲突最少的那个区间？
</br>这些方案都能很容易举出反例，不是正确的方案。
</br>
</br>正确的思路其实很简单，可以分为以下三步：
</br>1、从区间集合 intvs 中选择一个区间 x，这个 x 是在当前所有区间中结束最早的（end 最小）。
</br>2、把所有与 x 区间相交的区间从区间集合 intvs 中删除。
</br>3、重复步骤 1 和 2，直到 intvs 为空为止。之前选出的那些 x 就是最大不相交子集。
</br>把这个思路实现成算法的话，可以按每个区间的 end 数值升序排序，因为这样处理之后实现步骤 1 和步骤 2 都方便很多。
</br>算法实现：
</br>对于步骤1：由于事先按照每个区间的end数值升序排序，所以最小的end即为第一个元素。
</br>关键：如何移除与x相交的区间，选择下一轮循环的x。
</br>由于事先按照每个区间的end升序排序，故所有与x相交的区间必然会与x的end相交；
</br>如果一个区间不想与x的end相交，它的start必然要大于等于x的end：

![image](https://user-images.githubusercontent.com/41592973/207490723-ee059be9-ebdb-474d-8051-17817e444b8a.png)

```java
public int intervalSchedule(int[][] intvs) {
    if (intvs.length == 0) return 0;
    // 按 end 升序排序
    Arrays.sort(intvs, new Comparator<int[]>() {
        public int compare(int[] a, int[] b) {
            return a[1] - b[1];
        }
    });
    // 至少有一个区间不相交
    int count = 1;
    // 排序后，第一个区间就是 x
    int x_end = intvs[0][1];
    for (int[] interval : intvs) {
        int start = interval[0];
        if (start >= x_end) {
            // 找到下一个选择的区间了
            count++;
            x_end = interval[1];
        }
    }
    return count;
}
```

---

## [435.无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/)

</br>应用：435.无重叠区间
</br>输入一个区间的集合，若想使其中的区间都互不重叠，至少需要移除几个区间？

```java
int eraseOverlapIntervals(int[][] intvs);
```

</br>其中输入区间的终点总是大于起点，边界相等的区间不互相重叠。
</br>例：
></br>输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
></br>输出: 1
></br>解释: 移除 [1,3] 后，剩下的区间没有重叠。

</br>数组长度 - 最多有多少个区间不会重叠 = 至少需要移除的区间个数

```java
int eraseOverlapIntervals(int[][] intervals) {
    int n = intervals.length;
    return n - intervalSchedule(intervals);
}
```

---

## [452.用最少的箭头射爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/)

</br>假设在二维平面上有很多圆形气球，这些圆形投影到x轴上会形成一个个区间。
</br>给你输入这些区间，你沿着x轴前进，可以垂直向上射箭，请问你至少要射几箭才能把这些气球全部射爆？

```java
int findMinArrowShots(int[][] intvs);
```

例：
></br>输入：points = [[10,16],[2,8],[1,6],[7,12]]
></br>输出：2
></br>解释：气球可以用2支箭来爆破:
></br>-在x = 6处射出箭，击破气球[2,8]和[1,6]。
></br>-在x = 11处发射箭，击破气球[10,16]和[7,12]。

</br>该问题同区间调度算法，如果最多有n个不重叠的区间，那么就至少需要n个箭头射穿所有区间：

![image](https://user-images.githubusercontent.com/41592973/207494084-b55f4630-f049-4817-8f7a-011cd73787ce.png)

</br>该问题同区间调度调度算法的区别为：如果两个区间的边界触碰不算重叠；
</br>而该问题中，箭头如果碰到气球的边界气球也会爆炸，即相当与区间边界触碰也算重叠：

![image](https://user-images.githubusercontent.com/41592973/207494539-910a0489-de23-45a6-acd2-5c5b3893d953.png)

```java
int findMinArrowShots(int[][] intvs) {
    // ...

    for (int[] interval : intvs) {
        int start = interval[0];
        // NOTE: 把 >= 改成 > 
        if (start > x_end) {
            count++;
            x_end = interval[1];
        }
    }
    return count;
}
```

---
 
# 动规算法 vs 贪心算法

</br>贪心可理解为一种特殊的动规问题，贪心具有一些更为特殊的性质，可以进一步降低动规算法的时间复杂度。
</br>
</br>动规问题：一般为求最值形式，如最长子序列、最小编辑距离、最长公共子串等。
</br>贪心算法作为特殊的动规也是一样，也为求最值问题。
</br>

## [55.跳跃游戏](https://leetcode.cn/problems/jump-game/)

</br>该问题本质上也是求最值问题：
</br>通过题目中的跳跃规则，最多能跳多远？
</br>若能越过最后一格则返回true，否则返回false。
</br>
</br>故该问题可用动规及贪心算法求解，贪心算法如下：
</br>

```java
//算法每一步都计算从当前位置最远能够跳到哪里，
//然后同全局最优的最远位置farthest对比，
//通过每一步的最优解更新全局的最优解就是贪心算法。
boolean canJump(int[] nums) {
    int n = nums.length;
    int farthest = 0;
    for (int i = 0; i < n - 1; i++) {
        // 不断计算能跳到的最远距离
        farthest = Math.max(farthest, i + nums[i]);
        // 可能碰到了 0，卡住跳不动了
        if (farthest <= i) {
            return false;
        }
    }
    return farthest >= n - 1;
}
```

## [45.跳跃游戏II](https://leetcode.cn/problems/jump-game/)

</br>题目保证你一定可以跳到最后一格，请问你最少要跳多少次才能跳过去?
</br>
</br>动规： 采用自顶向下的dp-func解法。
</br>dp方法定义：从索引p跳到最后一格，至少需要 dp(nums, p) 步

```java
//从索引p跳到最后一格，至少需要 dp(nums, p) 步
int dp(int[] nums, int p);
```

</br>所求即为dp(nums, 0)，base case就是当p超过最后一个时不需要跳跃。

```java
if (p >= nums.length - 1) {
    return 0;
}
```

</br>动规解法可先暴力穷举所有可能的跳法，通过备忘录memory消除重叠子问题，取其中最小的值即为答案：

```java
int[] memo;
// 主函数
public int jump(int[] nums) {
    int n = nums.length;
    // 备忘录都初始化为 n，相当于 INT_MAX
    // 因为从 0 跳到 n - 1 最多 n - 1 步
    memo = new int[n];
    Arrays.fill(memo, n);

    return dp(nums, 0);
}

// 定义：从索引 p 跳到最后一格，至少需要 dp(nums, p) 步
int dp(int[] nums, int p) {
    int n = nums.length;
    // base case
    if (p >= n - 1) {
        return 0;
    }
    // 子问题已经计算过
    if (memo[p] != n) {
        return memo[p];
    }
    int steps = nums[p];
    // 你可以选择跳 1 步，2 步...
    for (int i = 1; i <= steps; i++) {
        // 穷举每一个选择
        // 计算每一个子问题的结果
        int subProblem = dp(nums, p + i);
        // 取其中最小的作为最终结果
        memo[p] = Math.min(memo[p], subProblem + 1);
    }
    return memo[p];
}
```

</br>状态：当前所站的索引p
</br>选择：可以跳出的步数
</br>算法时间复杂度：递归深度 * 每次递归需要的时间复杂度 = O(N^2)，leetcode部分超时。
</br>
</br>贪心优点：贪心选择性质可以进一步优化动规问题。
</br>满足贪心选择性质的问题：
</br>动规思路：穷举所有子问题，然后取其中最小的即为答案，核心代码框架：

```java
    int steps = nums[p];
    // 你可以选择跳 1 步，2 步...
    for (int i = 1; i <= steps; i++) {
        // 计算每一个子问题的结果
        int subProblem = dp(nums, p + i);
        res = min(subProblem + 1, res);
    }
```

</br>for循环中会陷入递归计算子问题，此处即为动规时间复杂度高的原因。
</br>优化：不递归，仅判断哪个选择最优即可：

![image](https://user-images.githubusercontent.com/41592973/207517607-482bc903-b3d8-4cff-8d88-d4fa531ab541.png)

如上，站在位置0，可以向前跳1、2、3步，最优跳数为2，因为2的下一跳区间值最大。
以上即为贪心选择性质，无需递归计算所有选择的具体结果通过比较求最值，只需做出最优选择即可。

```java
int jump(int[] nums) {
    int n = nums.length;
    int end = 0, farthest = 0;
    int jumps = 0;
    for (int i = 0; i < n - 1; i++) {
        farthest = Math.max(nums[i] + i, farthest);
        if (end == i) {
            jumps++;
            end = farthest;
        }
    }
    return jumps;
}
```

![image](https://user-images.githubusercontent.com/41592973/207518575-54ba7d4d-f2e4-4c6b-a624-894c69a44132.png)

</br>i及end标记了可以选择的跳跃步数。
</br>farthest：标记所有选择[i..end]中能够跳到的最远距离。
</br>jumps：记录跳跃步数。
</br>
</br>贪心时间复杂度：O(N)，空间复杂度O(1)。

---

# [使用贪心解决视频剪辑问题](https://labuladong.github.io/algo/3/29/101/)

## [1024.视频剪辑](https://leetcode.cn/problems/video-stitching/)

</br>题目给定一个目标区间和若干小区间，如何通过裁剪和组合小区间拼凑出目标区间？最少需要几个小区间？
</br>
</br>**区间问题：首先按照区间的起点或终点对区间进行排序。**
</br>因为排序之后更容易找到相邻区间之间的关系，如果时求最值问题，可以使用贪心算法进行求解。
</br>
</br>本例排序：先按起点升序排序，若起点相同的话按照终点降序排列。
</br>原因：
</br>1.要用若干短视频拼凑出完整版视频[0, T]，至少有一格视频的起点是0.
</br>2.如果有几个短视频的起点都相同，那么应选择最长即终点值最大的视频。
</br>以上即为贪心策略，基于以上两点，将clips按照起点升序排列，起点相同的按照终点降序排列。
</br>最后得到的区间顺序：

![image](https://user-images.githubusercontent.com/41592973/207553644-7c9f5616-b64c-451c-883a-6403e78edde1.png)
