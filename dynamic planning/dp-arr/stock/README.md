---
每一天，看看总共有几种可能的「状态」，再找出每个「状态」对应的「选择」。
我们要穷举所有「状态」，穷举的目的是根据对应的「选择」更新状态。
for 状态1 in 状态1的所有取值：
    for 状态2 in 状态2的所有取值：
        for 选择 in 选择列表:
            dp[状态1][状态2][...] = 择优(选择1，选择2...)
---
1.【选择】           
该问题每天都有三种「选择」：买入、卖出、无操作，我们用 buy, sell, rest 表示这三种选择。
问题是，并不是每天都可以任意选择这三种选择的，因为 sell 必须在 buy 之后，buy 必须在 sell 之后。
那么 rest 操作还应该分两种状态，一种是 buy 之后的 rest（持有了股票），一种是 sell 之后的 rest（没有持有股票）。
而且还有交易次数 k 的限制，就是说你 buy 还只能在 k > 0 的前提下操作。
---
2.【状态】
>这个问题的「状态」有三个：
>- 第一个是天数，
>- 第二个是允许交易的最大次数，
>- 第三个是当前的持有状态（即之前说的 rest 的状态，我们不妨用 1 表示持有，0 表示没有持有）。

```commandline
用一个三维数组就可以装下这几种状态的全部组合：
dp[i][k][0 or 1]
0 <= i <= n - 1, 1 <= k <= K
n 为天数，大 K 为交易数的上限，0 和 1 代表是否持有股票。
此问题共 n × K × 2 种状态，全部穷举就能搞定。
for 0 <= i < n:
    for 1 <= k <= K:
        for s in {0, 1}:
            dp[i][k][s] = max(buy, sell, rest)
```


用自然语言描述出每一个状态的含义：</br>
比如dp[3][2][1] 的含义就是：今天是第三天，我现在手上持有着股票，至今最多进行 2 次交易。</br>
再比如 dp[2][3][0] 的含义：今天是第二天，我现在手上没有持有股票，至今最多进行 3 次交易。</br>
我们想求的最终答案是 dp[n - 1][K][0]，即最后一天，最多允许 K 次交易，最多获得多少利润。

读者可能问为什么不是 dp[n - 1][K][1]？</br>
因为 dp[n - 1][K][1] 代表到最后一天手上还持有股票，dp[n - 1][K][0] 表示最后一天手上的股票已经卖出去了，很显然后者得到的利润一定大于前者。

记住如何解释「状态」，一旦你觉得哪里不好理解，把它翻译成自然语言就容易理解了。

---
3.【状态转移方程式】</br>
```commandline
f(0)=f(0).reset | f(1).sell:+price[i]
f(1)=f(1).reset | f(0).buy:-price[i]
------------------------------------------
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
              max( 今天选择 rest,        今天选择 sell       )
解释：今天我没有持有股票，有两种可能，我从这两种可能中求最大利润：
1、我昨天就没有持有，且截至昨天最大交易次数限制为 k；然后我今天选择 rest，所以我今天还是没有持有，最大交易次数限制依然为 k。
2、我昨天持有股票，且截至昨天最大交易次数限制为 k；但是今天我 sell 了，所以我今天没有持有股票了，最大交易次数限制依然为 k。

dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
              max( 今天选择 rest,         今天选择 buy         )    
解释：今天我持有着股票，最大交易次数限制为 k，那么对于昨天来说，有两种可能，我从这两种可能中求最大利润：
1、我昨天就持有着股票，且截至昨天最大交易次数限制为 k；然后今天选择 rest，所以我今天还持有着股票，最大交易次数限制依然为 k。
2、我昨天本没有持有，且截至昨天最大交易次数限制为 k - 1；但今天我选择 buy，所以今天我就持有股票了，最大交易次数限制为 k。
```
NOTE:时刻牢记「状态」的定义，状态 k 的定义并不是「已进行的交易次数」，而是「最大交易次数的上限限制」。
如果确定今天进行一次交易，且要保证截至今天最大交易次数上限为 k，那么昨天的最大交易次数上限必须是 k - 1。              

如果 buy，就要从利润中减去 prices[i]，如果 sell，就要给利润增加 prices[i]。今天的最大利润就是这两种可能选择中较大的那个。
注意 k 的限制，在选择 buy 的时候相当于开启了一次交易，那么对于昨天来说，交易次数的上限 k 应该减小 1。

NOTE：以前我以为在 sell 的时候给 k 减小 1 和在 buy 的时候给 k 减小 1 是【不等效】的，
因为交易是从 buy 开始，如果 buy 的选择不改变交易次数 k 的话，会出现交易次数超出限制的的错误。             

    
```commandline  
base case：即最简单的初始已知状态   
dp[-1][...][0] = 0
解释：因为 i 是从 0 开始的，所以 i = -1 意味着还没有开始，这时候的利润当然是 0。
dp[-1][...][1] = -infinity
解释：还没开始的时候，是不可能持有股票的。
因为我们的算法要求一个最大值，所以初始值设为一个最小值，方便取最大值。
dp[...][0][0] = 0
解释：因为 k 是从 1 开始的，所以 k = 0 意味着根本不允许交易，这时候利润当然是 0。
dp[...][0][1] = -infinity
解释：不允许交易的情况下，是不可能持有股票的。
因为我们的算法要求一个最大值，所以初始值设为一个最小值，方便取最大值。
``` 

---

4.股票问题动规解法通用框架
```
base case：
dp [i：天数] [k：最大交易次数] [0|1：第i天的股票持有状态，0不持有，1持有]
base case：1.天数i为-1；2.最大交易次数k为0
dp[-1][...][0] = dp[...][0][0] = 0
dp[-1][...][1] = dp[...][0][1] = -infinity

状态转移方程：
for 0 <= i < n:
for 1 <= k <= K:
    # for s in {0, 1}:
    #     dp[i][k][s] = max(buy, sell, rest)
    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

```
数组索引是 -1 怎么编程表示出来呢，负无穷怎么表示呢？这都是细节问题，有很多方法实现。

---
problems：121</br>
直接套状态转移方程，根据 base case，可以做一些化简：
```commandline
for i in n:
    for k in K:
        dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
        dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i]) 
                    = max(dp[i-1][1][1], -prices[i])
解释：k = 0 的 base case，所以 dp[i-1][0][0] = 0。

现在发现 k 都是 1，不会改变，即 k 对状态转移已经没有影响了。
可以进行进一步化简去掉所有 k：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], -prices[i])
```
直接写出代码：
```commandline
int n = prices.length;
int[][] dp = new int[n][2];
for (int i = 0; i < n; i++) {
    dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]);
    dp[i][1] = Math.max(dp[i-1][1], -prices[i]);
}
return dp[n - 1][0];
```

显然 i = 0 时 i - 1 是不合法的索引，这是因为我们没有对 i 的 base case 进行处理，可以这样给一个特化处理：
```commandline
if (i - 1 == -1) {
    dp[i][0] = 0;
    // 根据状态转移方程可得：
    //   dp[i][0] 
    // = max(dp[-1][0], dp[-1][1] + prices[i])
    // = max(0, -infinity + prices[i]) = 0

    dp[i][1] = -prices[i];
    // 根据状态转移方程可得：
    //   dp[i][1] 
    // = max(dp[-1][1], dp[-1][0] - prices[i])
    // = max(-infinity, 0 - prices[i]) 
    // = -prices[i]
    continue;
} 
```     
这样处理 base case 很麻烦，而且注意一下状态转移方程，新状态只和相邻的一个状态有关，
可以用动态规划的降维打击：空间压缩技巧，不需要用整个 dp 数组，只需要一个变量储存相邻的那个状态就足够了，这样可以把空间复杂度降到 O(1):
```commandline
// 原始版本
int maxProfit_k_1(int[] prices) {
    int n = prices.length;
    int[][] dp = new int[n][2];
    for (int i = 0; i < n; i++) {
        if (i - 1 == -1) {
            // base case
            dp[i][0] = 0;
            dp[i][1] = -prices[i];
            continue;
        }
        dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]);
        dp[i][1] = Math.max(dp[i-1][1], -prices[i]);
    }
    return dp[n - 1][0];
}

// 空间复杂度优化版本
int maxProfit_k_1(int[] prices) {
    int n = prices.length;
    // base case: dp[-1][0] = 0, dp[-1][1] = -infinity
    int dp_i_0 = 0, dp_i_1 = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
        // dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
        // dp[i][1] = max(dp[i-1][1], -prices[i])
        dp_i_1 = Math.max(dp_i_1, -prices[i]);
    }
    return dp_i_0;
}
```
    
---

problems 122:
这道题的特点在于没有给出交易总数 k 的限制，也就相当于 k 为正无穷。
如果 k 为正无穷，那么就可以认为 k 和 k - 1 是一样的。可以这样改写框架：

```commandline
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
            = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])

我们发现数组中的 k 已经不会改变了，也就是说不需要记录 k 这个状态了：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
```

直接翻译成代码：

```java
// 原始版本
int maxProfit_k_inf(int[] prices) {
    int n = prices.length;
    int[][] dp = new int[n][2];
    for (int i = 0; i < n; i++) {
        if (i - 1 == -1) {
            // base case
            dp[i][0] = 0;
            dp[i][1] = -prices[i];
            continue;
        }
        dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]);
        dp[i][1] = Math.max(dp[i-1][1], dp[i-1][0] - prices[i]);
    }
    return dp[n - 1][0];
}

// 空间复杂度优化版本
int maxProfit_k_inf(int[] prices) {
    int n = prices.length;
    int dp_i_0 = 0, dp_i_1 = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
        int temp = dp_i_0;
        dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
        dp_i_1 = Math.max(dp_i_1, temp - prices[i]);
    }
    return dp_i_0;
}

```

---

第三题，看力扣第 309 题「 最佳买卖股票时机含冷冻期」，也就是 k 为正无穷，但含有交易冷冻期的情况：
和上一道题一样的，只不过每次 sell 之后要等一天才能继续交易，只要把这个特点融入上一题的状态转移方程即可：

```commandline
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
解释：第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 。
```


翻译成代码：
```java
// 原始版本
int maxProfit_with_cool(int[] prices) {
    int n = prices.length;
    int[][] dp = new int[n][2];
    for (int i = 0; i < n; i++) {
        if (i - 1 == -1) {
            // base case 1
            dp[i][0] = 0;
            dp[i][1] = -prices[i];
            continue;
        }
        if (i - 2 == -1) {
            // base case 2
            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]);
            // i - 2 小于 0 时根据状态转移方程推出对应 base case
            dp[i][1] = Math.max(dp[i-1][1], -prices[i]);
            //   dp[i][1] 
            // = max(dp[i-1][1], dp[-1][0] - prices[i])
            // = max(dp[i-1][1], 0 - prices[i])
            // = max(dp[i-1][1], -prices[i])
            continue;
        }
        dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]);
        dp[i][1] = Math.max(dp[i-1][1], dp[i-2][0] - prices[i]);
    }
    return dp[n - 1][0];
}

// 空间复杂度优化版本
int maxProfit_with_cool(int[] prices) {
    int n = prices.length;
    int dp_i_0 = 0, dp_i_1 = Integer.MIN_VALUE;
    int dp_pre_0 = 0; // 代表 dp[i-2][0]
    for (int i = 0; i < n; i++) {
        int temp = dp_i_0;
        dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
        dp_i_1 = Math.max(dp_i_1, dp_pre_0 - prices[i]);
        dp_pre_0 = temp;
    }
    return dp_i_0;
}

```

---
第四题，看力扣第 714 题「 买卖股票的最佳时机含手续费」，也就是 k 为正无穷且考虑交易手续费的情况：

每次交易要支付手续费，只要把手续费从利润中减去即可，改写方程：
```commandline
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
解释：相当于买入股票的价格升高了。
在第一个式子里减也是一样的，相当于卖出股票的价格减小了。
如果直接把 fee 放在第一个式子里减，会有一些测试用例无法通过，错误原因是整型溢出而不是思路问题。
一种解决方案是把代码中的 int 类型都改成 long 类型，避免 int 的整型溢出。
```

直接翻译成代码，注意状态转移方程改变后 base case 也要做出对应改变：
```commandline
// 原始版本
int maxProfit_with_fee(int[] prices, int fee) {
    int n = prices.length;
    int[][] dp = new int[n][2];
    for (int i = 0; i < n; i++) {
        if (i - 1 == -1) {
            // base case
            dp[i][0] = 0;
            dp[i][1] = -prices[i] - fee;
            //   dp[i][1]
            // = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
            // = max(dp[-1][1], dp[-1][0] - prices[i] - fee)
            // = max(-inf, 0 - prices[i] - fee)
            // = -prices[i] - fee
            continue;
        }
        dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
        dp[i][1] = Math.max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee);
    }
    return dp[n - 1][0];
}

// 空间复杂度优化版本
int maxProfit_with_fee(int[] prices, int fee) {
    int n = prices.length;
    int dp_i_0 = 0, dp_i_1 = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
        int temp = dp_i_0;
        dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
        dp_i_1 = Math.max(dp_i_1, temp - prices[i] - fee);
    }
    return dp_i_0;
}
```

---
第五题，看力扣第 123 题「 买卖股票的最佳时机 III」，也
就是 k = 2 的情况：
k = 2 和前面题目的情况稍微不同，因为上面的情况都和 k 的关系不太大：
要么 k 是正无穷，状态转移和 k 没关系了；
要么 k = 1，跟 k = 0 这个 base case 挨得近，最后也没有存在感。

这道题 k = 2 和后面要讲的 k 是任意正整数的情况中，对 k 的处理就凸显出来了

原始的状态转移方程，没有可化简的地方
```commandline
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
```
按照之前的代码，我们可能想当然这样写代码（错误的）：
```commandline
int k = 2;
int[][][] dp = new int[n][k + 1][2];
for (int i = 0; i < n; i++) {
    if (i - 1 == -1) {
        // 处理 base case
        dp[i][k][0] = 0;
        dp[i][k][1] = -prices[i];
        continue;
    }
    dp[i][k][0] = Math.max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);
    dp[i][k][1] = Math.max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]);
}
return dp[n - 1][k][0];

```
为什么错误？我这不是照着状态转移方程写的吗？

还记得前面总结的「穷举框架」吗？就是说我们必须穷举所有状态。其实我们之前的解法，都在穷举所有状态，只是之前的题目中 k 都被化简掉了。

比如说第一题，k = 1 时的代码框架：
```commandline
int n = prices.length;
int[][] dp = new int[n][2];
for (int i = 0; i < n; i++) {
    dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]);
    dp[i][1] = Math.max(dp[i-1][1], -prices[i]);
}
return dp[n - 1][0];

```
但当 k = 2 时，由于没有消掉 k 的影响，所以必须要对 k 进行穷举：

```commandline
// 原始版本
int maxProfit_k_2(int[] prices) {
    int max_k = 2, n = prices.length;
    int[][][] dp = new int[n][max_k + 1][2];
    for (int i = 0; i < n; i++) {
        for (int k = max_k; k >= 1; k--) {
            if (i - 1 == -1) {
                // 处理 base case
                dp[i][k][0] = 0;
                dp[i][k][1] = -prices[i];
                continue;
            }
            dp[i][k][0] = Math.max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);
            dp[i][k][1] = Math.max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]);
        }
    }
    // 穷举了 n × max_k × 2 个状态，正确。
    return dp[n - 1][max_k][0];
}


```
k 的 base case 是 0，按理说应该从 k = 1, k++ 这样穷举状态 k 才对？
而且如果你真的这样从小到大遍历 k，提交发现也是可以的。

这个疑问很正确，因为我们后文 动态规划答疑篇 有介绍 dp 数组的遍历顺序是怎么确定的，
主要是根据 base case，以 base case 为起点，逐步向结果靠近。

但为什么我从大到小遍历 k 也可以正确提交呢？
因为你注意看，dp[i][k][..] 不会依赖 dp[i][k - 1][..]，
而是依赖 dp[i - 1][k - 1][..]，而 dp[i - 1][..][..]，都是已经计算出来的，
所以不管你是 k = max_k, k--，还是 k = 1, k++，都是可以得出正确答案的。

那为什么我使用 k = max_k, k-- 的方式呢？因为这样符合语义：
你买股票，初始的「状态」是什么？
应该是从第 0 天开始，而且还没有进行过买卖，所以最大交易次数限制 k 应该是 max_k；
而随着「状态」的推移，你会进行交易，那么交易次数上限 k 应该不断减少，
这样一想，k = max_k, k-- 的方式是比较合乎实际场景的。

当然，这里 k 取值范围比较小，所以也可以不用 for 循环，直接把 k = 1 和 2 的情况全部列举出来也可以：
```commandline
// 状态转移方程：
// dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
// dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])
// dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
// dp[i][1][1] = max(dp[i-1][1][1], -prices[i])
```

```commandline
// 空间复杂度优化版本
int maxProfit_k_2(int[] prices) {
    // base case
    int dp_i10 = 0, dp_i11 = Integer.MIN_VALUE;
    int dp_i20 = 0, dp_i21 = Integer.MIN_VALUE;
    for (int price : prices) {
        dp_i20 = Math.max(dp_i20, dp_i21 + price);
        dp_i21 = Math.max(dp_i21, dp_i10 - price);
        dp_i10 = Math.max(dp_i10, dp_i11 + price);
        dp_i11 = Math.max(dp_i11, -price);
    }
    return dp_i20;
}
```

---
第六题，看力扣第 188 题「 买卖股票的最佳时机 IV」，即 k 可以是题目给定的任何数的情况：
有了上一题 k = 2 的铺垫，这题应该和上一题的第一个解法没啥区别，
你把上一题的 k = 2 换成题目输入的 k 就行了。

但试一下发现会出一个内存超限的错误，原来是传入的 k 值会非常大，dp 数组太大了。
那么现在想想，交易次数 k 最多有多大呢？
一次交易由买入和卖出构成，至少需要两天。
所以说有效的限制 k 应该不超过 n/2，
如果超过，就没有约束作用了，相当于 k 没有限制的情况， 而这种情况是之前解决过的。

所以我们可以直接把之前的代码重用：
```commandline
int maxProfit_k_any(int max_k, int[] prices) {
    int n = prices.length;
    if (n <= 0) {
        return 0;
    }
    if (max_k > n / 2) {
        // 复用之前交易次数 k 没有限制的情况
        return maxProfit_k_inf(prices);
    }

    // base case：
    // dp[-1][...][0] = dp[...][0][0] = 0
    // dp[-1][...][1] = dp[...][0][1] = -infinity
    int[][][] dp = new int[n][max_k + 1][2];
    // k = 0 时的 base case
    for (int i = 0; i < n; i++) {
        dp[i][0][1] = Integer.MIN_VALUE;
        dp[i][0][0] = 0;
    }

    for (int i = 0; i < n; i++) 
        for (int k = max_k; k >= 1; k--) {
            if (i - 1 == -1) {
                // 处理 i = -1 时的 base case
                dp[i][k][0] = 0;
                dp[i][k][1] = -prices[i];
                continue;
            }
            dp[i][k][0] = Math.max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);
            dp[i][k][1] = Math.max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]);     
        }
    return dp[n - 1][max_k][0];
}
```

---
请你实现如下函数：
```commandline
int maxProfit_all_in_one(int max_k, int[] prices, int cooldown, int fee);

输入股票价格数组 prices，你最多进行 max_k 次交易，
每次交易需要额外消耗 fee 的手续费，
而且每次交易之后需要经过 cooldown 天的冷冻期才能进行下一次交易，
请你计算并返回可以获得的最大利润。
```

```commandline
// 同时考虑交易次数的限制、冷冻期和手续费
int maxProfit_all_in_one(int max_k, int[] prices, int cooldown, int fee) {
    int n = prices.length;
    if (n <= 0) {
        return 0;
    }
    if (max_k > n / 2) {
        // 交易次数 k 没有限制的情况
        return maxProfit_k_inf(prices, cooldown, fee);
    }

    int[][][] dp = new int[n][max_k + 1][2];
    // k = 0 时的 base case
    for (int i = 0; i < n; i++) {
        dp[i][0][1] = Integer.MIN_VALUE;
        dp[i][0][0] = 0;
    }

    for (int i = 0; i < n; i++) 
        for (int k = max_k; k >= 1; k--) {
            if (i - 1 == -1) {
                // base case 1
                dp[i][k][0] = 0;
                dp[i][k][1] = -prices[i] - fee;
                continue;
            }

            // 包含 cooldown 的 base case
            if (i - cooldown - 1 < 0) {
                // base case 2
                dp[i][k][0] = Math.max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);
                // 别忘了减 fee
                dp[i][k][1] = Math.max(dp[i-1][k][1], -prices[i] - fee);
                continue;
            }
            dp[i][k][0] = Math.max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);
            // 同时考虑 cooldown 和 fee
            dp[i][k][1] = Math.max(dp[i-1][k][1], dp[i-cooldown-1][k-1][0] - prices[i] - fee);     
        }
    return dp[n - 1][max_k][0];
}

// k 无限制，包含手续费和冷冻期
int maxProfit_k_inf(int[] prices, int cooldown, int fee) {
    int n = prices.length;
    int[][] dp = new int[n][2];
    for (int i = 0; i < n; i++) {
        if (i - 1 == -1) {
            // base case 1
            dp[i][0] = 0;
            dp[i][1] = -prices[i] - fee;
            continue;
        }

        // 包含 cooldown 的 base case
        if (i - cooldown - 1 < 0) {
            // base case 2
            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]);
            // 别忘了减 fee
            dp[i][1] = Math.max(dp[i-1][1], -prices[i] - fee);
            continue;
        }
        dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
        // 同时考虑 cooldown 和 fee
        dp[i][1] = Math.max(dp[i - 1][1], dp[i - cooldown - 1][0] - prices[i] - fee);
    }
    return dp[n - 1][0];
}
```

你可以用这个 maxProfit_all_in_one 函数去完成之前讲的 6 道题目，
因为我们无法对 dp 数组进行优化，所以执行效率上不是最优的，但正确性上肯定是没有问题的。

如何通过状态转移的方法解决复杂的问题:
关键就在于列举出所有可能的「状态」，然后想想怎么穷举更新这些「状态」。
一般用一个多维 dp 数组储存这些状态，
从 base case 开始向后推进，推进到最后的状态，就是我们想要的答案。

具体到股票买卖问题，我们发现了三个状态，使用了一个三维数组，无非还是穷举 + 更新，

