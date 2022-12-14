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