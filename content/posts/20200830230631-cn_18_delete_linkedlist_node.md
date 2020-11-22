+++
title = "CN-18. Delete LinkedList Node"
author = ["John Doe"]
draft = false
+++

last modified
: 2020-08-30 23:08:35


tags
: [LinkedList]({{< relref "20200813223551-linkedlist" >}}), [Recursion]({{< relref "20200813223609-recursive" >}})

source
: [leetcode-cn](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/)


## Edge Cases {#edge-cases}


## Solution 1 - Single/Two Pointer {#solution-1-single-two-pointer}

```java
class Solution {
    public ListNode deleteNode(ListNode head, int val) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;

        ListNode p = dummy;
        while (p.next != null) {
            if (p.next.val == val) {
                p.next = p.next.next;
                break;
            }
            p = p.next;
        }

        return dummy.next;
    }
}
```


### Complexity {#complexity}

-   time: O(N)
-   space: O(1)


## Solution 2 - Recursion {#solution-2-recursion}

```java
class Solution {
    public ListNode deleteNode(ListNode head, int val) {
        if (head == null) return null;
        if (head.val == val) return head.next;
        head.next = deleteNode(head.next, val);
        return head;
    }
}
```


### Complexity {#complexity}

-   time: O(N)
-   space: O(N)
