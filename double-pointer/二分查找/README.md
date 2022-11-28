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


