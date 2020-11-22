+++
title = "CN-07. Rebuild binary tree"
author = ["John Doe"]
draft = false
+++

last modified
: 2020-08-25 20:22:17


tags
: [BinaryTree]({{< relref "20200824221056-binarytree" >}}), [Recursion]({{< relref "20200813223609-recursive" >}})

source
: [leetcode-cn](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/)


## Edge Cases {#edge-cases}


## Solution {#solution}

```java
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0) return null;
        Map<Integer, Integer> index = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            index.put(inorder[i], i);
        }
        return buildTreeHelper(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1, index);
    }

    private TreeNode buildTreeHelper(int[] preorder, int pl, int pr, int[] inorder, int il, int ir, Map<Integer, Integer> index) {
        if (pl == pr) { // or il == ir
            return new TreeNode(preorder[pl]);
        }
        if (pl > pr || il > ir) {
            return null;
        }
        // root node
        TreeNode root = new TreeNode(preorder[pl]);

        // find left tree part
        int leftSize = index.get(root.val) - il;

        // build child tree
        root.left = buildTreeHelper(preorder, pl + 1, pl + leftSize, inorder, il, il + leftSize - 1, index);
        root.right = buildTreeHelper(preorder, pl + leftSize + 1, pr, inorder, il + leftSize + 1, ir, index);

        return root;
    }
}
```


### Complexity {#complexity}

-   time: O(N) + O(N)
-   space: O(N)
