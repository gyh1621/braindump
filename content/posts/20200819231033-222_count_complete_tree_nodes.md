+++
title = "222. Count Complete Tree Nodes"
author = ["John Doe"]
draft = false
+++

Time-stamp: <2020-11-21 01:04:44 gyh"timestamp-wrapper"><span class="timestamp">&lt;2020-08-19 Wed 23:15&gt;</span></span>

tags
: [Tree]({{< relref "20200813232106-tree" >}}), [BinarySearch]({{< relref "20200819231114-binarysearch" >}}), [Recursion]({{< relref "20200813223609-recursive" >}})

source
: [leetcode](https://leetcode.com/problems/count-complete-tree-nodes/)


## Edge Cases {#edge-cases}


## Solution 1 - Recursion {#solution-1-recursion}

****NOTE****: this can also apply to non-complete tree

```java
class Solution {
    public int countNodes(TreeNode root) {
        return root == null ? 0 : 1 + countNodes(root.left) + countNodes(root.right);
    }
}
```


### Complexity {#complexity}

-   time: O(N)
-   space: O(lgN)


## Solution 2 - Binary Search {#solution-2-binary-search}

key is to find number of leafs in the final level

use binary search to find first position missing: O(d)
when doing binary search, we need to test if the node exists in each compare, use binary search again to go down the tree: O(d)

```java
class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) return 0;

        // compute depth
        int d = computeDepth(root);

        // binary search
        int left = 0, right = (int) Math.pow(2, d) - 1;
        while (left <= right) {
            int pivot = (left + right) / 2;
            if (exists(root, d, pivot)) left = pivot + 1;
            else right = pivot - 1;
        }

        return left + (int) Math.pow(2, d) - 1;
    }

    private int computeDepth(TreeNode root) {
        int d = 0;
        while (root != null) {
            root = root.left;
            d++;
        }
        return d - 1;
    }

    private boolean exists(TreeNode root, int d, int idx) {
        int left = 0, right = (int) Math.pow(2, d) - 1;
        for (int i = 0; i < d; i++) {
            int mid = (left + right) / 2;
            if (idx <= mid) {
                root = root.left;
                right = mid;
            } else {
                root = root.right;
                left = mid + 1;
            }
        }
        return root != null;
    }
}
```


### Complexity {#complexity}

-   time: O(d^2)
-   space: O(1)
