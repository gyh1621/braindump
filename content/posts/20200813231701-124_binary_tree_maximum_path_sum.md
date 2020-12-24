+++
title = "124. Binary Tree Maximum Path Sum"
author = ["John Doe"]
draft = false
+++

tags
: [Recursion]({{< relref "20200813223609-recursive" >}}), [Tree]({{< relref "20200813232106-tree" >}})

source
: [leetcode](https://leetcode.com/problems/binary-tree-maximum-path-sum/)


## Edge Cases {#edge-cases}


## Solution {#solution}

start from current node, get left node's max path sum, right node's max path sum
max path sum of the tree with current node as root is

1.  left path max sum + root.val
2.  right path max sum + root.val
3.  left + right + root.val  // start a new path

<!--listend-->

```java
class Solution {
    int maxSum = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        helper(root);
        return maxSum;
    }

    private int helper(TreeNode root) {
        if (root == null) return 0;

        int leftGain = Math.max(helper(root.left), 0);
        int rightGain = Math.max(helper(root.right), 0);

        // continue the same path
        int sameMax = Math.max(leftGain + root.val, rightGain + root.val);

        // or start a new path
        maxSum = Math.max(leftGain + root.val + rightGain, maxSum);


        return sameMax;
    }

}
```


### Complexity {#complexity}

-   time: O(N)
-   space: O(H)
