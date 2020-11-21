+++
title = "CN-04.Search a 2d matrix ii"
author = ["John Doe"]
draft = false
+++

Time-stamp: <2020-11-21 01:04:29 gyh"timestamp-wrapper"><span class="timestamp">&lt;2020-09-17 Thu 00:12&gt;</span></span>

tags
: [BinarySearchTree]({{< relref "20200824221146-binarysearchtree" >}})

source
: [leetcode-cn](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)


## Edge Cases {#edge-cases}


## Solution {#solution}

{{< figure src="/ox-hugo/2020-08-24_22-12-45_5BF34F21-34A8-4835-BCE5-788D5BBF4747.png" >}}

```java
class Solution {
    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        if (matrix == null) return false;
        int R = matrix.length;
        if (R == 0) return false;
        int C = matrix[0].length;

        int r = 0, c = C - 1;
        while (r < R && c >= 0) {
            if (matrix[r][c] == target) return true;
            else if (matrix[r][c] < target) r++;
            else c--;
        }

        return false;
    }
}
```


### Complexity {#complexity}

-   time: O(M + N)
-   space: O(1)
