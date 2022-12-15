</br>区间问题即为线段问题，如：合并所有线段、找出线段交点等。
</br>主要使用一下两个技巧解决区间问题：
</br>1. 排序
</br>按起点升序排序，若起点相同按终点降序排序；
</br>按终点降序排序等。
</br>2. 画图
</br>画出两个区间的相对位置可能情况

---

# 区间覆盖问题

## [1288.删除被覆盖区间](https://leetcode.cn/problems/remove-covered-intervals/)

</br>题目要求去除被覆盖区间后还剩多少个区间 = 区间总数 - 被覆盖区间个数
</br>
</br>**区间问题首先针对首位区间值进行排序：**
</br>本例按照区间起点进行升序排列，若起点相同按终点降序进行排列，其目的为防止出现如下情况：
</br>
</br>对于两个起点相同的区间，需保证长的区间在上面（按终点降序排列），
</br>这样才会被判定为覆盖，否则会被错误的判定为相交，导致少算一个覆盖区间。
</br>
</br>排序后两相邻区间有如下三种位置情况：
</br>
</br>1. 找到了覆盖区间
</br>2. 两个区间可以合并成一格大区间
</br>3. 两个区间完全不相交

```java
int removeCoveredIntervals(int[][] intvs) {
    // 按照起点升序排列，起点相同时降序排列
    Arrays.sort(intvs, (a, b) -> {
        if (a[0] == b[0]) {
            return b[1] - a[1];
        }
        return a[0] - b[0]; 
    });

    // 记录合并区间的起点和终点
    int left = intvs[0][0];
    int right = intvs[0][1];

    int res = 0;
    for (int i = 1; i < intvs.length; i++) {
        int[] intv = intvs[i];
        // 情况一，找到覆盖区间
        if (left <= intv[0] && right >= intv[1]) {
            res++;
        }
        // 情况二，找到相交区间，合并
        if (right >= intv[0] && right <= intv[1]) {
            right = intv[1];
        }
        // 情况三，完全不相交，更新起点和终点
        if (right < intv[0]) {
            left = intv[0];
            right = intv[1];
        }
    }

    return intvs.length - res;
}
```