# 二分搜索算法

```java
int binarySearch(int[] nums, int target) {
    int left = 0; 
    int right = nums.length - 1; // 注意

    while(left <= right) {
        int mid = left + (right - left) / 2;
        if(nums[mid] == target)
            return mid; 
        else if (nums[mid] < target)
            left = mid + 1; // 注意
        else if (nums[mid] > target)
            right = mid - 1; // 注意
    }
    return -1;
}
```

---

1、为什么 while 循环的条件中是 <=，而不是 <？</br>
 因为初始化 right 的赋值是 nums.length - 1，即最后一个元素的索引，而不是 nums.length.</br>
 这二者可能出现在不同功能的二分查找中，区别是：前者相当于两端都闭区间 [left, right]，</br>
 后者相当于左闭右开区间 [left, right)，因为索引大小为 nums.length 是越界的。 </br>
 我们这个算法中使用的是前者 [left, right] 两端都闭的区间。这个区间其实就是每次进行搜索的区间。</br>
什么时候应该停止搜索呢？当然，找到了目标值的时候可以终止：</br>
```java
if(nums[mid] == target)
  return mid; 
```
但如果没找到，就需要 while 循环终止，然后返回 -1。</br>
那 while 循环什么时候应该终止？搜索区间为空的时候应该终止，意味着你没得找了，即没有找到。</br>
while(left <= right) 的终止条件是 left == right + 1，写成区间的形式就是 [right + 1, right]，</br>
或者带个具体的数字进去 [3, 2]，可见这时候区间为空，因为没有数字既大于等于 3 又小于等于 2 的吧。所以这时候 while 循环终止是正确的，直接返回 -1 即可。
while(left < right) 的终止条件是 left == right，写成区间的形式就是 [right, right]，
或者带个具体的数字进去 [2, 2]，这时候区间非空，还有一个数 2，但此时 while 循环终止了。
也就是说这区间 [2, 2] 被漏掉了，索引 2 没有被搜索，如果这时候直接返回 -1 就是错误的。
要用 while(left < right) 需打个补丁：
```java
//...
while(left < right) {
    // ...
}
return nums[left] == target ? left : -1;
```

---

2、为什么 left = mid + 1，right = mid - 1？有的代码是 right = mid 或者 left = mid？</br>
首先明确「搜索区间」开闭情况，本算法的搜索区间是两端都闭的，即 [left, right]。</br>
那么当我们发现索引 mid 不是要找的 target 时，下一步应该去搜索哪里呢？</br>
当然是去搜索区间 [left, mid-1] 或者区间 [mid+1, right] ，因为 mid 已经搜索过，应该从搜索区间中去除。

---

3、此算法缺陷：左右侧边界的处理问题
比如说给你有序数组 nums = [1,2,2,2,3]，target 为 2，此算法返回的索引是 2。
但是如果我想得到 target 的左侧边界，即索引 1，或者我想得到 target 的右侧边界，即索引 3，这样的话此算法是无法处理的。
这样的需求很常见，你也许会说，找到一个 target，然后向左或向右线性搜索不行吗？
可以，但是不好，因为这样难以保证二分查找对数级的复杂度了。

---

# 寻找左侧边界的二分算法

```java
int left_bound(int[] nums, int target) {
    int left = 0;
    int right = nums.length; // 注意
    
    while (left < right) { // 注意
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            right = mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid; // 注意
        }
    }
    return left;
}
```

---

1、为什么 while 中是 < 而不是 <=? </br>
因为 right = nums.length 而不是 nums.length - 1。因此每次循环的「搜索区间」是 [left, right) 左闭右开。</br>
while(left < right) 终止的条件是 left == right，此时搜索区间 [left, left) 为空，所以可以正确终止。</br>
PS：这里先要说一个搜索左右边界和上面这个算法的一个区别：</br>
刚才的 right 是 nums.length - 1 ， 这里写成 nums.length 使得「搜索区间」变成左闭右开？</br>
因为对于搜索左右侧边界的二分查找，这种写法比较普遍。

---

2、为什么没有返回 -1 的操作？如果 nums 中不存在 target 这个值，怎么办？</br>
在返回的时候额外判断一下 nums[left] 是否等于 target 就行了，如果不等于，就说明 target 不存在。
不过我们得考察一下 left 的取值范围，免得索引越界。</br>
假如输入的 target 非常大，那么就会一直触发 nums[mid] < target 的 if 条件，left 会一直向右侧移动，直到等于 right，while 循环结束。</br>
由于这里 right 初始化为 nums.length，所以 left 变量的取值区间是闭区间 [0, nums.length]，那么我们在检查 nums[left] 之前需要额外判断一下，防止索引越界：
```java
while (left < right) {
    //...
}
// 此时 target 比所有数都大，返回 -1
if (left == nums.length) return -1;
// 判断一下 nums[left] 是不是 target
return nums[left] == target ? left : 
```

---

3、为什么 left = mid + 1，right = mid ？和之前的算法不一样？</br>
因为「搜索区间」是 [left, right) 左闭右开，所以当 nums[mid] 被检测之后，下
一步应该去 mid 的左侧或者右侧区间搜索，即 [left, mid) 或 [mid + 1, right)。

---

4、为什么该算法能够搜索左侧边界？</br>

关键在于对于 nums[mid] == target 这种情况的处理：</br>
```java
if (nums[mid] == target)
    right = mid;
```
可见，找到 target 时不要立即返回，而是缩小「搜索区间」的上界 right，在区间 [left, mid) 中继续搜索， 即不断向左收缩，达到锁定左侧边界的目的。

---

5、为什么返回 left 而不是 right？</br>
都是一样的，因为 while 终止的条件是 left == right。

---

6、能不能想办法把 right 变成 nums.length - 1，也就是继续使用两边都闭的「搜索区间」？这样就可以和第一种二分搜索在某种程度上统一起来了。</br>
答：当然可以，只要你明白了「搜索区间」这个概念，就能有效避免漏掉元素，随便你怎么改都行。下面我们严格根据逻辑来修改：</br>
因为你非要让搜索区间两端都闭，所以 right 应该初始化为 nums.length - 1，while 的终止条件应该是 left == right + 1，也就是其中应该用 <=：
```java
int left_bound(int[] nums, int target) {
    // 搜索区间为 [left, right]
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        // if else ...
    }
```

因为搜索区间是两端都闭的，且现在是搜索左侧边界，所以 left 和 right 的更新逻辑如下：</br>

```java
if (nums[mid] < target) {
    // 搜索区间变为 [mid+1, right]
    left = mid + 1;
} else if (nums[mid] > target) {
    // 搜索区间变为 [left, mid-1]
    right = mid - 1;
} else if (nums[mid] == target) {
    // 收缩右侧边界
    right = mid - 1;
}
```

和刚才相同，如果想在找不到 target 的时候返回 -1，那么检查一下 nums[left] 和 target 是否相等即可：

```java
// 此时 target 比所有数都大，返回 -1
if (left == nums.length) return -1;
// 判断一下 nums[left] 是不是 target
return nums[left] == target ? left : -1;
至此，整个算法就写完了，完整代码如下：

int left_bound(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    // 搜索区间为 [left, right]
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            // 搜索区间变为 [mid+1, right]
            left = mid + 1;
        } else if (nums[mid] > target) {
            // 搜索区间变为 [left, mid-1]
            right = mid - 1;
        } else if (nums[mid] == target) {
            // 收缩右侧边界
            right = mid - 1;
        }
    }
    // 判断 target 是否存在于 nums 中
    // 此时 target 比所有数都大，返回 -1
    if (left == nums.length) return -1;
    // 判断一下 nums[left] 是不是 target
    return nums[left] == target ? left : -1;
}
```

这样就和第一种二分搜索算法统一了，都是两端都闭的「搜索区间」，而且最后返回的也是 left 变量的值。只要把住二分搜索的逻辑，两种形式大家看自己喜欢哪种记哪种吧。

---