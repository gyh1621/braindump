+++
title = "136. Number only show once"
author = ["Yuhang Guo"]
draft = false
+++

tags
: [trick]({{< relref "20200722211911-trick" >}}), [BinaryOperation]({{< relref "20200830220657-binaryoperation" >}})

source
: [leetcode-cn](https://leetcode-cn.com/problems/single-number/)


## Edge Cases {#edge-cases}


## Solution - O(N) Space {#solution-o--n--space}

1.  use set, when number in set, delete it; not in set, add it.
    after one iteration, left is the number only shows once
2.  hashset, store number showing times
3.  set store all numbers, get sum1 from set, sum1 \* 2 - sum(array) = answer


### Complexity {#complexity}

-   time: O(N)
-   space:


## Solution - BinaryOperation {#solution-binaryoperation}

```nil
a xor 0 = a
a xor a = 0
a xor b xor c = a xor c xor b = a xor (c xor b)
```

iterate whole array, xor every item, left is answer


### Complexity {#complexity}

-   time: O(N)
-   space: O(1)
