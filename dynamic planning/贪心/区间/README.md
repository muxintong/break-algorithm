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
</br>本例按照区间起点进行升序排列，若起点相同按终点降序进行排列：

![image](https://user-images.githubusercontent.com/41592973/207785786-2090710f-75f1-441b-8192-0f4c25ccb14e.png)


其目的为防止出现如下情况：

![image](https://user-images.githubusercontent.com/41592973/207785569-edb12909-76dc-4db0-bfa0-c19c60a9e914.png)


</br>对于两个起点相同的区间，需保证长的区间在上面（按终点降序排列），
</br>这样才会被判定为覆盖，否则会被错误的判定为相交，导致少算一个覆盖区间。
</br>
</br>排序后两相邻区间有如下三种位置情况：

![image](https://user-images.githubusercontent.com/41592973/207785618-d71bb409-3b56-4b7a-a13a-bebe49790394.png)


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

---

# 区间合并问题

## [56.合并区间](https://leetcode.cn/problems/merge-intervals/)

</br>给出一个区间的集合，合并所有重叠的区间。
</br>解决区间问题：先排序，后画出所有可能位置情况。
</br>一个区间可表示为[start, end]，在区间调度问题中，需按照end排序，以满足贪心选择性质；
</br>对于区间合并问题，按start或end排序均可；
</br>本例按照start升序排列：

![image](https://user-images.githubusercontent.com/41592973/207790929-42b78a57-0dc9-4b16-bae8-6487064d0f91.png)


</br>对于几个相交区间合并后的结果区间x来说：
</br>start为所有相交区间中最小的； end为所有相交区间中最大的：

![image](https://user-images.githubusercontent.com/41592973/207791172-527a468a-64cd-4ac5-83c8-4dae0370070e.png)



```java
# intervals 形如 [[1,3],[2,6]...]
def merge(intervals):
    if not intervals: return []
    # 按区间的 start 升序排列
    intervals.sort(key=lambda intv: intv[0])
    res = []
    res.append(intervals[0])

    for i in range(1, len(intervals)):
        curr = intervals[i]
        # res 中最后一个元素的引用
        last = res[-1]
        if curr[0] <= last[1]:
            # 找到最大的 end
            last[1] = max(last[1], curr[1])
        else:
            # 处理下一个待合并区间
            res.append(curr)
    return res

```

---

# 区间交集问题

## [986.区间列表的交集](https://leetcode.cn/problems/interval-list-intersections/)

</br>给定两个由一些闭区间组成的列表，每个区间列表成对不相交，且已经排序。
</br>返回这两个区间列表的交集。
</br>
</br>NOTE：区间左右都是闭区间
</br>
</br>解决区间问题：首先排序，题目已经排好序，
</br>接下来使用两个索引指针p1、p2遍历集合A、B找出所有交集：
</br>使用[left1, right1]、[left2, right2]表示在集合A、B中的两个区间；
</br>两个区间存在交集的所有可能情况：

![image](https://user-images.githubusercontent.com/41592973/207818779-9f7acadf-6e15-4a79-a21b-8dd403018165.png)


</br>交集值应为两个区间中左边界大的max(left1, left2)，右边界小的min(right1, right2)。

![image](https://user-images.githubusercontent.com/41592973/207818873-22658d33-99e0-4ab3-a956-9afd29d18d73.png)

</br>关于索引指针p1、p2前进条件的判定：
</br>关于p1、p2索引指针是否前进只取决于右侧边界值，右侧边界值小的前移。

![image](https://user-images.githubusercontent.com/41592973/207818976-9fb73de3-8b83-4cce-b0c0-77569dc92c7d.png)


```python
# A, B 形如 [[0,2],[5,10]...]
def intervalIntersection(A, B):
    i, j = 0, 0 # 双指针
    res = []
    while i < len(A) and j < len(B):
        a1, a2 = A[i][0], A[i][1]
        b1, b2 = B[j][0], B[j][1]
        # 两个区间存在交集
        if b2 >= a1 and a2 >= b1:
            # 计算出交集，加入 res
            res.append([max(a1, b1), min(a2, b2)])
        # 指针前进
        if b2 < a2: j += 1
        else:       i += 1
    return res
```
