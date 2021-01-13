+++
title = "11. Container With Most Water"
author = ["Yuhang Guo"]
draft = false
+++

tags
: [two pointers]({{< relref "20200720224430-two_pointers" >}})

source
: [Leetcode](https://leetcode.com/problems/container-with-most-water/)


## Solution {#solution}

```java
class Solution {
    public int maxArea(int[] height) {
        int l = 0, r = height.length - 1;
        int max = 0;

        while (l <= r) {
            max = Math.max(max, Math.min(height[l], height[r]) * (r - l));
            if (height[l] <= height[r]) {
                l++;
            } else {
                r--;
            }
        }

        return max;
    }
}
```


## Complexity {#complexity}

-   time: O(N)
-   space: O(1)
