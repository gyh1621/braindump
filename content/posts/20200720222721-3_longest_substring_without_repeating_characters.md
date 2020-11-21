+++
title = "3. Longest Substring Without Repeating Characters"
author = ["John Doe"]
draft = false
+++

Time-stamp: <2020-11-21 01:04:10 gyh"timestamp-wrapper"><span class="timestamp">&lt;2020-07-20 Mon 22:29&gt;</span></span>

tags
: [sliding window]({{< relref "20200716205834-sliding_window" >}}), [subarray]({{< relref "20200716205913-subarray" >}})


## Solution {#solution}

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<>();

        int maxLen = 0;
        for (int i = 0, j = 0; i < s.length(); i++) {
            if (map.containsKey(s.charAt(i))) {
                j = Math.max(j, map.get(s.charAt(i)) + 1);
            }
            map.put(s.charAt(i), i);
            maxLen = Math.max(maxLen, i - j + 1);
        }

        return maxLen;
    }
}
```

NOTICE: `j = Math.max(j, map.get(s.charAt(i)) + 1);`


## Complexity {#complexity}

-   time:  O(N)
-   space: O(N)
