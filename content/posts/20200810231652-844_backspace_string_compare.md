+++
title = "844. Backspace String Compare"
author = ["Yuhang Guo"]
draft = false
+++

tags
: [two pointers]({{< relref "20200720224430-two_pointers" >}})

source
: [leetcode](https://leetcode.com/problems/backspace-string-compare/)


## Edge Cases {#edge-cases}

```nil
"bbbextm"
"bbb#extm"
```


## Solution {#solution}

scan from end of strings

```java
class Solution {
    public boolean backspaceCompare(String S, String T) {
        int i = S.length() - 1, j = T.length() - 1;

        int skipS = 0, skipT = 0;
        while (i >= 0 || j >= 0) {  // see edge case
            while (i >= 0) {
                if (S.charAt(i) == '#') {
                    skipS++;
                    i--;
                } else if (skipS > 0) {
                    skipS--;
                    i--;
                } else {
                    break;
                }
            }
            while (j >= 0) {
                if (T.charAt(j) == '#') {
                    skipT++;
                    j--;
                } else if (skipT > 0) {
                    skipT--;
                    j--;
                } else {
                    break;
                }
            }

            if ((i >= 0) != (j >= 0)) return false;
            if (i >= 0 && j >= 0 && S.charAt(i) != T.charAt(j)) return false;
            i--;
            j--;
        }

        return true;
    }
}
```


### Complexity {#complexity}

-   time: O(M+N)
-   space: O(1)
