+++
title = "CN-06.Print Linked List Reversely"
author = ["John Doe"]
draft = false
+++

tags
: [Recursion]({{< relref "20200813223609-recursive" >}})

source
: [leetcode-cn](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/)


## Edge Cases {#edge-cases}


## Solution 1 - reverse the list {#solution-1-reverse-the-list}

Allow to change original data

```java
class Solution {
    public int[] reversePrint(ListNode head) {
        if (head == null) return new int[0];
        ListNode dummy = new ListNode(-1);
        ListNode p1 = dummy, p2 = head;
        int count = 0;
        while (p2 != null) {
            ListNode tmp = p2.next;
            p2.next = p1.next;
            p1.next = p2;
            p2 = tmp;
            count++;
        }

        int[] num = new int[count];
        p1 = dummy.next;
        count = 0;
        while (p1 != null) {
            num[count++] = p1.val;
            p1 = p1.next;
        }

        return num;
    }
}
```


### Complexity {#complexity}

-   time: O(N)
-   space: O(1)


## Solution 2 - go twice {#solution-2-go-twice}

Not allow to change

1.  first iteration, get count
2.  second iteration, start from `num` end and list's first


### Complexity {#complexity}

-   time: O(N)
-   space: O(1)


## Solution 3 - Stack {#solution-3-stack}

Not allow to change


### Complexity {#complexity}

-   time: O(N)
-   space: O(N)


## Solution 4 - Recursion {#solution-4-recursion}

Not allow to change


### Complexity {#complexity}

-   time: O(N)
-   space: O(N)
