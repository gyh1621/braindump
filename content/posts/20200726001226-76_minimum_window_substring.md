+++
title = "76. Minimum Window Substring"
author = ["Yuhang Guo"]
draft = false
+++

tags
: [sliding window]({{< relref "20200716205834-sliding_window" >}}), [subarray]({{< relref "20200716205913-subarray" >}})

source
: [leetcode](https://leetcode.com/problems/minimum-window-substring/)


## Edge Cases {#edge-cases}

```nil
"aa"
"aa"
```

```nil
"aaflslflsldkalskaaa"
"aaa"
```

```nil
"abc"
"a"
```


## Solution {#solution}

```java
class Solution {
    public String minWindow(String s, String t) {
        int[] count = new int[128];

        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        int found = 0, required = 0;
        for (char c: tArray) {
            count[c]++;
            required++;
        }

        int minL = -1, minR = -1;
        for (int l = 0, r = 0; r < sArray.length; r++) {
            count[sArray[r]]--;

            if (count[sArray[r]] >= 0) found++;

            if (found == required) {
                while (count[sArray[l]] != 0) count[sArray[l++]]++;
                if (minR == -1 || (r - l) < (minR - minL)) {
                    minR = r;
                    minL = l;
                }
                count[sArray[l++]]++;
                found--;
            }
        }

        return minR == -1 ? "" : s.substring(minL, minR + 1);
    }
}
```


## Complexity {#complexity}

-   time: O(N)
-   space: O(N + M)
