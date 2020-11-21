+++
title = "CN-11. Find smallest number in the shifted array"
author = ["John Doe"]
draft = false
+++

Time-stamp: <2020-11-21 01:04:44 gyh"timestamp-wrapper"><span class="timestamp">&lt;2020-08-25 Tue 23:14&gt;</span></span>

tags
: [BinarySearch]({{< relref "20200819231114-binarysearch" >}})

source
: [leetcode-cn](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)


## Edge Cases {#edge-cases}


## Solution {#solution}

```java
class Solution {
    public int minArray(int[] numbers) {
        int left = 0, right = numbers.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (numbers[mid] < numbers[right]) {
                right = mid;
            } else if (numbers[mid] > numbers[right]) {
                left = mid + 1;
            } else {
                right -= 1;  // important
            }
        }

        return numbers[left];
    }
}
```


### Complexity {#complexity}

-   time: O(lgN), worst O(N)
-   space: O(1)
