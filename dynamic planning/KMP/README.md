[有限状态机---KMP字符匹配算法](https://labuladong.github.io/algo/3/28/97/)

```java
public class KMP {
    private int[][] dp;
    private String pat;

    public KMP(String pat) {
        this.pat = pat;
        int M = pat.length();
        // dp[状态][字符] = 下个状态
        dp = new int[M][256];
        // base case
        dp[0][pat.charAt(0)] = 1;
        // 影子状态 X 初始为 0
        int X = 0;
        // 构建状态转移图（稍改的更紧凑了）
        for (int j = 1; j < M; j++) {
            for (int c = 0; c < 256; c++)
                dp[j][c] = dp[X][c];
            dp[j][pat.charAt(j)] = j + 1;
            // 更新影子状态
            X = dp[X][pat.charAt(j)];
        }
    }

    public int search(String txt) {
        int M = pat.length();
        int N = txt.length();
        // pat 的初始态为 0
        int j = 0;
        for (int i = 0; i < N; i++) {
            // 计算 pat 的下一个状态
            j = dp[j][txt.charAt(i)];
            // 到达终止态，返回结果
            if (j == M) return i - M + 1;
        }
        // 没到达终止态，匹配失败
        return -1;
    }
}
```

传统的 KMP 算法是使用一个一维数组 next 记录前缀信息，而本文是使用一个二维数组 dp 以状态转移的角度解决字符匹配问题，但是空间复杂度仍然是 O(256M) = O(M)。

在 pat 匹配 txt 的过程中，只要明确了「当前处在哪个状态」和「遇到的字符是什么」这两个问题，就可以确定应该转移到哪个状态（推进或回退）。

对于一个模式串 pat，其总共就有 M 个状态，对于 ASCII 字符，总共不会超过 256 种。所以我们就构造一个数组 dp[M][256] 来包含所有情况，并且明确 dp 数组的含义：

dp[j][c] = next 表示，当前是状态 j，遇到了字符 c，应该转移到状态 next。

明确了其含义，就可以很容易写出 search 函数的代码。

对于如何构建这个 dp 数组，需要一个辅助状态 X，它永远比当前状态 j 落后一个状态，拥有和 j 最长的相同前缀，我们给它起了个名字叫「影子状态」。

在构建当前状态 j 的转移方向时，只有字符 pat[j] 才能使状态推进（dp[j][pat[j]] = j+1）；而对于其他字符只能进行状态回退，应该去请教影子状态 X 应该回退到哪里（dp[j][other] = dp[X][other]，其中 other 是除了 pat[j] 之外所有字符）。

对于影子状态 X，我们把它初始化为 0，并且随着 j 的前进进行更新，更新的方式和 search 过程更新 j 的过程非常相似（X = dp[X][pat[j]]）。