+++
title = "833. Find And Replace in String"
author = ["John Doe"]
draft = false
+++

Time-stamp: <2020-11-21 01:03:43 gyh"timestamp-wrapper"><span class="timestamp">&lt;2020-08-03 Mon 22:54&gt;</span></span>

tags
: [subarray]({{< relref "20200716205913-subarray" >}})

source
: [leetcode](https://leetcode.com/problems/find-and-replace-in-string/)


## Edge Cases {#edge-cases}

index array may not sorted


## Solution {#solution}

```java
class Solution {
    public String findReplaceString(String S, int[] indexes, String[] sources, String[] targets) {
        StringBuilder sb = new StringBuilder();
        int[] match = new int[S.length()];
        Arrays.fill(match, -1);

        for (int i = 0; i < sources.length; i++) {
            String source = sources[i];
            if (S.substring(indexes[i], indexes[i] + source.length()).equals(source)) {
                match[indexes[i]] = i;
            }
        }

        int i = 0;
        while (i < S.length()) {
            if (match[i] >= 0) {
                sb.append(targets[match[i]]);
                i += sources[match[i]].length();
            } else {
                sb.append(S.charAt(i));
                i++;
            }
        }

        return sb.toString();
    }
}
```


### Complexity {#complexity}

-   time: O(NQ), N is length of S, Q is number of append times
-   space: O(N)
