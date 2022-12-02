---

</br>原文地址：
</br>[https://labuladong.github.io/algo/1/11/](https://labuladong.github.io/algo/1/11/)
</br>[https://labuladong.github.io/algo/2/20/31/](https://labuladong.github.io/algo/2/20/31/)

---

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
 区别是：前者相当于两端都闭区间 [left, right]，后者相当于左闭右开区间 [left, right)，因为索引大小为 nums.length 是越界的。 </br>
 这个算法中使用的是 [left, right] 闭区间，找到了目标值的时候可以终止：</br>
```java
if(nums[mid] == target) 
  return mid; 
```
但如果没找到，就需要 while 循环终止，然后返回 -1。</br>
那 while 循环什么时候应该终止？搜索区间为空的时候应该终止，意味着你没得找了，即没有找到。</br>
while(left <= right) 的终止条件是 left == right + 1，写成区间的形式就是 [right + 1, right]，</br>
while(left < right) 的终止条件是 left == right，写成区间的形式就是 [right, right]，即right<right，</br>
但该情况下漏掉了left=right这种情况， 要用 while(left < right) 需打个补丁：
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

3、此算法缺陷：左右侧边界的处理问题</br>
比如说给你有序数组 nums = [1,2,2,2,3]，target 为 2，此算法返回的索引是 2。</br>
但是如果我想得到 target 的左侧边界，即索引 1，或者我想得到 target 的右侧边界，即索引 3。</br>
一种可能的解决方案：找到一个 target，然后向左或向右线性搜索，但该种做法无法确保二分查找对数级复杂度。

---

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
</br>
搜索左右边界和上面这个算法的一个区别：</br>
刚才的 right 是 nums.length - 1 ， 这里写成 nums.length 使得「搜索区间」变成左闭右开：对于搜索左右侧边界的二分查找，这种写法比较普遍。

---

2、为什么没有返回 -1 的操作？如果 nums 中不存在 target 这个值，怎么办？</br>
在返回的时候额外判断一下 nums[left] 是否等于 target 就行了，如果不等于，就说明 target 不存在，还需判定 left 的取值范围，防止索引越界。</br>
假如输入的 target 非常大，那么就会一直触发 nums[mid] < target 的 if 条件，left 会一直向右侧移动，直到等于 right，while 循环结束。</br>
由于这里 right 初始化为 nums.length，所以 left 变量的取值区间是闭区间 [0, nums.length]，那么我们在检查 nums[left] 之前需要额外判断一下，防止索引越界：
```java
while (left < right) {
    //...
}
// 此时 target 比所有数都大，返回 -1
if (left == nums.length) return -1;
// 判断一下 nums[left] 是不是 target
return nums[left] == target ? left : -1
```

---

3、为什么 left = mid + 1，right = mid ？而非 right = mid + 1</br>
因为「搜索区间」是 [left, right) 左闭右开，所以当 nums[mid] 被检测之后，下一步应该去 mid 的左侧或者右侧区间搜索，即 [left, mid) 或 [mid + 1, right)。

---

4、为什么该算法能够搜索左侧边界？</br>
关键在于对于 nums[mid] == target 这种情况的处理：</br>
```java
if (nums[mid] == target)
    right = mid;
```
即：**找到 target 时不要立即返回，而是缩小「搜索区间」的上界 right，在区间 [left, mid) 中继续搜索， 即不断向左收缩，达到锁定左侧边界的目的。**

---

5、为什么返回 left 而不是 right？</br>
都是一样的，因为 while 终止的条件是 left == right。

---

6、把 right 变成 nums.length - 1，使用两边都闭的「搜索区间」统一算法模板：</br>
 right 应该初始化为 nums.length - 1，while 的终止条件应该是 left == right + 1，也就是其中应该用 <=：
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
```

完整代码如下：

```java
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

这样就和第一种二分搜索算法统一了，都是两端都闭的「搜索区间」，而且最后返回的也是 left 变量的值。

---

---

# 寻找右侧边界的二分查找

```java
int right_bound(int[] nums, int target) {
    int left = 0, right = nums.length;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            left = mid + 1; // 注意
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid;
        }
    }
    return left - 1; // 注意
}
```

---

1、为什么这个算法能够找到右侧边界？</br>
关键点：
```commandline
if (nums[mid] == target) {
    left = mid + 1;
```
即：**当 nums[mid] == target 时，不要立即返回，而是增大「搜索区间」的左边界 left，使得区间不断向右靠拢，达到锁定右侧边界的目的。**

---

2、为什么最后返回 left - 1 而不像左侧边界的函数，返回 left？既然是搜索右侧边界，应该返回 right 才对。</br>
while 循环的终止条件是 left == right，所以 left 和 right 是一样的，要体现右侧的特点，返回 right - 1 。</br>
至于为什么要减一，这是搜索右侧边界的一个特殊点，关键在锁定右边界时的这个条件判断：
```java
// 增大 left，锁定右侧边界
if (nums[mid] == target) {
    left = mid + 1;
    // 这样想: mid = left - 1
```
因为我们对 left 的更新必须是 left = mid + 1，就是说 while 循环结束时，nums[left] 一定不等于 target 了，而 nums[left-1] 可能是 target。</br>
至于为什么 left 的更新必须是 left = mid + 1，是为了把 nums[mid] 排除出搜索区间。

---

3、为什么没有返回 -1 的操作？如果 nums 中不存在 target 这个值，怎么办？</br>
只要在最后判断一下 nums[left-1] 是不是 target 就行了。</br>
类似之前的左侧边界搜索，left 的取值范围是 [0, nums.length]，但由于我们最后返回的是 left - 1，所以 left 取值为 0 的时候会造成索引越界，额外处理一下即可正确地返回 -1：
```java
while (left < right) {
    // ...
}
// 判断 target 是否存在于 nums 中
// 此时 left - 1 索引越界
if (left - 1 < 0) return -1;
// 判断一下 nums[left] 是不是 target
return nums[left - 1] == target ? (left - 1) : -1;
```

---

4、把算法的「搜索区间」统一成两端都闭的形式：

```java
int right_bound(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else if (nums[mid] == target) {
            // 这里改成收缩左侧边界即可
            left = mid + 1; //终止结束条件：mid = left - 1
        }
    }
    // 最后改成返回 left - 1
    if (left - 1 < 0) return -1;
    return nums[left - 1] == target ? (left - 1) : -1;
}
```
由于 while 的结束条件为 right == left - 1，把上述代码中的 left - 1 都改成 right 也没有问题，这样可能更有利于看出来这是在「搜索右侧边界」。

---

---

逻辑统一</br>

>第一个，最基本的二分查找算法：</br>
></br>
>因为我们初始化 right = nums.length - 1</br>
>所以决定了我们的「搜索区间」是 [left, right]</br>
>所以决定了 while (left <= right)</br>
>同时也决定了 left = mid+1 和 right = mid-1</br>
></br>
>因为我们只需找到一个 target 的索引即可</br>
>所以当 nums[mid] == target 时可以立即返回</br>
>第二个，寻找左侧边界的二分查找：</br>
></br>
>因为我们初始化 right = nums.length</br>
>所以决定了我们的「搜索区间」是 [left, right)</br>
>所以决定了 while (left < right)</br>
>同时也决定了 left = mid + 1 和 right = mid</br>
></br>
>因为我们需找到 target 的最左侧索引</br>
>所以当 nums[mid] == target 时不要立即返回</br>
>而要收紧右侧边界以锁定左侧边界</br>
>第三个，寻找右侧边界的二分查找：</br>
></br>
>因为我们初始化 right = nums.length</br>
>所以决定了我们的「搜索区间」是 [left, right)</br>
>所以决定了 while (left < right)</br>
>同时也决定了 left = mid + 1 和 right = mid</br>
></br>
>因为我们需找到 target 的最右侧索引</br>
>所以当 nums[mid] == target 时不要立即返回</br>
>而要收紧左侧边界以锁定右侧边界</br>
></br>
>又因为收紧左侧边界时必须 left = mid + 1</br>
>所以最后无论返回 left 还是 right，必须减一</br>
>对于寻找左右边界的二分搜索，常见的手法是使用左闭右开的「搜索区间」，只要修改两处即可变化出三种写法：

```java
int binary_search(int[] nums, int target) {
    int left = 0, right = nums.length - 1; 
    while(left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1; 
        } else if(nums[mid] == target) {
            // 直接返回
            return mid;
        }
    }
    // 直接返回
    return -1;
}

int left_bound(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else if (nums[mid] == target) {
            // 别返回，锁定左侧边界
            right = mid - 1;
        }
    }
    // 判断 target 是否存在于 nums 中
    // 此时 target 比所有数都大，返回 -1
    if (left == nums.length) return -1;
    // 判断一下 nums[left] 是不是 target
    return nums[left] == target ? left : -1;
}

int right_bound(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else if (nums[mid] == target) {
            // 别返回，锁定右侧边界
            left = mid + 1;
        }
    }
    // 此时 left - 1 索引越界
    if (left - 1 < 0) return -1;
    // 判断一下 nums[left] 是不是 target
    return nums[left - 1] == target ? (left - 1) : -1;
}
```

NOTE:</br>
1、分析二分查找代码时，不要出现 else，全部展开成 else if 方便理解。</br>
2、注意「搜索区间」和 while 的终止条件，如果存在漏掉的元素，记得在最后检查。</br>
3、如需定义左闭右开的「搜索区间」搜索左右边界，只要在 nums[mid] == target 时做修改即可，搜索右侧时需要减一。</br>
4、如果将「搜索区间」全都统一成两端都闭，好记，只要稍改 nums[mid] == target 条件处的代码和返回的逻辑即可。</br>
二分思维：通过已知信息尽可能多地收缩（折半）搜索空间，从而增加穷举效率，快速找到目标。</br>

---

# 二分搜索的泛化

二分搜索的原型就是在「有序数组」中搜索一个元素 target，返回该元素对应的索引。</br>
如果该元素不存在，那可以返回一个什么特殊值，这种细节问题只要微调算法实现就可实现。</br>
还有一个重要的问题，如果「有序数组」中存在多个 target 元素，那么这些元素肯定挨在一起，这里就涉及到算法应该返回最左侧的那个 target 元素的索引还是最右侧的那个 target 元素的索引，也就是所谓的「搜索左侧边界」和「搜索右侧边界」，这个也可以通过微调算法的代码来实现。
在具体的算法问题中，常用到的是「搜索左侧边界」和「搜索右侧边界」这两种场景，很少有让你单独「搜索一个元素」。

</br>因为算法题一般都让你求最值，比如让你求吃香蕉的「最小速度」，让你求轮船的「最低运载能力」，求最值的过程，必然是搜索一个边界的过程

```java
// 搜索左侧边界
int left_bound(int[] nums, int target) {
    if (nums.length == 0) return -1;
    int left = 0, right = nums.length;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            // 当找到 target 时，收缩右侧边界
            right = mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid;
        }
    }
    return left;
}

// 搜索右侧边界
int right_bound(int[] nums, int target) {
    if (nums.length == 0) return -1;
    int left = 0, right = nums.length;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            // 当找到 target 时，收缩左侧边界
            left = mid + 1;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid;
        }
    }
    return left - 1;
}
```

**什么问题适用于二分搜索技巧？**
</br>需从题目中提取出自变量x，关于x的函数f(x)，以及目标值target。
</br>同时，x、f(x)、target还需满足一下条件：
</br>1. f(x)必须是x上的单调函数（递增递减均可），即使用二分搜索前数组需有序。
</br>2. 题目是让你计算满足越苏条件f(x)==target时的x值。
</br>
</br>例：
</br>nums：升序排序的有序数组
</br>target：目标元素
</br>计算target在数组中的索引位置，如果有多个目标元素，返回最小的索引。
</br>
</br>上述要求即为求【左侧边界】的题型，对应x、f(x)、target分别如下：
</br>x：数组中元素的索引可认为时自变量x，则函数关系f(x)如下
```java
//函数f(x)是关于自变量x的单调递增函数
//入参nums不变，不是自变量，可以忽略
int f(int x, int[] nums) {
  return nums[x];
}
```
</br>函数f即相当于正向访问数组nums，因为nums为升序排序的有序数组，所以f(x)就是x上的单调递增函数。
</br>求解元素target的最左索引？即等价于满足f(x)==target的x最小值为多少？
</br>画出单调函数，即可运用二分搜索框架：
```java
//函数f(x)是关于自变量x的单调递增函数
int f(int x, int[] nums) {
    return nums[x];
}

int left_bound(int[] nums, int target) {
    if (nums.length == 0) return -1;
    int left = 0, right = nums.length;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (f(mid, nums) == target) {
            //收缩右边界=》确定左边界
            right=mid;
        } else if (f(mid, nums) < target) {
            left = mid +1;
        } else if (f(mid, nums) > target) {
            right = mid;
        }
    }
    return left;
```

```java
//函数f是关于自变量x的单调函数
int f(int x) {
    // ...
}

//主函数，在f(x)==target的约束下求x的最值
int solution(int[] nums, int target) {
    if (nums.length == 0) return -1;
    //自变量x的最小值
    int left = ...;
    //自变量x的最大值
    int right = ... + 1;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (f(mid) == target) {
            //求左边界还是右边界？
            ...
        } else if (f(mid) < target) {
            //如何是f(x)更大？
            ...
        } else if (f(mid) > target) {
            //如何是f(x)更小？
            ...
        }
    }
    return left;
```
</br>二分搜索算法步骤：
</br>1. 确定x、f(x)、target分别为多少，并写出函数f(x)
</br>2. 找到x的取值范围作为二分搜索的区间，初始化left和right变量
</br>3. 根据题目要求，确定应该使用左侧边界还是右侧边界的二分搜索算法。

---

# 875
</br>珂珂每小时最多只吃一堆香蕉，如果吃不完的话留到下一小时再吃；
</br>如果吃完了这一堆还有胃口，也只会等到下一个小时才会吃下一堆。
</br>他想在警卫回来之前吃完所有的香蕉，让我们确定吃香蕉的最小速度K。
```java
int minEatingSpeed(int[] piles, int H);
```
</br>按照如下步骤应用二分搜索算法：
</br>1. 确定x、f(x)、target分别是什么，并写出函数f(x)代码。
</br>二分搜索的本质就是在搜索自变量x。
</br>所以题目所求即为自变量，即珂珂的吃香蕉速度。
</br>在x上的单调函数f(x)?吃香蕉的速度越快，吃完所有香蕉堆所需的时间就越小，速度和时间就是一个单调关系。
</br>故f(x)的定义如下：若吃香蕉的速度为x根/小时，则需要f(x)小时吃完所有的香蕉。
```java
//若吃香蕉的速度为x根/小时，则需要f(x)小时吃完所有的香蕉。
//f(x)是x上的单调递减函数
int f(int[] piles, int x) {
    int hours = 0;
    for(int i = 0; i < piles.length; i++) {
        hours += piles[i] / x;
        if (piles[i] % x > 0) {
            hours++;
        }
    }
    return hours;
}
```
</br>target:吃香蕉的时间限制H即为target，是对f(x)返回值的最大约束。
</br>
</br>2. 找到x的取值范围作为二分搜索的搜索区间，初始化left和right变量。
</br>即吃香蕉的速度的取值范围：
</br>最小速度：1
</br>最大速度：piles数组中元素的最大值，因为每小时最大吃一堆香蕉。
</br>两种选择确定二分搜索的区间：
</br>使用for循环遍历piles数组，计算最大值。
</br>看题目中piles的取值范围约束，给right初始化一个取值范围之外的值。
</br>使用题目中的约束条件确定二分搜索的区间：
```java
public int minEatingSpeed(int[] piles, int H) {
    int left = 1;
    //NOTE:right是开区间，所以在加1
    int right = 1000000000 + 1;
    
}
```
</br>3. 根据题目要求，确定是搜索左边界还是右边界
</br>自变量x：吃香蕉的速度
</br>f(x)：关于自变量x的单调递减函数
</br>target：吃香蕉的时间限制H
</br>
</br>题目要求计算最小速度，即x要尽可能的小：
</br>